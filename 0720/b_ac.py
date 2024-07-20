import numpy as np
N, T, P = map(int, input().split())
L = list(map(int, input().split()))

# T以上の要素の数
count = 0
for i in range(N):
    if L[i] >= T:
        count += 1
        
day = 0
if count >= P:
    print(0)
else:
    while count < P:
        day += 1
        count = 0
        for i in range(N):
            if L[i] >= (T - day):
                count += 1
    print(day)