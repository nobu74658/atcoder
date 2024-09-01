import numpy as np
N, M = map(int, input().split())
A = list(map(int, input().split()))

# (休憩所iから休憩所Nまでの距離) = (休憩所iから休憩所N-1までの距離)＋(休憩所N-1から休憩所Nまでの距離) = (休憩場iから休憩所i+1までの距離)＋(休憩所i+1から休憩所N-1までの距離)+(休憩所N-1から休憩所Nまでの距離)

count = 0
grid = np.array([[-1 for _ in range(N)] for _ in range(N)])

for i in range(N):
    grid[i][(i+1)%N] = A[i]

# grid[i][j]を計算する再帰関数、計算途中の値はgrid[i][j]に格納する
def calc(grid, i, j):
    if grid[i][j] != -1:
        return grid[i][j]
    else:
        if (j > 0):
            grid[i][j] = calc(grid, i, j-1) + calc(grid, j-1, j)
        else:
            grid[i][j] = calc(grid, i, N-1) + calc(grid, N-1, j)
        return grid[i][j]

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        calc(grid, i, j)
        if grid[i][j] % M == 0:
            count += 1

print(count)