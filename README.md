# Collectd

[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-smbambling.collectd-blue.svg)](https://galaxy.ansible.com/smbambling/ansible-role-collectd/)
[![Build Status](https://travis-ci.org/smbambling/ansible-role-collectd.svg?branch=master)](https://travis-ci.org/smbambling/ansible-role-collectd)
[![CodeClimate](https://codeclimate.com/github/smbambling/ansible-role-collectd/badges/gpa.svg)](https://codeclimate.com/github/smbambling/ansible-role-collectd)
[![IssueCount](https://codeclimate.com/github/smbambling/ansible-role-collectd/badges/issue_count.svg)](https://codeclimate.com/github/smbambling/ansible-role-collectd)

## Table of Contents

1. [Overview](#overview)
1. [Requirements](#requirements)
1. [Role Variables](#role-variables)
1. [Dependencies](#dependencies)
1. [Examples](#examples)
1. [Development / Contributing](#development--contributing)
1. [License](#license)
1. [Author Information](#author-information)

## Overview

Collectd Installation and Configuration

## Requirements

This role requires Ansible 2.3 or higher and platform requirements are
listed in the [metadata](meta/main.yml) file.

## Role Variables

> Variables listed in **main/defaults.yml** with no value are considered to have a value of 'none'. If these variables are left unset, they are assigned a value from the _collectd\_variables\_overrides_ task using the set_fact Ansible module. The values are obtained from the collectd role variables in /vars/* based on the OS family.

The variables that can be passed to this role and a brief description about
them are as follows. (For all variables, take a look at defaults/main.yml)

| Name              | Default | Type        | Description         |
| ------------------|---------| ------------| --------------------|
| collectd\_service\_name| collectd | String | Name of the collectd service |
| collectd\_packages | See role variables (/vars)  | Array | List of packages|
| collectd\_version | See role variables (/vars) | String | Version of the collectd package(s) to install |
| collectd\_yum\_repo\_baseurl | See role variables (/vars) | String| YUM repository base url |
| collectd\_yum\_repo\_rpm\_key| See role variables (/vars) | String | YUM repository RPM Key|
| collectd\_yum\_repo\_enabled| See role variables (/vars) | Boolean | Enable YUM repository |
| collectd\_config\_file | See role variables (/vars) | String| Configuration file location|
| collectd\_config\_owner| root | String | Configuration file(s) owner |
| collectd\_config\_group | See role variables (/vars) | String| configuration file(s) group |
| collectd\_config\_mode| 0640 | Int | Configuration file(s) mode |
| collectd\_plugin\_conf\_dir | See role variables (/vars) | String | Plugins directory |
| collectd\_plugin\_conf\_dir\_mode | 0750 | Int | Plugins directory mode|
| collectd\_plugin\_conf\_order| 10 | Int | Plugin file prefix, to set load order when available|
| collectd\_conf\_autoloadplugin | false | Boolean | Set the AutoLoadPlugin value in the collectd configuration|
| collectd\_config\_typesdb | See role variables (/vars) | Array | Set the TypesDB value(s) in the collectd configuration|
| collectd\_config\_write\_queue\_limit\_high | See role variables (/vars) | String | Enable/Set the WriteQueueLimitHigh value in the collectd configuration  |
| collectd\_config\_write\_queue\_limit\_low | See role variables (/vars) | String | Enable/Set the WriteQueueLimitLow value in the collectd configuration  |
| collectd\_config\_interval| 60 | Int | Set the Interval value in the collectd configuration |
| collectd\_config\_timeout | 2 | Int | Set the Timeout value in the collectd configuration|
| collectd\_config\_read\_threads| 5 | Int | Set the ReadThreads value in the collectd configuration|
| collectd\_config\_write\_threads| 5 | Int | Set the WriteThreads value in the collectd configuration|
| collectd\_plugins| See **Collectd Plugins** below | Array of Dictionaries | Manage/Configure plugins and values|
| collectd\_disabled\_plugins | []| Array | List of plugins and should be disabled and configuration file(s) removed|

### Collectd Plugins

This role provides several methods for managing/configuring Collectd plugins.

#### Basic

You can override the *collectd\_plugins* variable as a single configuration within your projects host/group variables when calling this role from within your projects playbook

```yaml
## Playbook reference
roles:
    - {role: ansible-role-collectd}

## Host/Group variable reference
collectd_plugins:
  - name: logfile
    order: '00'
    options:
      LogLevel: "info"
      File: "/var/log/collectd.log"
      Timestamp: true
      PrintSeverity: false
```

#### Nested Variables

You can also override the *collectd\_plugins* variable by nesting multiple variables per plugin. 

See the example below where the *collectd\_plugin_logfile* plugin is nested within the *collectd\_plugins* variable.  Allowing you to override just the *collectd\_plugin\_logfile* as needed based on host/group without the need to manage the entire *collectd\_plugins* variable block

```yaml
collectd_plugin_logfile:
  - name: logfile
    order: '00'
    options:
      LogLevel: "info"
      File: "/var/log/collectd.log"
      Timestamp: true
      PrintSeverity: false

collectd_plugins:
  "{{ collectd_plugin_logfile }}"
```

#### Include Role Class

You can also use the Ansible include_role module with the task\_from attribute to call the *plugins\_class* task file to manage any plugins. 

This method can be used when you have included this role from within another role such as a "base" role to install/manage the collectd service and any default plugins you wish such as CPU/Memory.  But have an additional role as one for your web servers that you want to manage the Apache plugin for.

```yaml
tasks:
    - name: Install Collectd Disk Plugin
      include_role:
        name: ansible-role-collectd
        tasks_from: plugins_class.yml
      vars:
        - name: apache
          options:
            Instance: apache80
              URL: http://localhost/mod_status?auto
              User: collectd
              Password: hoh2Coo6
```

## Dependencies

None

## Examples

### Example Playbook

See the Molecule testing [Playbook](molecule/default/playbook.yml) for an example

## Development / Contributing

See [Contributing](.github/CONTRIBUTING.md).

This role has been tested against the following distributions and Ansible version:

|Distribution|Ansible 2.3|Ansible 2.4|Ansible 2.5|Ansible 2.6| Notes |
|------------|-----------|-----------|-----------|-----------|-------|
|**Centos 6**|<span style="color:green">Yes</span>|<span style="color:green">Yes</span>|<span style="color:green">Yes</span>|<span style="color:green">Yes</span>||
|**Centos 7**|<span style="color:green">Yes</span>|<span style="color:green">Yes</span>|<span style="color:green">Yes</span>|<span style="color:red">No</span>|Requires two runs to enable service with Ansible 2.6|
|**FreeBSD 11.2**|<span style="color:green">Yes</span>|<span style="color:green">Yes</span>|<span style="color:green">Yes</span>|<span style="color:green">Yes</span>||
|**OpenBSD 6.3**|<span style="color:green">Yes</span>|<span style="color:green">Yes</span>|<span style="color:green">Yes</span>|<span style="color:green">Yes</span>||

## License

Licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Author Information

- Steven Bambling