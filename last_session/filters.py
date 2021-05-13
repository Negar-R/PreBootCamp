names = ["sara", "dara", "kian"]

example = list(map(lambda name: name + "*", names))

# print(example)


numbers = [1, 2, 3, 4, 5]
# filter
# filer(func, iterable)

ans = list(filter(lambda num: num % 2 == 0, numbers))
# print(ans)

ans = list(map(lambda num: num % 2 == 0, numbers))
# print(ans)

ans = list(filter(lambda name: name + "*", names))
# print(ans)


users = [
    {"name": "negar", "age": 12},
    {"name": "ramin", "age": 23},
    {"name": "hamid", "age": 12},
]

ans = list(
    map(lambda user: user["name"], filter(lambda user: user["age"] == 12, users))
)
# print(ans)


# Genrator

# yield


def cal():
    return 2 + 3


# print(cal())


def gen():
    yield 2 + 3  # suspend, save state
    print("salam")
    a = 1 + 1
    print(a)
    yield "this is negar"


# generator = iterator -> pointer
# next


print("this is type : ", type(gen()))
# print(next(gen()))
# print(next(gen()))
# print(next(gen()))
# print(next(gen()))

a = gen()
# print(next(a))
# print(next(a))
# print(next(a))

try:
    print(next(a))
    print(next(a))
    print(next(a))
except Exception as e:
    print("this is error !! ", str(e))
    pass


# cpu -> a b

# l = [x for x in range(10)]
# print(l)
# print(len(l))

g = (x for x in range(10))
print(type(g))

print(next(g))
print(next(g))
print(next(g))
print(next(g))

print(len(g))

# 1, 1, 2, 3, 5, 8
