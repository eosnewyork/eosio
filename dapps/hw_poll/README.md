
This is the first stab at a hello world contract based on a *very* alpha DAWN 3.0

Description:  This contract is the very early stages of being an "Hello World" polling constract

Assumptions:  It is assumed that you have an understanding of EOS and the build mechanism found here:
https://github.com/EOSIO/eos#runanode

*NOTE* In no way is this an endorsement of using the same key for multiple accounts

1. Once the single testnet is up and running create a set of keys that will be used throughout this tutorial
```
> eosioc create key
Private key: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Public key: EOSxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

2. Ensure the wallet application is running in the background and logging information
```
# change the port number as it will conflict with the eosiod default port of 8888
> eosiowd --http-server-address 127.0.0.1:8886 &> ~/wallet.log &

```

3. Import the private key into your wallet
```
> eosioc --wallet-port 8886 import xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

```

4. Load up the eosio.system contract so you can create a user
```
> eosioc --wallet-port 8886 set contract eosio \
         ~/eos/build/contracts/eosio.system/eosio.system.wast \
         ~/eos/build/contracts/eosio.system/eosio.system.abi
```

5. Create two accounts inita and hw.poll for the contract.  Replace EOSxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx with
public key from step 1.
```
> eosioc --wallet-port 8886 -p 8887 create account eosio inita \
  EOSxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx EOSxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

> eosioc --wallet-port 8886 -p 8887 create account eosio hw.poll \
  EOSxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx EOSxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

```

6. Compile the contract and load the contract.
```
# your location of the hw_poll files may differ
> eosiocpp -o ~/eosnewyork/eosio/dapps/hw_poll/hw_poll.wast ~/eosnewyork/eosio/dapps/hw_poll/hw_poll.cpp
> eosioc --wallet-port 8886 set contract hw.poll \
  ~/eosnewyork/eosio/dapps/hw_poll/hw_poll.wast \
  ~/eosnewyork/eosio/dapps/hw_poll/hw_poll.abi \
  --permission hw.poll@active
```

7. Push a simple transaction
```
> eosioc --wallet-port 8886 -p 8887 push action hw.poll create '{ "creator" : "inita" , "question" : "Who am I today"}'
```

8. Enjoy.