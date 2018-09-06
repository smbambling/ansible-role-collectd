import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_services(host):
    service = host.service("collectd")
    with host.sudo():
        assert service.is_running
        assert service.is_enabled
