import pytest
import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('name,order', [
    ("logfile", "00"),
    ("disk", "10"),
    ("cpu", "10")
])
def test_file(host, name, order):
    if host.system_info.distribution.lower() in ['freebsd']:
        collectd_config_owner = 'root'
        collectd_config_group = 'wheel'
        collectd_plugin_conf_dir = '/usr/local/etc/collectd.d'
        collectd_plugin_conf_dir_mode = '0750'
    elif host.system_info.distribution.lower() in ['openbsd']:
        collectd_config_owner = 'root'
        collectd_config_group = '_collectd'
        collectd_plugin_conf_dir = '/etc/collectd.d'
        collectd_plugin_conf_dir_mode = '0750'
    else:
        collectd_config_owner = 'root'
        collectd_config_group = 'root'
        collectd_plugin_conf_dir = '/etc/collectd.d'
        collectd_plugin_conf_dir_mode = '0750'

    with host.sudo():
        file = host.file("{}/{}_{}.conf".format(collectd_plugin_conf_dir, order, name)) # noqa:E501
        assert file.is_file
        assert file.user == collectd_config_owner
        assert file.group == collectd_config_group
        assert oct(file.mode) == collectd_plugin_conf_dir_mode
        assert "LoadPlugin {}".format(name) in file.content
