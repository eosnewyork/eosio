#!/usr/bin/env python

import argparse
from eospy.cleos import Cleos
import time

# constants
seconds_in_hour = 3600
seconds_in_day = 24 * seconds_in_hour

# args
parser = argparse.ArgumentParser(description='Claim rewards')
parser.add_argument('--url', '-u', type=str, action='store', default='https://api.eosnewyork.io', dest='url')
parser.add_argument('--account','-a', type=str, action='store', required=True, dest='account')
parser.add_argument('--claim-permission','-p', type=str, action='store', required=True, dest='permission')
parser.add_argument('--key-claim','-k', type=str, action='store', default='claim', dest='key_claim')
args = parser.parse_args()

# claim rewards
ce = Cleos(args.url)
print(ce.get_info())

# get info on producer
prod_info = ce.get_producers(lower_bound=args.account, limit=1)['rows'][0]
# check last time
now = time.time()
# last_claim_time == microseconds so need them in seconds
time_diff = now - int(prod_info['last_claim_time'])/1000/1000
seconds_left = seconds_in_day - time_diff
# create claim transaction
data = ce.abi_json_to_bin('eosio', 'claimrewards',{'owner':args.account})
trx = {"actions":
    [{
        "account":'eosio',
        "name":"claimrewards",
        "authorization":[
            {
                "actor":args.account,
                "permission": args.permission
            }],
        "data":data['binargs']}
    ]}
print(trx)
# 
while(True) :
    if time_diff > seconds_in_day :
        print('Claiming')
        resp = ce.push_transaction(trx, args.key_claim)
        print(resp)
        # wait for the trx to clear
        time.sleep(30)
    else :
        # fake claim     
        print('{} seconds left until claim. Sleeping for a bit.'.format(seconds_left))
        if seconds_left > seconds_in_hour * 18 :
            sleep_time = seconds_in_hour * 18
        elif seconds_left > seconds_in_hour * 12 :
            sleep_time = seconds_in_hour * 12
        elif seconds_left > seconds_in_hour * 6 :
            sleep_time = seconds_in_hour * 6
        elif seconds_left > seconds_in_hour * 3 :
            sleep_time = seconds_in_hour * 3
        else :
            sleep_time = seconds_left
        # sleep
        print('Sleeping {} seconds'.format(sleep_time))
        time.sleep(sleep_time)    
