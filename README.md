# Ansible amq role

This is an [Ansible](http://www.ansible.com) role which deploys a RedHat AMQ Broker active-pasive two node cluster using jping and nfs share.

## Role Variables

A list of all the default variables for this role is available in `defaults/main.yml`. The role setups the following facts:

- `amq_broker_cluster_nodes`: list of dicts with the broker nodes

## Filters

The role provides these filters:

- `urlsplit_splitquery`: given the dictionary returned by the urlsplit filter parses the query key into a dictionary
- `urlcombine`: composes a URL from a dictionary using the same keys as produced by the urlsplit filter

## Usage

This is an example playbook:

```yaml
---

- hosts: all
  tasks:
    - include_role:
        name: amtega.amq
```

## Testing

Tests are based on molecule with vagrant virtual machines. Follow the instructions in `molecule/default/INSTALL.rst`.

To run the tests you have to pass the following variables:

- `ANSIBLE_INVENTORY`: path to an inventory providing the variables `amq_artifact` and `amq_broker_login`
- `ANSIBLE_VAULT_PASSWORD_FILE`: path to the file containing the vault password required for the previous inventory

```shell
cd amtega.amq

export ANSIBLE_INVENTORY=~/myinventory ANSIBLE_VAULT_PASSWORD_FILE=~/myvaultpassword
molecule test
```

## License

Copyright (C) 2020 AMTEGA - Xunta de Galicia

This role is free software: you can redistribute it and/or modify it under the terms of:

GNU General Public License version 3, or (at your option) any later version; or the European Union Public License, either Version 1.2 or – as soon they will be approved by the European Commission ­subsequent versions of the EUPL.

This role is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details or European Union Public License for more details.

## Author Information

- Daniel Sánchez Fábregas
- Juan Antonio Valiño García
- This role is heavyly based in https://github.com/redhat-cop/jboss_amq
