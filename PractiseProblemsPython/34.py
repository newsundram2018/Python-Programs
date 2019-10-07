'''
Created on Oct 7, 2019

@author: Anonymous
'''
#PF-Prac-34
def check_well_formatted(input_item,list_label):
    #Start writing your code here
    if type(input_item) != list or len(input_item) < 2 or (input_item[0] not in list_label):
        return False
    else:
        for i in input_item[1:]:
            if type(i) != str and not check_well_formatted(i, list_label):
                return False
        return True

input_list1=['VP', ['V', 'eat']]
list_label1=['VP', 'V']
result=check_well_formatted(input_list1,list_label1)
if result is True:
    print("Well formatted")
else:
    print("Not Well formatted")