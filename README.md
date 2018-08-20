# deploying smart contract on eth blockchain using infura and metamask

## setting up web3

setting up is pretty simple, just run

$ pip install --upgrade pip

$ python3.5 -m venv venv
$ . venv/bin/activate 


$ pip install web3

in order to leave the *venv*

$ deactivate


## creating infura node

make an account and create a project
should provide with API key and links as shown below:

**testnet:**

'https://ropsten.infura.io/v3/YOUR-API-KEY'

'https://kovan.infura.io/v3/YOUR-API-KEY'

'https://rinkeby.infura.io/v3/YOUR-API-KEY'

**mainnet:**

'https://mainnet.infura.io/v3/YOUR-API-KEY'

## connection mainnet via infura

if you want to connect to infura node using auto function on Web3py

$ export INFURA_API_KEY=YOUR-API-KEY

$ printenv INFURA_API_KEY

$ python3.5

$ >>> from web3.auto.infura import w3

$ >>> w3.isConnected()
$ True

##   deploy via infura

special thanks to this url below:

https://ethereum.stackexchange.com/questions/44614/how-to-connect-to-infura-and-deploy-contract-use-web3-py

from reverse engineering the codes shown above, i was able to come up with the python script where you can deply using remote wallet such as metamask
