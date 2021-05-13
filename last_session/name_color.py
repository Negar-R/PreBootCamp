import json

# loads data from file as a dict
with open("name_id.json", "r") as f:
    name_id_dict = json.load(f)


with open("id_color.json", "r") as f:
    id_color_dict = json.load(f)


# check dictionaries to find name and color that have same id
# and create a dictionary with key = name , value = color
result_dict = {}
for name, id in name_id_dict.items():
    result_dict[name] = id_color_dict[id]

# print("this is final result as a dict : ", result_dict)


# since f.write() only takes str convert dict to str by json.dumps()
with open("result.json", "w") as f:
    f.write(json.dumps(result_dict))
