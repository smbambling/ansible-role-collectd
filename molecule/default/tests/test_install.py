import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_package(host):
    if host.system_info.distribution.lower() in ['freebsd']:
        collectd_pkg = 'collectd5'
    else:
        collectd_pkg = 'collectd'
    pkg = host.package(collectd_pkg)
    assert pkg.is_installed
