'''
Created on Sep 29, 2019

@author: Anonymous
'''
#PF-Tryout

def doublePreceding (values):
    if len(values) > 0:
        previous = values[0]
        values[0] = 0
        for idx in range(0, len(values)):
            values[idx] = 2 * previous
            previous = values[idx]
    return values
    
print(doublePreceding([3,8,2]))