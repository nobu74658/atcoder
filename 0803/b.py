N = int(input())
A = list(map(int, input().split()))
second_biggest = sorted(A)[-2]

print(A.index(second_biggest)+1)