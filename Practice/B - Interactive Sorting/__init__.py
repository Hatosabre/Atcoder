import sys

i_N, i_Q = sys.stdin.readline().rstrip().split()
N = int(i_N)
Q = int(i_Q)

weight = ""
for x in range(N):
    weight += chr(ord('A') + x)


n = 0
for _ in range(Q):
    if n % N > (n + 1) % N:
        n = 0

    print("? {} {}".format(weight[n % N], weight[(n + 1) % N]), flush=True)
    sys.stdout.flush()

    ans = sys.stdin.readline().rstrip()
    if ans == '>':
        # cp = weight[n % N]
        # weight[n % N] = weight[(n + 1) % N]
        # weight[(n + 1) % N] = cp
        if (n + 2) % N != 0:
            weight = weight[:n % N] + weight[(n + 1) % N] + weight[n % N] + weight[(n + 2) % N:]
        else:
            weight = weight[:n % N] + weight[(n + 1) % N] + weight[n % N]

    n += 1

print("! {}".format(weight), flush=True)
