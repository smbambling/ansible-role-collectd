import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_collectd_config(host):
    if host.system_info.distribution.lower() in ['freebsd']:
        collectd_config_file = '/usr/local/etc/collectd.conf'
        collectd_config_owner = 'root'
        collectd_config_group = 'wheel'
        collectd_config_mode = '0640'
    elif host.system_info.distribution.lower() in ['openbsd']:
        collectd_config_file = '/etc/collectd.conf'
        collectd_config_owner = 'root'
        collectd_config_group = '_collectd'
        collectd_config_mode = '0640'
    else:
        collectd_config_file = '/etc/collectd.conf'
        collectd_config_owner = 'root'
        collectd_config_group = 'root'
        collectd_config_mode = '0640'

    with host.sudo():
        file = host.file(collectd_config_file)
        assert file.is_file
        assert file.user == collectd_config_owner
        assert file.group == collectd_config_group
        assert oct(file.mode) == collectd_config_mode
        assert "AutoLoadPlugin false" in file.content


def test_collectd_d_dir(host):
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
        collectd_plugin_conf_dir = 'etc/collectd.d'
        collectd_plugin_conf_dir_mode = '0750'

    with host.sudo():
        directory = host.file(collectd_plugin_conf_dir)
        assert directory.is_directory
        assert directory.user == collectd_config_owner
        assert directory.group == collectd_config_group
        assert oct(directory.mode) == collectd_plugin_conf_dir_mode


def test_collectd_config_typesdb(host):
    if host.system_info.release.split('.')[0] == '6':
        collectd_config_file = '/etc/collectd.conf'

        with host.sudo():
            file = host.file(collectd_config_file)
            assert "foobar.db" in file.content
