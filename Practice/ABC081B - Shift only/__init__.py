N = input()
A = input().split()

result = 0

while True:
    for An in A:
        even = True

        if int(An) % (2 ** (result + 1)):
            even = False

        if not even:
            print(result)
            break

    else:
        result += 1
        continue
    break

