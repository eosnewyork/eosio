
# Snapshots

Scripts that takes a file containing a list of accounts and generates a csv file in the format:

`<account creation time>, <account name>, <total EOS owned>`

The files are uploaded to https://www.eossnapshots.io 

## Python script

1. Install `eospy` following these [instructions](https://github.com/eosnewyork/eospy#installation)
2. Run the script.
```
# --acct-file: file containing account list
# --out-file: output csv file
# --time: max creation time of the accounts. Timestamp is in the format YYYY-MM-DDHH:mm
snapshot_creator.py --acct-file /tmp/acct_snapshot.txt --out-file /tmp/20180728.csv --time 2018-07-2900:00
```

## C# script

Please see this [repo](https://github.com/eosnewyork/EOSAccountInfo)