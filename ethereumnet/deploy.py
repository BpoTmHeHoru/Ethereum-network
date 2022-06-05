
from web3 import Web3
import json

config = json.load(open("../config.json"))

option = input("Test => ")
w3 = Web3(Web3.HTTPProvider(f'http://{config["node1"]["ip"]}:{config["node1"]["port"]}'))
w3.eth.default_account = w3.eth.accounts[0]
w3.geth.personal.unlock_account(w3.eth.default_account, "123", 1)
contract = w3.eth.contract(abi=config["contract"]["abi"], bytecode=config["contract"]["bytecode"])
hash = contract.constructor().transact()
w3.geth.personal.lock_account(w3.eth.default_account)
receipt = w3.eth.wait_for_transaction_receipt(hash)

config["contract"]["address"] = receipt.contractAddress
print(receipt.contractAddress)
json.dump(config, open("../config.json", "w"), indent=4)

if option == "test":
    contract = w3.eth.contract(address=config["contract"]["address"], abi=config["contract"]["abi"])
    w3.geth.personal.unlock_account(w3.eth.default_account, "123", 1)
    res = contract.functions.Register("kelerus").transact()
    w3.geth.personal.lock_account(w3.eth.default_account)
    w3.eth.wait_for_transaction_receipt(res)
    res = contract.functions.Auth("kelerus").call()
    print(res)