N, Y = input().split()
n = int(N)
y = int(Y)

for i in range(n + 1):
    for j in range(n - i + 1):
        k = n - i - j
        if 10 * i + 5 * j + k == int(y / 1000):
            print("{} {} {}".format(i, j, k))
            exit()


print("-1 -1 -1")
