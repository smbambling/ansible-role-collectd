# CollectD 

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

CollectD Installation and Configuration

## Requirements

This role requires Ansible 2.3 or higher and platform requirements are
listed in the [metadata](meta/main.yml) file.

## Role Variables

The variables that can be passed to this role and a brief description about
them are as follows. (For all variables, take a look at defaults/main.yml)

| Name              | Default | Type        | Description         |
| ------------------|---------| ------------| --------------------|
| | | |


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
