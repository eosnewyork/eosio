
# Scripts 

## Python Scripts 
### Environment setup

#### Linux
```
# create virtual environment
mkdir -p ~/envs/eospy
virtualenv ~/envs/eospy
# activate the environment
source ~/envs/eospy/bin/activate
# install the library
pip install git+https://github.com/eosnewyork/eospy
```

#### Windows

1. Install python
You can use either Python 2.7 or 3.7 however we suggest python 3.7 as we have tested that version more thoroughly.
https://www.howtogeek.com/197947/how-to-install-python-on-windows/
[Python 2.7](https://www.python.org/downloads/release/python-2715/)
[Python 3.7](https://www.python.org/downloads/release/python-370/)

2. Install git
https://www.atlassian.com/git/tutorials/install-git

3. Install eospy
```
pip install git+https://github.com/eosnewyork/eospy
```

### `chk_rewards.py`

Get the rewards information about an account

Example
```
./chk_rewards.py --account eosnewyorkio
```

## bash scripts

### `json_to_producerjson.sh`

Convert bp.json url to [producerjson smart contract](https://github.com/greymass/producerjson)

Example
```
./json_to_producerjson.sh https://bp.eosnewyork.io/bp.json
--2018-07-28 11:12:28--  https://bp.eosnewyork.io/bp.json
Resolving bp.eosnewyork.io (bp.eosnewyork.io)... 143.204.142.73, 143.204.142.89, 143.204.142.17, ...
Connecting to bp.eosnewyork.io (bp.eosnewyork.io)|143.204.142.73|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1571 (1.5K) [application/json]
Saving to: ‘/tmp/1532790748_bp.json’

100%[============================================================================================>] 1,571       --.-K/s   in 0s

2018-07-28 11:12:28 (147 MB/s) - ‘/tmp/1532790748_bp.json’ saved [1571/1571]

Creating command for "eosnewyorkio"
===============================
cleos push action producerjson set '{"owner":"eosnewyorkio","json": "{\"producer_account_name\":\"eosnewyorkio\",\"producer_public_key\":\"EOS6GVX8eUqC1gN1293B3ivCNbifbr1BT6gzTFaQBXzWH9QNKVM4X\",\"org\":{\"candidate_name\":\"EOSNewYork\",\"website\":\"https://www.eosnewyork.io\",\"code_of_conduct\":\"https://steemit.com/eos/@eosnewyork/eos-new-york-code-of-conduct\",\"ownership_disclosure\":\"https://steemit.com/eos/@eosnewyork/eos-new-york-ownership-disclosure-and-corporate-structure\",\"email\":\"community@eosnewyork.io\",\"branding\":{\"logo_256\":\"https://bp.eosnewyork.io/Logo_256.jpg\",\"logo_1024\":\"https://bp.eosnewyork.io/Logo_1024.jpg\",\"logo_svg\":\"https://bp.eosnewyork.io/eosnewyorkio.svg\"},\"location\":{\"name\":\"CookIslands\",\"country\":\"CK\",\"latitude\":-18.857952,\"longitude\":-159.785278},\"social\":{\"steemit\":\"eosnewyork\",\"twitter\":\"eosnewyork\",\"youtube\":\"UCg7aeCSXUTP49w_elxgYIXA\",\"facebook\":\"eosnewyorkBP\",\"github\":\"eosnewyork\",\"reddit\":\"eosnewyork\",\"keybase\":\"d3ck\",\"telegram\":\"eosnewyorkchat\",\"wechat\":\"kevineosnewyork\"}},\"nodes\":[{\"location\":{\"name\":\"primary\",\"country\":\"BR\",\"latitude\":-23.5505,\"longitude\":-46.6333},\"is_producer\":true,\"node_type\":\"producer\",\"p2p_endpoint\":\"node1.eosnewyork.io:6987\",\"api_endpoint\":\"http://api.eosnewyork.io\",\"ssl_endpoint\":\"https://api.eosnewyork.io\"}]}"}' -p "eosnewyorkio"@active

# make sure to unlock your wallet, copy everything under "===============================", and run

```