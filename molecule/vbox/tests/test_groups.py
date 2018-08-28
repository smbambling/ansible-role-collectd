import pytest
import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('group', [
    ['monkeys', 2000],
    ['beatles', None],
])
def test_ops_group(host, group):
    assert host.group(group[0]).exists
    if group[1]:
        assert host.group(group[0]).gid == group[1]
