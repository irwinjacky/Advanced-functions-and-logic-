# %%
#given list
list_one = [1,2,3,4,[5,6,7,[8,9,]]]
#set i = index = to 0
i = 0
#create while loop

while True:
    #create a variable for the length of the list
    length = len(list_one)
    #once you reach the end of the list length end the loop
    if i == length:
        break
    #check i value type
    if type(list_one[i]) != int:
        #set the list equal to to the inner list
        list_one = list_one[i]
        #reset the value of i
        i = 0
    #if value of i is not list then move on
    else:
        i += 1
    
#adjust the list to add one to the values in the list
list_one_adj = [x + 1 for x in list_one]

print(list_one_adj)
# %%
