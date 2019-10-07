'''
Created on Sep 30, 2019

@author: Anonymous
'''
#PF-Prac-21
def check_numbers(num1,num2):
    #start writing your code here
    list=[i for i in range(num1,num2+1)]
    num_list=set()
    for i in range(len(list)):
        for j in range(len(list)):
            if i==j:
                continue
            elif list[i]%list[j]==0:
                num_list.add(list[i])
    count=len(num_list)
    return [set(num_list),count]

num1=10
num2=30
print(check_numbers(num1, num2))