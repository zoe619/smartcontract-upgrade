// SPDX-License-Identifier:MIT

pragma solidity ^0.8.0;


contract Box{
   
   uint256 private value;

   event ValueChanged(uint256 newValue);

   function storeValue(uint256 newValue) public{
       value = newValue;
       emit ValueChanged(newValue);

   }

   function returnValue() public view returns(uint256){
       return value;
   }
}