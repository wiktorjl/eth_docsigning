#!/bin/sh
mkdir -p contract_output
solcjs --bin --abi  ./contracts/SimpleDocument.sol -o contract_output