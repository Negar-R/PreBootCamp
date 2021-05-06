# # # # li = [1,2,3,4,4,4,4,"asd",-1,-2000,4]
# # # # res = []
# # # # for i in range(len(li)):
# # # #     if li[i] in li :
# # # #         if li[i] not in res :
# # # #             res.append(li[i])
# # # #         else:
# # # #             res.append(None)

# # # # print(li.index("asd"))
# # # # print(res.index("asd"))


# # # # karmandan = [
# # # #     {
# # # #     "name ": "navid",
# # # #     "age" : 22
# # # # }, {"name" : "Zahra", "age" : 10}]

# # # # print(karmandan[1].get("name"))
# # # # print(karmandan[1].get("age"))


# # # print(tehran.get("country"))
# # # print(tehran["country"])

# # def asd():
# #     tehran = {
# #         "name" : "tehran",
# #         "country" : "Iran",
# #         "pop" : 80,
# #     }
# #     print(tehran)

# # asd()

import json
humans = []

for i in range(2):
    # person = {}
    # person['name'] = input("namet chiest ??")
    # person['field'] = input("field et chie hala ??")
    # humans.update(i, person)
    name , field = input("name , field ").split()
    humans.append({"name" : name , 'field' : field})

print(json.dumps(humans))


# {0: {'name': 'navid', 'field': 'asd'}, 1: {'name': 'nahid', 'field': '123'}}

# JSON :
#     {
#         humans : [
#             {'name': }
#         ]
#     }

# humans = [
#     {
#         "name" : "navid" ,
#         "field" : "students"
#     },
#     {
#         "name" : "arash",
#         "field" : "teacher"
#     },
#     {
#         "name" : "navid" ,
#         "field" : "students"
#     },
#     {
#         "name" : "arash",
#         "field" : "teacher"
#     }
# ]

# list
# set 
# tuple
# dict
# update()
# items()
# values()

# iterating on dictionary ... !

# for (key , value) in a_dict:
    
# immutability
# mutable
