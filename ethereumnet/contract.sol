//SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.10;
pragma abicoder v2;




contract main  {
    enum Role { guets, user, admin}

    struct user {
        string Name;
        
        string Pass;
        Role   Roles;
    }

    struct  nft {
        uint256 TokenID;
        address _Owner;
        uint16 Amount;
        uint16 Data;
    }


    mapping (address => user) users;
    mapping (address => nft) YourCookie;

    nft[] Cookie;

    function reg(string memory _Name, string memory _Pass) public {
        users[msg.sender] = user(_Name, _Pass, Role.user);
    }

    function auth(string memory _Pass) public view returns(user memory) {
        require(keccak256(bytes(_Pass)) == keccak256(bytes(users[msg.sender].Pass)));
        return users[msg.sender];
        
    }



































}