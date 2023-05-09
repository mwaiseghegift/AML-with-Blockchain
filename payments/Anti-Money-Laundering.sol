// Anti-Money Laundering Smart Contract
// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract AntiMoneyLaundering {
    address public admin;
    uint public threshold;
    mapping(address => uint) public balances;

    constructor() {
        admin = msg.sender;
        threshold = 100 ether;
    }

    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw(uint amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance.");
        balances[msg.sender] -= amount;
       payable( msg.sender).transfer(amount);
    }

    function transfer(address to, uint amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance.");
        require(balances[to] + amount >= balances[to], "Overflow error.");
        balances[msg.sender] -= amount;
        balances[to] += amount;
        
        if (balances[msg.sender] >= threshold) {
            // Log a suspicious transaction
            emit SuspiciousTransaction(msg.sender, to, amount);
        }
    }

    event SuspiciousTransaction(address from, address to, uint amount);
}
