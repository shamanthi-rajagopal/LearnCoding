<?php
//Created by Shamanthi Rajagopal
//Conditionals

//Same conditional symbols as other languages (<,>,=,etc)

$age = 20;

if ($age>=18){
echo 'You are an ADULT!';
} else {
echo 'You are a child :)';
}
echo '<p></p>';

$t = date("H"); //shows the hour of the current day

if($t<12){
  echo'Good Morning!';
}
else if ($t<17) {
  echo'Good Afternoon!';
} 
else {
  echo'Good Evening!';
}
echo '<p></p>';

//Method one - Writing else/if conditions

$posts = ['First Post']; //array with one element

if(!empty($posts)){ //empty functions check is empty
  echo $posts[0];
}

//Method 2 - with out if/else statements
$firstPost = !empty($posts) ? $posts[0]: 'No Posts';
echo $firstPost;
echo '<p></p>';

//Switches

$favColour = 'yellow';

switch($favColour){
  case 'blue':
    echo"Your favourite colour is blue!";
    break;
  case 'red':
    echo"Your favourite colour is blue!";
    break;
  case 'green':
    echo"Your favourite colour is blue!";
    break;
  default:
    echo"Your favourite colour is not one of the RGB colours :(";
}

?>