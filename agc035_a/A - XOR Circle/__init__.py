# import copy
#
N = input()
A = input().split()
n = int(N)
Int_A = [int(a) for a in A]

k = 0

for a in Int_A:
    k ^= a

if k == 0:
    print("Yes")
else:
    print("No")
