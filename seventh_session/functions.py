a = [1, 2, 6, 8, 9]


def first_func():
    for i in a:
        i += 10
    return a


new_list = first_func()

new_list.append("negar")
# print(new_list)
# # ------------------


def test():
    for i in a:
        print("this is test : ", i)
        return "ok"


# test()
# print("end")

dic = {"name": "negar", "last_name": "rezaei", "age": 12}


# def cal():
#     for k, v in dic.items():
#         print("this is key : ", k, " ", "this is value : ", v)


# cal()


def get_param(x, y):
    print("this is sum : ", x + y)


# get_param(10, 17)
# get_param(4, 89)


def cal(a, b, c):
    return a ** b + c


# ans = cal(2, 3, 10)
# print(ans)


def power(a, b):  # parameter
    ans = 1
    for i in range(b):
        ans *= a
    return ans


# print(power(2, 5)) # argument

# if age = None:
#    greeting(name, 10)

# default
def greeting(name, age=10):
    print(f"hi {name} with age {age}")


# greeting("ali", 28)
# greeting("navid")


# order of parameter
def divide(x, y):
    print(x / y)


# divide(10, 5)
# divide(y=5, x=10)

# uncertain number of parameters non-keyword
def cal(*args):
    # print("this is args : ", args)
    # print("this type : ", type(args))
    new_list = list()
    for num in args:
        num += 10
        new_list.append(num)
    print(new_list)


# cal()
# cal(1, 2, 3)
# cal(2, 7, 8, 9, 0, 17)


# name=negar, family=rezaei, age=12, country=iran

# uncertain number of keyword arguments
def info(name, **kwargs):
    print("name : ", name)
    print(kwargs)
    print(type(kwargs))


# info("negar", family="rezaei", age=12, country="iran")


# def type_hint(name: str, age: int):
#     pass

# a, b, x


def dana_sleep(a, b, x):
    cnt = 0
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            if a % i == 0 and b % j == 0 and i + j <= x:
                cnt += 1

    return cnt


# print(dana_sleep(2, 2, 2))  # 1,1
# print(dana_sleep(7, 7, 14))  # 1, 7 - 7, 1 - 1, 1 - 7, 7


# n, k
# n = 10, k = 2

# 1 3 5 7 9 11 | 10 8 6 4 2

# n, k = input().split()

# k -= 1
# k <= n / 2 -> baze aval
# k > n / 2 -> baza dovom

# n % 2 == 0 -> k : dovom ------> n - (k - (n / 2)) * 2 | k -> aval : 1 + (k) * 2
# n % 2 == 1 -> k : dovom ------>

# def calculate(n, k):
#     ans = 0
#     if n % 2 == 0:
#         pass
#     else:
#         pass
#     print("this is ans : ", ans)


# calculate(n, k)
