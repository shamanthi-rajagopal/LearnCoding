<?php
//Shamanthi Rajagopal
//PHP file for me to learn and do exercises
// variables & datatypes
?>

<?php 
//Created by Shamanthi Rajagopal

                /* PHP DATA TYPES*/ 
/*
Strings - Series of characters, with quotes
Integers - Whole numbers
Floats - Decimal Numbers
Boolean - true/false
Arrays - Special variable that can whole more than one value
Object - Related to classes
NULL - Empty variable
Resources - Special variable that holds a resource
*/

                /* Variable Rules*/
/*
- Variables must start with '$'
- Must also start with a letter or underscore (not a number)
- Case sensitive
*/

$name = 'Shamanthi'; // string
$age = 18; // int
$in_uni = true; //if true shows 1 else it shows nothing (even if false)
$bank_balance = 10.01; // float

echo $name;
echo '<p> </p>';
var_dump($in_uni);
echo '<p> </p>';

echo $name.' is '.$age.' years old.'; // concatenation
echo" $name has $$bank_balance."; // easier to do with double quotes
echo '<p> </p>';

//Math operations
echo 5+5;
echo '5'+'5';
echo '<p> </p>';
echo 10 - 8;
echo '<p> </p>';
echo 9*1;
echo '<p> </p>';
echo 100/10;
echo '<p> </p>';
echo 10%3;
echo '<p> </p>';

//Constants => never going to change
define('HOST','localhost');
define('DB_NAME','dev_DB');

echo HOST;
?>