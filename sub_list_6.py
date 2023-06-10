def get_sublist_with_every_other(list_data, start_index, end_index):
    sub_list = list_data[start_index:end_index+1]
    return sub_list[1::2]

list_data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
start_index = 2
end_index = 9

result = get_sublist_with_every_other(list_data, start_index, end_index)
print(result)