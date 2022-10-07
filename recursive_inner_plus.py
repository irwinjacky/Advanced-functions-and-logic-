#%%
input_list = [1, 2, 3, 4, [5, 6, 7, [8, 9,]]]
list2 = input_list
#set variables

def sublist2(list2):    #create function
    list_output = list2 #create a list that isn't changing the function
    i = 0               #set index to 0
    while type(list_output) != int and i < len(list_output):
        if type(list_output[i]) != int:
            list_output = list_output[i]
            i = 0
        else:
            i += 1
    return list_output

sublist2(list2)
list_two = sublist2(list2)
list_two_adj = [x + 1 for x in list_two]
print(list_two_adj)
#%%