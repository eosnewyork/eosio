** A Work in Progress **

# Using Ansible for Private Testnet Configuration

As the Head of Block Production at [EOS New York](eosnewyork.io) I have been wondering about the best way to manage our BP nodes. One of the tools we have used in the past has been [Ansible](http://docs.ansible.com) so we figured we would see how well it works with EOS.IO software. Below are our instuctions on how to setup a testnet environment on GCE.

Assumptions:
1. You have sudo access on a Linux box.

## Procedure to create a single node testnet on GCE using [eoscanada's bios process](https://github.com/eoscanada/eos-bios).

### Create the bios node 

1. Read some [Ansible documentation](http://docs.ansible.com/ansible/latest/scenario_guides/guide_gce.html)

1. Pull down the EOS New York repository for testing
```
cd ~
git clone https://github.com/eosnewyork/eosio
cd eosio/tests
```
2. Create virtualenv for ansible
```
sudo mkdir /opt/ansible
virtualenv /opt/ansible
source /opt/ansible/bin/ansible
pip install ansible apache-libcloud pycrypto
```

3. Run the ansible command to create the bios node.
```
ansible-playbook playbooks/testnet.yaml -K -i inventory/testnet.yaml --tags "bios" -e '{"service_account_email": "{YOUR_ACCT_EMAIL}", "credentials_file": "{YOUR_CRED_FILE}", "project_id": "{YOUR_PROJ_ID}"}' 
```

4. Login to the **eosme** node and run some commands
```
ssh bootnode_public_ip
sudo su eosio
cd /opt/eosio/eos-bios
./eos-bios boot
```

### MORE TO COME