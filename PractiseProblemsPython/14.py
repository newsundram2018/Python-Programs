'''
Created on Sep 26, 2019

@author: Anonymous
'''
#PF-Tryout
def find_five_digit():
    #start writing your code here
    x=10000
    while True:
        print(x)
        y=[int(i) for i in str(x)]
        if((y[0]+2)==y[1] and (y[1]+2)==y[2] and (y[3]-2)==y[2] and (y[4]+2)==y[3]):
            return y
        x+=1

find_five_digit()