'''
Created on Sep 30, 2019

@author: Anonymous
'''
#This problem should be done in Eclipse. Copy the below code to Eclipse and get started.

#PF-Tryout

def number_lines( file_path ):
    #start writing your code here
    f=open(file_path,"r")
    x=open("newfile.txt","w")
    data=f.readlines()
    count=1
    for i in range(len(data)):
        x.write("{}".format(count)+data[i])
        count+=1
    
                      
file_path="13.py"
number_lines(file_path)



