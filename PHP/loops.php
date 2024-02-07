<?php
//Created by Shamanthi Rajagopal
//Loops

//For Loop
for($x=0; $x<= 10; $x++){
echo $x; // loop through 0 to 10 and prints the numbers side by side
}
echo'<p></p>';

//While Loop
$x = 1;

while($x<=15){
  echo 'Number '.$x.'<br>';
  $x++;
}

echo'<p></p>';

//Foreach Loop

//Method 1 => For Loop
$posts = ['First Post','Second Post','Third Post'];

for($x = 0; $x< count($posts); $x++){
  echo $posts[$x];
}

echo'<p></p>';

//Method 2 => Foreach Loop
foreach($posts as $post){
  echo $post;
}

echo'<p></p>';
?>