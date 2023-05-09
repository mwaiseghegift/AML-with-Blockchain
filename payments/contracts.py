contract_path = "Anti-Money-Laundering.sol"

with open(contract_path, 'r') as file:
  contract_file = file.read()


from solcx import compile_standard

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {
            "Anti-Money-Laundering.sol": {
                "content": contract_file
            }
        },
        "settings":
            {
                "outputSelection": {
                    "*": {
                        "*": [
                            "abi",
                            "metadata",
                            "evm.bytecode",
                            "evm.bytecode.sourceMap"
                        ]
                    }
                }
            }
    },
    solc_version="0.8.0"
)

import json

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

ANTI_MONEY_LAUNDERING_ABI = compiled_sol['contracts']['Anti-Money-Laundering.sol']['AntiMoneyLaundering']['abi']
ANTI_MONEY_LAUNDERING_BYTECODE = compiled_sol['contracts']['Anti-Money-Laundering.sol']['AntiMoneyLaundering']['evm']['bytecode']['object']
