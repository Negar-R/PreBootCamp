# _file = open("karbar.txt", mode="r" , encoding="UTF-8")
# print(_file.read())   
# _file.close() 


# _file = open("karbar.txt", mode="w" , encoding="UTF-8")
# _file.write("salam az pythton")  
# _file.close() 


# # open("name" , mode= , encoding)

# # mode : r (read), w (write), a (append)

# # read()

# # close()

import json

_file = open("country-by-population.json" , mode="r")

countries_python_data = json.load(_file)

n = 10000000000000000

li = countries_python_data

total_population = 0
count_country = 0

for country in li:
    total_population += country['population']
    count_country += 1


for country in li:
    number_of_vacins = int( n * (country['population'] / total_population))
    country['number of vacins'] = number_of_vacins
    
_file.close()
_file = open("result.json" , mode="w")
# _file.write(str(li))
_file.write(json.dumps(li))
_file.close()


# >>> import json
# >>> 
# >>> 
# >>> res = '{"asd":156}'
# >>> res
# '{"asd":156}'
# >>> eval(res)
# {'asd': 156}
# >>> json.loads(res)
# {'asd': 156}
# >>> di = json.loads(res)
# >>> json.dump(di , open("asd.txt", mode="w"))
# >>> json.dumps(di)
# '{"asd": 156}'
# >>> 

'''
load -> فایل رو تبدیل به متقییر های پایتونی میکنه (اگه بتونه)
loads -> ورودیش یه استرینگ عه

/////////////

dump -> متقییر پایتونی رو داخل فایل میریزه
dumps -> خروجی اش یه استرینگه 
'''



