'''
Created on Sep 29, 2019
Given a string, write a python function to return True if the strings "mat" and "jet" appear the same number of times in the given string, else return False.
Note: Perform case insensitive string comparison wherever necessary.

Sample Input    Expected Output
Jet on the Mat but mat is too long    False
mat jet Jet Mat    True

@author: Anonymous
'''

#PF-Prac-26
def check_occurence(string):
    #start writing your code here
    count_Jet=0
    count_met=0
    string=string.lower()
    for i in string.split():
        if i=='jet':
            count_Jet+=1
        elif i=='mat':
            count_met+=1
    if count_met==count_Jet:
        return True
    return False
    
string="Jet on the Mat but mat is too long"
print(check_occurence(string))