S = input()

T = ""

dreamer = "dreamer"
dream = "dream"
eraser = "eraser"
erase = "erase"

while True:
    if S[len(S) - 5:] == erase:
        S = S[:len(S) - 5]
        continue
    if S[len(S) - 5:] == dream:
        S = S[:len(S) - 5]
        continue
    if S[len(S) - 6:] == eraser:
        S = S[:len(S) - 6]
        continue
    if S[len(S) - 7:] == dreamer:
        S = S[:len(S) - 7]
        continue
    break

if S == "":
    print("YES")
else:
    print("NO")
