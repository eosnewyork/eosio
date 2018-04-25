** A Work in Progress **

# Using Ansible for Private Testnet Configuration

As the Head of Block Production at [EOS New York](eosnewyork.io) I have been wondering about the best way to manage our BP nodes. One of the tools we have used in the past has been [Ansible](http://docs.ansible.com) so we figured we would see how well it works with EOS.IO software. Below are our instuctions on how to setup a testnet environment on GCE.

Assumptions:
1. You have sudo access on a Linux box.

## Procedure to create a testnet on GCE.

### Create the bios node 

1. Read some [Ansible documentation](http://docs.ansible.com/ansible/latest/scenario_guides/guide_gce.html)

1. Pull down the EOS New York repository for testing
```
cd ~
git clone https://github.com/eosnewyork/eosio
```
2. Create virtualenv for ansible
```
sudo mkdir /opt/ansible
virtualenv /opt/ansible
source /opt/ansible/bin/ansible
pip install ansible
```

3. Run the ansible command to create the bios node.
```
ansible-playbook playbooks/testnet.yaml -i inventory/testnet.yaml --tags "bios" -e '{"service_account_email": "{YOUR_ACCT_EMAIL}", "credentials_file": "{YOUR_CRED_FILE}", "project_id": "{YOUR_PROJ_ID}"}' 
```

The output of the final command should look something like:

>TASK [start : verify node is producing] ********************************************************************************************>**ok: [35.190.176.229] => {
>    "msg": "'[u'\"'\"'2128500ms thread-0   producer_plugin.cpp:239       block_production_loo ] '\"'\"', u'\"'\"'eosio generated block c6b94a62... #2550 @ 2018-04-25T09:35:28.500 with 0 trxs, lib: 2549'\"'\"', u'\"'\"'2129000ms thread-0   producer_plugin.cpp:239
> block_production_loo ] '\"'\"', u'\"'\"'eosio generated block 21f74584... #2551 @ 2018-04-25T09:35:29.000 with 0 trxs, lib: 2550'\"'\"', u'\"'\"'2129500ms thread-0   producer_plugin.cpp:239       block_production_loo ] '\"'\"', u'\"'\"'eosio generated block 5b66ffbb... #2552 @ 2018-04-25T09:35:29.500 with 0 trxs, lib: 2551'\"'\"', u'\"'\"'2130000ms thread-0   producer_plugin.cpp:239       block_production_loo ] '\"'\"', u'\"'\"'eosio generated block 47a906ff... #2553 @ 2018-04-25T09:35:30.000 with 0 trxs, lib: 2552'\"'\"', u'\"'\"'2130500ms thread-0   producer_plugin.cpp:239       block_production_loo ] '\"'\"', u'\"'\"'eosio generated block 155c2349... #2554 @ 2018-04-25T09:35:30.500 with 0 trxs, lib: 2553'\"'\"', u'\"'\"'2131000ms thread-0   producer_plugin.cpp:239       block_production_loo ] '\"'\"', u'\"'\"'eosio generated block 3cbcd615... #2555 @ 2018-04-25T09:35:31.000 with 0 trxs, lib: 2554'\"'\"', u'\"'\"'2131500ms thread-0   producer_plugin.cpp:239       block_production_loo ] '\"'\"', u'\"'\"'eosio generated block 41a08f61... #2556 @ 2018-04-25T09:35:31.500 with 0 trxs, lib: 2555'\"'\"', u'\"'\"'2132000ms thread-0   producer_plugin.cpp:239       block_production_loo ] '\"'\"', u'\"'\"'eosio generated block 9b9b9cf9... #2557 @ 2018-04-25T09:35:32.000 with 0 trxs, lib: 2556'\"'\"', u'\"'\"'2132500ms thread-0
>   producer_plugin.cpp:239       block_production_loo ] '\"'\"', u'\"'\"'eosio generated block 425dec70... #2558 @ 2018-04-25T09:35:32.500 with 0 trxs, lib: 2557'\"'\"', u'\"'\"'2133001ms thread-0   producer_plugin.cpp:239       block_production_loo ] '\"'\"', u'\"'\"'eosio generated block 931e8757... #2559 @ 2018-04-25T09:35:33.000 with 0 trxs, lib: 2558'\"'\"']'"
>   }

>PLAY RECAP ***************************************************************************************************************************
>xx.xxx.xxx.xxx             : ok=16   changed=1    unreachable=0    failed=0
>localhost                  : ok=3    changed=1    unreachable=0    failed=0



### MORE TO COME