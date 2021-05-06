# # li = ["1", "50", "navid", "123", 1]


# # # DRY -> Don't Repeat Yourself

# # def search(ye_chizi):
# #     for item in li:
# #         if ye_chizi == item:
# #             is_found = True
# #             break
# #         else:
# #             is_found = False
# #     # print(is_found)
# #     return is_found


# # # ??? =  search("navid")
# # search("ASQar")
# # search(1)

# # if search(1):
# #     1 + 10

# # '''
# # argument ->
# # return   <-
# # '''

# # def print_khas(word):
# #     print(word)
# #     print("in kalame khas hastesh")


# # # def search()


# # li = [1, 2, 3, 4, 5, 4, 3]
# # li.pop(3)


# # def like_pop_once(li, item):
# #     res = []
# #     for i in range(len(li)):
# #         if li[i] == item:
# #             res = res + li[:i]
# #             res = res + li[i+1:]
# #             break
# #     if not res:
# #         return li
# #     return res


# # print(like_pop_once(li, 3))
# # print(like_pop_once(li, 3))
# # print(like_pop_once(li, 3))

# def average(li):
#     tmp = 0
#     for item in li:
#         tmp += item
    
#     result = tmp / len(li) 
     
#     return result 
    
# print(average([10,20,10,5,20]))

# # 3 X 2 
# # 3 + 3


# def mul(a, b):
#     result = 0
#     for i in range(1,b + 1):
#         result = result + a
#     return result

# print(mul(3 , 2))


# data = {"name" : "navid"}

# def search_in_dict(d,x):
#     for value in d.values():
#         if value == x:
#             return True
    
#     return False

# print(search_in_dict(data,"Hasan"))

# import datetime

# datetime.time()


# # def is_night() -> bool:
# #     return True
# #     return False

# # print(is_night())

# # def is_night():
# #     import datetime
# #     my_time=datetime.datetime.now()
# #     time=my_time.hour
# #     if time > 18:
# #         return True
# #     else:
# #         return False
    
    
def is_night():
    import datetime
    my_time = datetime.datetime.now()
    
    if my_time.hour > 20:
        return True
    else:
        return False
    

x = is_night()
print(x)

def search_list(li,item) -> bool:
    return True

def search_dict(li,item) -> bool:
    return True

def GCD(A , B):
    return 