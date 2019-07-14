N = input()
A = input().split()
Int_A = [int(a) for a in A]

Int_A.sort(reverse=True)

result = 0
flag = True
for a in Int_A:
    if flag:
        result += a
    else:
        result -= a

    flag = not flag

print(result)