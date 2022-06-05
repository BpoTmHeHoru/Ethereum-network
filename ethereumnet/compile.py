import solcx
import json

config = json.load(open("../config.json"))

solcx.install_solc("0.8.10")

contract = solcx.compile_files(
    "./contract.sol",
    output_values=["abi", "bin"],
    optimize=True,
    optimize_runs=200,
    solc_version="0.8.10"
)
config["contract"]["abi"] = contract[f'{list(contract.keys())[0]}']['abi']
config["contract"]["bytecode"] = contract[f'{list(contract.keys())[0]}']['bin']

json.dump(config, open("../config.json", "w"), indent=4)
