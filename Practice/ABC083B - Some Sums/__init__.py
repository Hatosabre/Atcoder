N, A, B = input().split()
n = int(N)
a = int(A)
b = int(B)

result = 0

for i in range(1, n + 1):
    r1 = i % 10
    r2 = int(i / 10) % 10
    r3 = int(i / 100) % 10
    r4 = int(i / 1000) % 10
    r5 = int(i / 10000) % 10
    if a <= r1 + r2 + r3 + r4 + r5 <= b:
        result += i

print(result)
