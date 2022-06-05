from web3.geth import GethMiner

from web3 import Web3
import json

config = json.load(open("../config.json"))

option = input("Что вы хотите сделать (start, stop) => ")

w3 = Web3(Web3.HTTPProvider(f'http://{config["node3"]["ip"]}:{config["node3"]["port"]}'))
w3.eth.default_account = w3.eth.accounts[0]
if not w3.isConnected():
    exit()
print(w3.eth.accounts)
miner = GethMiner(w3)

if option == "start":
    print(miner.start(1))
if option == "stop":
    print(miner.stop())