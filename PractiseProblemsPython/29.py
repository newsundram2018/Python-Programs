'''
Created on Sep 29, 2019
Given a list of numbers, write a python function to exchange the first n/2 elements of a list with the last n/2 elements. The function should return the new list.
n represents the number of elements in the list. Assume that it will always be even.


Sample Input    Expected Output
[1,2,3,4,5,6,7,8,9,10]    [10,9,8,7,6,1,2,3,4,5]
@author: Anonymous
'''
#PF-Prac-29
def exchange_list(number_list):
    #start writing your code here
    l=len(number_list)
    sh=l//2
    nlist=[]
    for i in number_list[sh:]:
        nlist.append(i)
    nlist.reverse()
    number_list=number_list[:sh]
    nlist.extend(number_list)

    
    return nlist
     
number_list=[1,2,3,4,5,6]
print(exchange_list(number_list))