'''
Created on Sep 30, 2019

@author: Anonymous
'''
#PF-Prac-32
def check_squares(number):
    #start writing your code here
    for i in range(1,100):
        for j in range(1,100):
            if i*i+j*j==number:
                return True
    return False

number=400
print(check_squares(number))