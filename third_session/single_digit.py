n = input()

while len(n) > 1:
    sum = 0
    for i in n:
        sum += int(i)
    n = str(sum)

print(n)
