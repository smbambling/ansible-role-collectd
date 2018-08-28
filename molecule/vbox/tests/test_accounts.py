import pytest
import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize(
    'name,uid,comment,primary_group,secondary_group,auth_key', [
        ('tmonkey1', '1006', 'Test Monkey 1',
         'tmonkey1', 'root', 'FAKEKEYSUTFF== tmonkey1'),
        ('tmonkey2', '1007', 'Test Monkey 2',
         'tmonkey2', 'root', 'FAKEKEYSUTFF== tmonkey2'),
        ('tmonkey3', '1008', 'Test Monkey 3',
         'monkeys', 'root', 'FAKEKEYSUTFF== tmonkey3'),
        ('tmonkey4', None, None, 'tmonkey4', None, None)
    ])
def test_sweng_user(host, name, uid, comment,
                    primary_group, secondary_group, auth_key):
    user = host.user(name)

    if uid:
        assert user.uid == int(uid)
    assert user.group == primary_group
    if secondary_group:
        assert secondary_group in user.groups

    if comment:
        assert user.gecos == comment

    if auth_key:
        with host.sudo():
            auth_keys = host.file('{}/.ssh/authorized_keys'.format(user.home))
            assert auth_key in auth_keys.content_string
