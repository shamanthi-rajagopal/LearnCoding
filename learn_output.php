<?php
//Shamanthi Rajagopal
//PHP file for me to learn and do exercises
//phpinfo();
?>

<?php //PHP tag => all PHP goes in the tag | html code can come after the tags

// echo - Output Strings, numbers, html, etc. (html should be outside php tag)
echo 'hello';
echo '<p> :O </p>'; 
echo '<p> </p>'; //spaces for the web server locally hosted to test php code

//print - single argument
print 123;
echo '<p> </p>'; 
print ('Shamanthi is soooo funny');
echo '<p> </p>'; 

//print_r() - print single values/arrays (echo cannot)
print_r([1,2,3]);
echo '<p> </p>'; 

//var_dump() - prints and returns data type and length
var_dump('Hello');
echo '<p> </p>'; 
var_dump(true);
echo '<p> </p>'; 

//var_export() - similar to var_dump but outputs a string representation of a variable
var_export('Hello');

?>

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Shamanthi's Document</title>
    </head>
    <body>
        <h1><?php echo 'This is written in PHP, within HTML code';?></h1>
        <h1><?='PHP is cool :p';?></h1>
    </body>
</html>