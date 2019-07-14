N = input()
D = []
for i in range(int(N)):
    D.append(int(input()))

result = []
for i in D:
    if i in result:
        continue
    else:
        result.append(i)

print(len(result))


