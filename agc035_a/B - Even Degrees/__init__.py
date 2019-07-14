N, M = input().split()
n = int(N)
m = int(M)
A = []
if m % 2 == 1:
    print("No")
    exit()

for _ in range(n):
    a, b = input().split()
    a = int(a)
    b = int(b)
    A.append([a, b])

