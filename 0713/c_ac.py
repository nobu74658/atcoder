import numpy as np

N = int(input())
L = []
R = []
for i in range(N):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

# Lの合計値を求める
L_sum = sum(L)
# Rの合計値を求める
R_sum = sum(R)

if (L_sum > 0 | 0 > R_sum):
    print('No')
else:
    # RからLを引いた値を求める
    R_subtract_L = np.array(R) - np.array(L)
    index = 0
    while L_sum < 0 | index < N:
        if - L_sum >= R_subtract_L[index]:
            L_sum += R_subtract_L[index]
            L[index] += R_subtract_L[index]
            R_subtract_L[index] = 0
        else:
            R_subtract_L[index] += L_sum
            L[index] -= L_sum
            L_sum = 0
        index += 1
    if L_sum == 0:
        print('Yes')
        for i in range(N):
            print(L[i])
    else:
        print('No')