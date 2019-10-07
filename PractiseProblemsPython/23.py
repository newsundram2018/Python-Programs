'''
Created on Sep 29, 2019

Write a python function to find out whether a number is divisible by the sum of its digits. If so return True,else return False.
Sample Input    Expected Output
42    True
66    False

@author: Anonymous
'''
#PF-Prac-23
def divisible_by_sum(number):
    #start writing your code here
    x=str(number)
    sum=0
    for i in x:
        sum+=int(i)
    if number%sum==0:
        return True
    return False
    
number=63
print(divisible_by_sum(number))