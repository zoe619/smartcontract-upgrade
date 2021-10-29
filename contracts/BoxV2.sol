// SPDX-License-Identifier:MIT

pragma solidity ^0.8.0;


contract BoxV2{
   
   uint256 private value;

   event ValueChanged(uint256 newValue);

   function storeValue(uint256 newValue) public{
       value = newValue;
       emit ValueChanged(newValue);

   }

   function returnValue() public view returns(uint256){
       return value;
   }

//   we will call increment on same address that we deployed Box.sol to
// We shouldn't be able to call increment on Box.sol but we should be able to call it on Box2.sol
   function increment() public{
       value = value + 1;
       emit ValueChanged(value);
   }
}