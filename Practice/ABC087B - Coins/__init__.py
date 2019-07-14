A = input()
B = input()
C = input()
X = input()
x = int(X)

result = 0

for a in range(int(A) + 1):
    for b in range(int(B) + 1):
        for c in range(int(C) + 1):
            if 10 * a + 2 * b + c == x / 50:
                result += 1

print(result)
