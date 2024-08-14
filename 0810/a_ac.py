# N = int(input())
# A = list(map(int, input().split()))
N, T, A = map(int, input().split())

if (T > N // 2):
    print('Yes')
elif (A > N // 2):
    print('Yes')
else:
    print('No')
