#!/bin/sh
set -e

if [ ! `which jq` ]; then
  echo "Please install jq"
  exit 1
fi

if [ -z "$1" ]; then
  echo "Please pass the URL for your bp.json"
  exit 1
fi

url=$1

bp_file=/tmp/`date '+%s'`_bp.json
# get the bp.json and compact it
wget --quiet -O - "$url" | jq -M -c '.' >$bp_file

# get producer name
prod_name=`cat $bp_file | jq '.producer_account_name'`
# escape quotes
sed -i 's/"/\\"/g' $bp_file

echo "Creating command for $prod_name"
echo "==============================="
echo "cleos push action producerjson set '{\"owner\":$prod_name,\"json\": \"`cat $bp_file`\"}' -p $prod_name@active"

rm $bp_file
