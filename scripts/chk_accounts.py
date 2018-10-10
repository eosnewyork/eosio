#!/usr/bin/env python

import argparse
from eospy.cleos import Cleos
import time
import os
import datetime as dt

# args
parser = argparse.ArgumentParser(description='Claim rewards')
parser.add_argument('--url', '-u', type=str, action='store', default='https://api.eosnewyork.io', dest='url')
parser.add_argument('--file', '-f', type=str, action='store', default='./account_cpu_net.csv', dest='outfile')
parser.add_argument('--accounts','-a', nargs='+', action='store', required=True, dest='accounts')
args = parser.parse_args()

# connect up
ce = Cleos(args.url)

header = 'account_name,cpu_used,cpu_avail,cpu_total,net_used,net_avail,net_total\n'
if not os.path.isfile(args.outfile) :
    with open(args.outfile, 'w') as out :
        out.write(header)

while(True) :
    for act in args.accounts :
        info = ce.get_account(act)
        cpu = info['cpu_limit']
        net = info['net_limit']
        line = '{},{},{},{},{},{},{},{}\n'.format(print(dt.datetime.now()),act, cpu['used'], cpu['available'], cpu['max'], net['used'], net['available'], net['max'])
        with open(args.outfile, 'a') as out :
            out.write(line)
    time.sleep(60)