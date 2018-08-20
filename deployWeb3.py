# Author : Phyo T Htut
# Mentor : Andrew Lee

from web3 import Web3
from solc import compile_source

contract_source_code = '''
pragma solidity ^0.4.21;

contract Greeter {
    string public greeting;

    function Greeter() public {
        greeting = 'Hello';
    }

    function setGreeting(string _greeting) public {
        greeting = _greeting;
    }

    function greet() view public returns (string) {
        return greeting;
    }
}
'''

compiled_sol = compile_source(contract_source_code) # Compiled source code
contract_interface = compiled_sol['<stdin>:Greeter']

provider = 'https://ropsten.infura.io/YOUR-API-KEY'
w3 = Web3(Web3.HTTPProvider(provider))
abi = contract_interface['abi']
bin = contract_interface['bin']

# eKey is the from wallet, and should be prompt with input()
eKey = input("User's Wallet: ")
# public key must be checked in the db by using w3.toChecksumAddress
eKey = w3.toChecksumAddress(eKey)

# dKey us the private key of the sender
dKey = input('Private Key: ')

if dKey[0:2] != '0x':
    dKey = '0x' + dKey

instance = w3.eth.contract(abi=abi, bytecode=bin)

tx_data = instance.constructor().buildTransaction({
    'from': eKey,
    'nonce': w3.eth.getTransactionCount(eKey),
    'gas': 1728712,
    'gasPrice': w3.toWei('21', 'gwei')})

signed = w3.eth.account.signTransaction(tx_data, dKey)
tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
print(tx_hash.hex())

tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
greeter = w3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=contract_interface['abi'],
)

## if you want to try and call the functions, you may do the following
#greeter.functions.greet().call()   # you should see 'Hello'

'''
tx_data = greeter.functions.setGreeting('Ni Hao').buildTransaction({
    'from': eKey,
    'nonce':w3.eth.getTransactionCount(eKey),
    'gas': 1728712, 2000000
    'gasPrice': w3.toWei('21', 'gwei')})
signed = w3.eth.account.signTransaction(tx_data, dKey)
w3.eth.sendRawTransaction(signed.rawTransaction)


greeter.functions.greeter.call()    # you should see 'Ni Hao'

'''
