# for i in n:

# for i in range(10):
#     print(i)

# for i in range(20, 10)

n = int(input())

sum = 0
cnt = 0

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            sum += j
            cnt += 1

print(cnt, sum)

# n = {16} -> 1, 16 - 2, 8 - 4, 4 - 8, 2

# n ^ 2 = 10 ^ 36

# n.log(n) -> 10 ^ 18 * 10 ^ 4 -> 10 ^ 22

# order

# time complexity , space complexity

# size n, output

# hardware , compilar , language , algorithm

# while , for , ...

# n = 1 -> 1


# for(int i = 0; i < n; i++) -> n bar
# a += i -> n bar

# 1 + 1 + 3n -> O(n)
# import time

# start = time.time()

# for i in range(10 ** 18):
#     a = i

# end = time.time()

# print("end : ", end - start)

# n = 10 ^ 8 -> order(n) -> 1 s
# n = 10 ^ 16 -> log(n)