#!/usr/bin/env python

from eospy.cleos import Cleos
import argparse

parser = argparse.ArgumentParser(description='Command Line Interface to EOSIO via python')
parser.add_argument('--api-version','-v', type=str, default='v1', action='store', dest='api_version')
parser.add_argument('--url', '-u', type=str, action='store', default='https://api.eosnewyork.io', dest='url')
parser.add_argument('--account','-a', type=str, action='store', required=True, dest='account')
parser.add_argument('--pos', type=int, action='store', default=-1, dest='pos')
parser.add_argument('--offset', type=int, action='store', default=-1000000, dest='offset')
args = parser.parse_args()

# get information
ce = Cleos(url=args.url, version=args.api_version)
#print(ce.get_info())
print('block_time,from,quantity')
actions = ce.get_actions(args.account, args.pos, args.offset)
for act in actions['actions']:
    if act['action_trace']['act']['name'] == 'transfer' and act['action_trace']['act']['account'] == 'eosio.token':
        if act['action_trace']['act']['data']['from'] == 'eosio.vpay' or act['action_trace']['act']['data']['from'] == 'eosio.bpay' :
            print(act['block_time'] + ',' + act['action_trace']['act']['data']['from'] + ',' +act['action_trace']['act']['data']['quantity'])
            
