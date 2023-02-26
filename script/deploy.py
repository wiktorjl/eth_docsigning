from web3 import Web3
import json
from dotenv import load_dotenv
import os


load_dotenv()
private_key = os.getenv("PRIVATE_KEY")
app_key = os.getenv("INFURA_APP_KEY")
caller = os.getenv("YOUR_ADDRESS")

# Read contract spec
with open('contract_output/contracts_SimpleDocument_sol_SimpleDocument.abi', 'r') as f:
    abi = json.loads(f.read())

# Read the contract itsekf
with open('contract_output/contracts_SimpleDocument_sol_SimpleDocument.bin', 'r') as f:
    bytecode = f.read()


# Connect to network
w3 = Web3(Web3.HTTPProvider("https://goerli.infura.io/v3/" + app_key))

# Create contract
account = w3.eth.account.privateKeyToAccount(private_key)
contract = w3.eth.contract(abi=abi, bytecode=bytecode)

# Build tx to create a new address
construct_txn = contract.constructor().buildTransaction({
    'from': account.address,
    'nonce': w3.eth.getTransactionCount(account.address),
    'gas': 1500000
})

# Sign and send
signed = account.signTransaction(construct_txn)
tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
print("Fetch new contract address from here: " + tx_hash.hex())
