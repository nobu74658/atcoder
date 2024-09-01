import numpy as np

N, K = map(int, input().split())
R = list(map(int, input().split()))

# [[],[],[],[],[]]
# fix result = [[] for i in range(N)]
array = [[] for _ in range(N)]

for i in range(len(R)):
    R_i = R[i]
    while R_i != 0:
        array[i].append(R_i)
        R_i -= 1

# print(array)

# [[1,2],[3,4]]なら[[1,3],[1,4],[2,3],[2,4]]を返す
# fix result = [[]]
result = [[]]
for i in range(len(array)):
    result = [x + [y] for x in result for y in array[i]]

# print(result)

answer = []
for i in range(len(result)):
    if sum(result[i]) % K == 0:
        answer.append(result[i])

answer.reverse()
for i in range(len(answer)):
    for j in range(len(answer[i])):
        print(answer[i][j], end=' ')
    print()