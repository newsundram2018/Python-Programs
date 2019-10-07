'''
Created on Sep 29, 2019



@author: Anonymous
'''

#PF-Prac-37
def sum_of_list(num_list): 
    #Start writing your code here
    lst=num_list
    if len(num_list)>1:
    #Do not alter the below line
        return lst[0] + sum_of_list(lst[1:])
    return lst[0]
    
num_list=[44,23,77,11,89,3]
result=sum_of_list(num_list)
print("Sum of the elements:",result)