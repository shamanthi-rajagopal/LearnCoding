<?php
//Created by Shamanthi Rajagopal
//Functions
//be careful with function scopes and use global variables only when needed
echo'<p></p>';

$y = 12; //global variable

function registerUser($email) { // Defining Function, has arguement
  $x = 10; //a variable in the function's scope
  echo 'User Registered';
  echo'<p></p>';
  echo $email.' registered';
}

registerUser('shamanthi2025@gmail.com'); // Declaring / calling the function
//has parameter
echo'<p></p>';

function sum($n1, $n2){ // can set default values as well without having to pass values in
  return $n1+$n2;
}

$sum = sum(1,2);
echo $sum;
echo'<p></p>';

$subtract = function($n1,$n2) {
  return $n1-$n2;
};

echo $subtract(20,12);

?>