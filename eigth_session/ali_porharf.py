'''
علی به تعداد حرف هاییکه که مردم میزنند توجه زیادی میکند . 
او یک شعار دارد . کم گوی گزیده گوی :)
بهش کمک کنید که کوتاه ترین سخن رو پیدا کنه

ورودی یک لیست
خروجی یک رشته
'''

li = [
    {"name" : "navid" , "count" : 100},
    {"name" : "asqar" , "count" : 10},
    {"name" : "arash" , "count" : 1000},
    {"name" : "negar" , "count" : 5000},
    {"name" : "asd" , "count" : 3513135},
      ]

# li = ( ("navid" , 135) , ("negar" , 500) )

def ali(_li ):
    _max_word = 0
    _res = {}
    for person in _li:
        if person['count'] > _max_word:
            _res = person
            _max_word = person['count']
            
    return _res

print(ali(li))