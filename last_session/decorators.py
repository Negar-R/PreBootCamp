def hi_dicorator(fun):
    def wrapper(*args, **kwargs):
        print("befor execution")
        fun(*args, **kwargs)
        print("nice to meet you")

    return wrapper


@hi_dicorator
def say_hello():
    print("hi every body")


# first_test = hi_dicorator(say_hello)
# first_test()

# say_hello()
# print(type(first_test), " ## ", first_test)

# print("_____________________________")


@hi_dicorator
def salam_felani(name):
    print(f"salam {name}")


# salam_felani("negar")

# @login_required
# def sample1():
# ....


# bubble sort

n = int(input())

# 1234
while True:
    n += 1

    digits = set()

    yeakn = int(n % 10)
    dahgan = int((n / 10) % 10)
    sadgan = int((n / 100) % 10)
    hezargan = int((n / 1000) % 10)

    digits.add(yeakn)
    digits.add(dahgan)
    digits.add(sadgan)
    digits.add(hezargan)

    if len(digits) == 4:
        print(n)
        break
