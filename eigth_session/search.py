

def search_in_dict(_d, item):
    if type(_d) == dict:
        for key, value in _d:
            if item == key:
                return True
    return False




def search_in_list(_li ,item):
    for _item in _li:
        if _item == item:
            return True
    return False

d = {
    "name": "navid",
    "age": 21,
    "city": "Tehran"
}

item = 21


if search_in_dict(d,item):
    print("OK , item Peyda shod ^__^")
else:
    print("Sharmande peyda nashod")



names = ["navid" , "erfan" , "zahra" , "shalqam"]

if search_in_list(names ,"nader"):
    print("bi vasat beraqs")
else:
    print("KaC nabod ... ")