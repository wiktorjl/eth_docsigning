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


# Connect to network
w3 = Web3(Web3.HTTPProvider(
    'https://goerli.infura.io/v3/' + app_key))

if w3.isConnected():
    print("Connection Successful")
else:
    print("Connection Failed")


# Get address of the smart contract deployed in previous step and chain id
smart_contract_address = w3.toChecksumAddress(
    '0x4d849cf3845750cbcc0a93ecfb3f886a98b96335')
chain_id = w3.eth.chain_id

# Get nonce
nonce = w3.eth.getTransactionCount(caller)

# Create contract
account = w3.eth.account.privateKeyToAccount(private_key)
contract = w3.eth.contract(address=smart_contract_address, abi=abi)

# Get the count of signatures before adding one
sig_count = contract.functions.countSignatures().call()
print("Count of signatures: " + str(sig_count))

# Add a new signature
call_function = contract.functions.addSignature("address_of_a_document").buildTransaction(
    {"chainId": chain_id, "from": caller, "nonce": nonce})
signed_tx = w3.eth.account.sign_transaction(
    call_function, private_key=private_key)
send_tx = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(send_tx)
print(tx_receipt)


# Get the count of signatures before adding one
sig_count = contract.functions.countSignatures().call()
print("Count of signatures: " + str(sig_count))
