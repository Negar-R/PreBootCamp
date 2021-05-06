import json
import math

def finder(file_name : str ):
    '''
    Looks for salaries lower than this given input
    دنبال حقوق های پایین تر از ورودی داده شده می گردد
    
    '''
    _file = open(file_name , mode = 'r')
    persons = json.load(_file)
    # print(persons)
    min_salary = int(input("min salary >>>"))
    
    _res = []
    for person in persons:
        if person['salary'] > min_salary:
            _res.append(person['name'])

    _file = open("result.txt" , mode = "w")
    _file.write(str(_res))
    return _res
    
finder("salaries.json")
# file open
# file print
# salary
# print / file result.txt
# close

# [
#     {
#         "name" : "navid",
#         "salary" : 10
#     },{
#         "name" : "erfan",
#         "salary" : 1
#     },{
#         "name" : "fateme",
#         "salary" : 1400
#     },{
#         "name" : "david",
#         "salary" : 100
#     }
# ]

