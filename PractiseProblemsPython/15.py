'''
Created on Sep 29, 2019

@author: Anonymous
'''
#PF-Prac-15
def check_22(num_list):
    #start writing your code here
    for i in range(len(num_list)-1):
        if num_list[i]==2 and num_list[i+1]==2:
            return True
    return False
            
        
print(check_22([3,2,5,1,2,1,2,2]))