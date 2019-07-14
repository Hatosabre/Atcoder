N = input()
plan = []
for _ in range(int(N)):
    plan_i_t, plan_i_x, plan_i_y = input().split()
    plan_i = [int(plan_i_t), int(plan_i_x), int(plan_i_y)]
    plan.append(plan_i)

for i in range(len(plan)):

    if i == 0:
        dist = abs(plan[i][1]) + abs(plan[i][2])
        if not(dist <= plan[i][0] and (plan[i][0] - dist) % 2 == 0):
            print("No")
            exit()
    else:
        dist = abs(plan[i][1] - plan[i - 1][1]) + abs(plan[i][2] - plan[i - 1][2])
        if not(dist <= plan[i][0] - plan[i - 1][0] and (plan[i][0] - plan[i - 1][0] - dist) % 2 == 0):
            print("No")
            exit()

print("Yes")