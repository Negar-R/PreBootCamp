# '''
# Input :
# {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}


# Output :
# [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78},
# {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
# '''

data = {'Science': [88, 89, 62, 95 ], 'Language': [77, 78, 84, 80]}

# result = []

# keys = tuple(data.keys())
# values = tuple(data.values())
# print("keys",keys)
# print("values" , values)
# print()

# ## Checking if data is correct
# length = len(values[0])
# for courese in values:
#     if len(courese) != length :
#         exit()

# for i in range(length):
#     tmp = {}
#     for j in range(len(keys)):
#         tmp[keys[j]] = values[j][i]
#     result.append(tmp)

# # result = [{} * length]
# # for key in data:
# #     for value in data[key]:

# print(result)





# res = {}
# li1 = [1,2,3,4]
# li2 = ["navid" , "ALI" ,"asd" , "asd"]

# if len(li1) == len(li2):
#     for item in li2 :
#         res[item] = li1[li2.index(item)]

# print(res)


# res['a'] = "asd"




d= {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}

lst = [dict(zip(d, num)) for num in zip(*d.values())]