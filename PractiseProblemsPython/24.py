'''
Created on Sep 29, 2019
Discription:
    Given two positive integers. Write a python function to return the greatest common divisor of the given numbers.
Sample Input    Expected Output
14 and 35    7
800 and 2800    400
@author: Anonymous
'''
#PF-Prac-24
def find_gcd(num1,num2):
    #start writing your code here
    for i in range(-num2,0):
        if(num1%abs(i)==0 and num2%abs(i)==0):
            return abs(i)
        

num1=45
num2=9
print(find_gcd(num1,num2))