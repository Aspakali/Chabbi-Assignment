def sort_list_of_dicts(list_of_dicts, key):
    return sorted(list_of_dicts, key=lambda x: x[key])

input_list = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]

sorted_list = sort_list_of_dicts(input_list, "fruit")
print(sorted_list)

sorted_list = sort_list_of_dicts(input_list, "color")
print(sorted_list)
