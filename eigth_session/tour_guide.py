'''
دو گروه با هم به یک سفر تفریحی میرن . گروه اول نزدیک ترین مسیر رو انتخاب میکنه و گروه دوم دور ترین مسیر رو .
بهشون کمک کنید مسیر رو از روی نقشه پیدا کنند
'''

Cities = {
    "Tehran": {'mashhad': 1000, 'esfahan': 1500},
    'mashhad': {'Bandar abas': 2500},
    'esfahan': {'Bandar abas': 500}
}

start = 'Tehran'
end = 'Bandar abas'

'''
حلقه ی ابتدایی
end = {
    'mashhad' : 1000,
    'esfahan' : 1500
}
حلقه ی دومی
end = {
    'mashhad' : 3500,
    'esfahan' : 2000
}
'''

ends = {}
for city , routes in Cities.items():
    if city == start:
        ends.update( routes)
        
print("------------***Step 1***---------")
print(ends)


for city , distance in ends.items():
    _city = Cities.get(city,None)
    if _city and end in _city :
        ends[city] += Cities[city][end]
        
print("------------***Step 2***---------")
print(ends)

resultA = [] 
resultB = [] 
max_distance = 0
min_ditance = 10000000

for city , _distance in ends.items():
    if max_distance < _distance:
        resultA = [city,_distance]
        max_distance = _distance
    if min_ditance > _distance:
        resultB = [city,_distance]
        max_distance = _distance
        
print("------------***Result***---------")
print((resultA,resultB))