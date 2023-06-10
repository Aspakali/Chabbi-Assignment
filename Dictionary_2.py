def get_file_types(extension_type_string, file_list):
    extension_type_list = extension_type_string.split(";")
    extension_type_mapping = {}
    for item in extension_type_list:
        extension, file_type = item.split(",")
        extension_type_mapping[extension] = file_type

    file_type_dict = {}
    for file_name in file_list:
        if "." in file_name:
            extension = file_name.split(".")[-1]
            file_type = extension_type_mapping.get(extension, "unknown")
        else:
            file_type = "unknown"
        file_type_dict[file_name] = file_type

    return file_type_dict


extension_type_string = "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
file_list = ["abc.jpg", "xyz.xls", "text.csv", "123"]

result = get_file_types(extension_type_string, file_list)
print(result)
