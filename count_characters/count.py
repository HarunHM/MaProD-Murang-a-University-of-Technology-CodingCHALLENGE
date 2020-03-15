"""
Define a string.
Define and initialize a variable count to 0.
Iterate through the string till the end and for each character except spaces, increment the count by 1.
To avoid counting the spaces check the condition i.e. string[i] != ' '.
"""

string = "Mathematics and Programming";  
count = 0;  
   
#Counts each character except space  
for i in range(0, len(string)):  
    if(string[i] != ' '):  
        count = count + 1;  
   
#Displays the total number of characters present in the given string  
print("Total number of characters in a string: " + str(count));  