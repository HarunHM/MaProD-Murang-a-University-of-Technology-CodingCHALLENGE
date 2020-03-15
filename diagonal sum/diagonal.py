filter_none
edit
play_arrow

brightness_4
# Python3 program to find the difference 
# between the sum of diagonal. 
def difference(arr, n): 
  
    # Initialize sums of diagonals 
    d1 = 0
    d2 = 0
  
    for i in range(0, n): 
        d1 = d1 + arr[i][i] 
        d2 = d2 + arr[i][n - i - 1] 
          
    # Absolute difference of the sums 
    # across the diagonals 
    return abs(d1 - d2) 
  
# Driver Code 
n = 3
  
arr = [[11, 2, 4], 
       [4 , 5, 6], 
       [10, 8, -12]] 
  
print(difference(arr, n)) 
      