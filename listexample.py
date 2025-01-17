the_list = []
print(the_list)

list_items = [1,2,3,4,5]
print(list_items)

print(len(list_items))

first_item = list_items[0]
last_item = list_items [-1]

def find_middle_items():
    lst = [1,2,3,4,5,6]
    length = len(lst)
    mid_index1 = length //2 
    if length % 2 == 0:
        return [lst[mid_index1 -1]],
    else:
        return [lst[mid_index1]]

print(find_middle_items())