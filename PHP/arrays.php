<?php
//Created by Shamanthi Rajagopal

//Simple Array

$numbers = [1,22,333,4444];

$fruits =array('apple','banana','blueberry');

print_r($fruits);
echo '<p></p>'; 

echo $fruits[2];
echo '<p></p>'; 

//Arrays seen in DBs
$person = [
  
  [
  'firstname' => 'Shamanthi',
  'lastname' => 'Rajagopal',
  'age' => '18'
  ],
  
  [
  'firstname' => 'Stephen',
  'lastname' => 'Curry',
  'age' => '30'
  ]

];

echo $person [1] ['firstname'];
?>