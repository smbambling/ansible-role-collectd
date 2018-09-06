import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_collectd_repo(host):
    if host.system_info.distribution.lower() in ['centos', 'redhat']:
        output = host.check_output('yum repolist all')
        assert 'collectd' in output
        assert 'enabled' in output
