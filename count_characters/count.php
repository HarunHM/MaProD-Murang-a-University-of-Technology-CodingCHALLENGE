<!DOCTYPE html>  
<html>  
<body>  
<?php  
$string = "The best of both worlds";  
$count = 0;  
   
//Counts each character except space  
for($i = 0; $i < strlen($string); $i++) {  
    if($string[$i] != ' ')  
        $count++;  
}  
   
//Displays the total number of characters present in the given string  
print("Total number of characters in a string: " . $count);  
?>  
</body>  
</html>  