import argparse
from eospy.cleos import Cleos
import time
import os
import datetime as dt

# args
parser = argparse.ArgumentParser(description='Claim rewards')
parser.add_argument('--url', '-u', type=str, action='store', default='https://api.eosnewyork.io', dest='url')
parser.add_argument('--file', '-f', type=str, action='store', default='./account_cpu_net.csv', dest='outfile')
args = parser.parse_args()

# connect up
ce = Cleos(args.url)

header = 'datetime,virtual_block_cpu_limit,virtual_block_net_limit,block_cpu_limit,block_net_limit\n'
if not os.path.isfile(args.outfile) :
    with open(args.outfile, 'w') as out :
        out.write(header)

#{
#    "server_version": "0f6695cb",
#    "chain_id": "aca376f206b8fc25a6ed44dbdc66547c36c6c33e3a119ffbeaef943642f0e906",
#    "head_block_num": 20949509,
#    "last_irreversible_block_num": 20949179,
#    "last_irreversible_block_id": "013fa8bb967bdaad9fa07839f4123ca5d82d976a9951f4837370f26453a1b43c",
#    "head_block_id": "013faa053b20b0e0e6f142b93a9d256cb44abe6f4e7a051f87fc6071812e1d6d",
#    "head_block_time": "2018-10-11T00:46:02.500",
#    "head_block_producer": "eosflytomars",
#    "virtual_block_cpu_limit": 200000000,
#    "virtual_block_net_limit": 1048576000,
#    "block_cpu_limit": 172486,
#    "block_net_limit": 1042584,
#    "server_version_string": "v1.3.0"
#}

while(True) :
    info = ce.get_info()
    line = '{},{},{},{},{}\n'.format(dt.datetime.now(),
                                              info['virtual_block_cpu_limit'],
                                              info['virtual_block_net_limit'],
                                              info['block_cpu_limit'],
                                              info['block_net_limit'])
    with open(args.outfile, 'a') as out :
        out.write(line)
    time.sleep(5)