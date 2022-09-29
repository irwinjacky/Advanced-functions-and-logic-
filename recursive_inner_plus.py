#%%
input_list = [1, 2, 3, 4, [5, 6, 7, [8, 9,]]]
list_two = input_list
print(list_two)
#create recursive function
def func_two(list_two):
    if len(list_two) > 0:
        if type(i) == list:
            list_two = list_two[i]
            return func_two(i)
        else:
            i += 1
    return list

func_two(list_two)
update_list = func_two(list_two)
adj_list = [x + 1 for x in list_two]
print(adj_list)
    

#%%