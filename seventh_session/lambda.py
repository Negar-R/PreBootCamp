def sum(x, y):
    return x + y


lambda x, y: x + y

# high_order_function


def high_order_function(x, func):
    print("this is x : ", x)
    print("this is func : ", func)
    print("this is ans : ", x + func(2))


# high_order_function(3, lambda x: x * 2)
# high_order_function(5, lambda x: x * 12)


def my_fuc(n):
    return lambda a: a * n


# result = my_fuc(2)
# print("this is result : ", result)
# print(result(10))

# n = 2, a = 10 -> 20

a = [1, 2, 3, 4]
b = []


def multiple():
    for i in a:
        b.append(i * 2)
    return b


# n = int(input())
# listt = list(map(int, input().split()))
# 1 2 3 1

# iterable : list, dic -> iterator = pointer , iterate
# map(fun , iterable)
# def -> for iterable -> +10

result = map(lambda x: x * 2, a)
# var = list(result)
# print("this is first iteration : ", tuple(result))
# print("this is second iteration : ", list(result))


def print_len(string):
    return len(string)


# result = list(map(len, ("banana", "apple", "orange")))
# print("this is result : ", result)

information = [
    {"name": "ali", "family": "najafi", "age": 18},
    {"name": "zahra", "family": "gilani", "age": 5},
    {"name": "elham", "family": "sharafi", "age": 20},
]

ans = list(map(lambda person: person["family"].upper(), information))
print(ans)

# map(fun , iterable)
# map : 1. C -> performance 2. memory usage

# -------------------------------

# marker = {color : number_of_marker_with_this_color}

# number color -> asc : avalin ozve in dic

# 1 1 2 3 4 -> 2,1 3,1 4,1 1,2
# 1 1 2 -> 2,1 1,2

# n = input()
# list_of_markers = list(map(int, input().split()))

# markers = {}

# for color in list_of_markers:
#     if color not in markers.keys():
#         markers[color] = 1
#     else:
#         markers[color] += 1

# result = sorted(markers.items(), key=lambda x: (x[1], x[0]))
# print("this is ans : ", result)

# sorted((key, value))

# print("final ans : ", result[0][0])


a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

power = list(map(pow, a, b))
print(power)
