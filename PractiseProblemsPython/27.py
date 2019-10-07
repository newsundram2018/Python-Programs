'''
Created on Sep 29, 2019
Given 2 positive integers, write a python function to return True if one of them is 10 or if their sum is 10, else return False.
Sample Input    Expected Output
10,9    True
2,8    True
2,9    False
@author: Anonymous
'''
#PF-Prac-27
def check_for_ten(num1,num2):
    #start writing your code here
    if num1==10 or num2==10:
        return True
    elif(num1+num2==10):
        return True
    return False
    
print(check_for_ten(10,9))