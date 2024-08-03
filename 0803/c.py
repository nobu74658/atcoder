import numpy as np

N, M = map(int, input().split())
A = list(map(int, input().split()))

total = sum(A)
if M >= total:
    print('infinite')
# else:
#     bugdet = 0
#     while total > M:
#         total = sum([min(bugdet, a) for a in A])
#         bugdet -= 1
#     while total < M:
#         total = sum([min(bugdet, a) for a in A])
#         bugdet += 1
#     print(bugdet - 2)
    
# else:
#     sorted_A = sorted(A)
#     bugdet = max_A = max(sorted_A)
#     index = 1
#     over = 0
#     while total - over + bugdet * index > M:
#         # print(total - over + bugdet * index, M, bugdet, index, over, 'hoge')
#         while sorted_A[-index] >= bugdet:
#             over += sorted_A[index]
#             index += 1
#         bugdet -= 1
#     print(bugdet + 1)
    
else:
    sorted_A = sorted(A)
    index = N // 2
    alpha = max(N // 8, 1)
    bugdet = sorted_A[index]
    total = sum(sorted_A[:index]) + sorted_A[index] * (N - index)
    while alpha > 1 or total > M:
        while total < M:
            total = sum(sorted_A[:index]) + bugdet * (N - index)
            bugdet = sorted_A[index]
            index += alpha
            index = min(index, N)
        while total > M:
            bugdet = sorted_A[index]
            total = sum(sorted_A[:index]) + bugdet * (N - index)
            index -= alpha
            index = max(index, 0)
        alpha = max(alpha // 2, 1)
    print(bugdet)
