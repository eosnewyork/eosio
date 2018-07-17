#!/usr/bin/env python

from eospy import cleos
import argparse
import time

parser = argparse.ArgumentParser(description='check the value of the last claim is less than 24 hours ago')
parser.add_argument('--api-version','-v', type=str, default='v1', action='store', dest='api_version')
parser.add_argument('--url', '-u', type=str, action='store', default='https://api.eosnewyork.io', dest='url')
parser.add_argument('--account', '-a', type=str, action='store', required=True, dest='acct')
args = parser.parse_args()

ce = cleos.Cleos(url=args.url, version=args.api_version)

print(ce.get_info())
# get list of producers
producers = ce.get_producers()

for prod in producers['rows'] :
    if prod['owner'] == args.acct :
        t = time.time()
        last_claim_secs = int(prod['last_claim_time'])/1000/1000
        time_diff = t - last_claim_secs
        seconds_in_day = 24*3600
        if time_diff > seconds_in_day :
            print('Last claim is > than a day')
            exit(2)
        exit(0)

exit(1)
