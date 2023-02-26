// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;


// Super simple contract that allows signing a IPFS url.
// Assumption to verify is whether the signing done at the time of the transaction is enoughhere.
contract SimpleDocument {
    
    mapping (address => string) public userToDocMapping;
    uint32 size = 0;

function addSignature(string memory file_pointer) external {
        userToDocMapping[msg.sender] = file_pointer;
        size++;
    }

    function countSignatures() view external returns ( uint32 ) {
        return size;
    }

}