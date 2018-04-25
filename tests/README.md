# Using Ansible for Private Testnet Configuration

As the Head of Block Production at [EOS New York](eosnewyork.io) I have been wondering about the best way to manage our BP nodes. One of the tools we have used in the past has been [Ansible](http://docs.ansible.com) so we figured we would see how well it works with EOS.IO software. Below are our instuctions on how to setup a testnet environment on GCE.

Assumptions:
1. You have sudo access on a Linux box.

##Procedure to create a testnet on GCE.

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


```
ansible-playbook playbooks/testnet.yaml -i inventory/testnet.yaml -e '{"service_account_email": "{YOUR_ACCT_EMAIL}", "credentials_file": "{YOUR_CRED_FILE}", "project_id": "{YOUR_PROJ_ID}"}'
```
