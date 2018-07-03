
# Scripts 

## Environment setup

### Linux
```
# create virtual environment
mkdir -p ~/envs/eospy
virtualenv ~/envs/eospy
# activate the environment
source ~/envs/eospy/bin/activate
# install the library
pip install git+https://github.com/eosnewyork/eospy
```

### Windows

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

## `get_rewards.py`

Get the rewards information about an account

Example
```
./get_rewards.py --account eosnewyorkio
```