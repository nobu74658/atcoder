A,B,C = map(int, input().split())

isContain = False
while B != C:
    if B == 23:
        B = 0
    else:
        B += 1
    if A == B:
        isContain = True
        break

if isContain:
    print('No')
else:
    print('Yes')