'''
Created on Sep 30, 2019

@author: Anonymous
'''
#PF-Prac-13
def close_number(num1,num2,num3):
    #start writing your code here
    list=[]
    list.append(num1-num2)
    list.append(num1-num3)
    list.append(num2-num3)
    list.append(num2-num1)
    list.append(num3-num1)
    list.append(num3-num2)
    list.sort()
    list.reverse()
    cou=0
    for i in list:
        if abs(i)==1 or i==0:
            cou=cou+1
    if(cou==2):
        return True
    return False
    
print(close_number(5,4,2))