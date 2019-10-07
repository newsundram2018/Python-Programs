'''
Created on Sep 29, 2019
Description:
Write a python function to print the given number of diagonal lines of stars.
Sample input: 5

Expected output:
*
.*
..*
...*
....*
Note: Setting the end parameter of the print function to empty string prevents the issuing of the new line.
Example: print(".",end="") will maintain the cursor in the same line after displaying "."



@author: Anonymous
'''
#PF-Tryout
def diagonal_stars(number):
   #start writing your code here
   for i in range(number):
       print("."*i+"*")

number=6    
diagonal_stars(number)