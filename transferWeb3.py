# Author : Phyo T Htut
# Mentor : Andrew Lee

from web3 import Web3

provider = 'https://ropsten.infura.io/4c222980c7ef4e6e9b7f28103b924456'
w3 = Web3(Web3.HTTPProvider(provider))

# eKey is the from wallet, and should be prompt with input()
eKey = input("User's Wallet: ")
# public key must be checked in the db by using w3.toChecksumAddress
eKey = w3.toChecksumAddress(eKey)

# dKey us the private key of the sender
dKey = input('Private Key: ')

if dKey[0:2] != '0x':
    dKey = '0x' + dKey
    
target = input('Target: ')
target = w3.toChecksumAddress(target)

val = float(input('How much ETH: '))
val = int(val * 10 ** 8)

transaction = {
            'to': target,
            'from': eKey, # Only 'from' address, don't insert 'to' address
            'value': val * 10 ** 10, # Add how many ethers you'll transfer during the deploy
            'gas': 2000000, # Trying to make it dynamic ..
            'gasPrice': w3.eth.gasPrice, # Get Gas Price
            'nonce': w3.eth.getTransactionCount(eKey), # Get Nonce
            } 

signed = w3.eth.account.signTransaction(transaction, dKey)
tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
print(tx_hash.hex())
