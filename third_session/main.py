# input

# age = int(input())

# print(f"sen {age}")

# t = type(age)
# print(t)


# n, x, y = input().split(",")

# age = int(input("inter your age : "))

# a = int(input())

st_1 = "salam be hame"

# print(st_1[0])
# for i in st_1:
#     print("this is of list : ", i)


# list
list_1 = []
list_1 = list()
print(type(list_1))

# lists can have any type of data
# list_1.append("hi")
# list_1.append(12)
# list_1.append(True)


# list_1.append("hi")
# list_1.append("hi")

# print(list_1)

# print(list_1[0])
# print(list_1[2])

# remove : delete item
# list_1.remove(12)
# print(list_1)

# list_1.remove("hi")
# print(list_1)

# pop : delete the item in one specific index
# list_1.pop(0)
# print(list_1)

# list_1.pop(3)

# list_1.append("salam")
# list_1.append("negar")

# print(list_1)

# list_1.pop()
# print(list_1)

# changeable, ordered, indexed, duplicate data

a = []
a.append(12)
a.append(13)
a.append(11)
a.append(1)
a.append(10)

print(a)

a.sort()

print(a)

a.reverse()
print(a)

b = ["banana", "apple", "23"]
b.sort()
print(b)

# index list
# 0 1 2 ...
# [, , , , , ]
#            -3,-2,-1

# l = len(b)
# print(b[l - 1])
# print("negetive index : ", b[-2])

# colliction -> iterable
# b = []
# for i in range(1, 13):
#     b.append(i)
#     b.reverse()

# print(b)

# for i in range(4, 9):
#     print(f"this is the {i}th elm of list : ", b[i])

# print(b[4:9])
# print(b[:])
# print(b[:-1])
# print(b[4:])
# print(b[-1:0])
# print(b[1:1])

# print(b[::])


# comrehension list
# a = [x for x in range(1, 13) if x % 2 == 0]

# print("this is : ", a)

# a = ["apple", "inj", "negar", "ghuuyggi"]

# b = [reshte for reshte in a if reshte.count("a") != 0]
# print(b)


# # string -> list

# if "ali" in a:
#     print("hi")
# else:
#     print("bye")

# if "n" in "negar":
#     print("ghhhhh")


a = 12
b = "salam"

c = 13

d = 12 + 13