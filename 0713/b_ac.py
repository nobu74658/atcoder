x_a, y_a = map(int, input().split())
x_b, y_b = map(int, input().split())
x_c, y_c = map(int, input().split())

# 2点間の距離を求める関数
def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2)

ab = distance(x_a, y_a, x_b, y_b)
bc = distance(x_b, y_b, x_c, y_c)
ca = distance(x_c, y_c, x_a, y_a)

# 直角三角形の判定
if ab + bc == ca:
    print('Yes')
elif bc + ca  == ab:
    print('Yes')
elif ca + ab == bc :
    print('Yes')
else:
    print('No')

