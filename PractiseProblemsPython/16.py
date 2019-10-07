'''
Created on Sep 29, 2019

@author: Anonymous
'''
#PF-Prac-16
def rotate_list(input_list,n):
    #start writing your code here
    output_list=input_list[-n:]+input_list[:-n]
    return output_list

input_list= [1,2,3,4,5]
output_list=rotate_list(input_list,2)
print(output_list)