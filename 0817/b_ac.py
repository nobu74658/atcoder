X = str(input())

index = -1
while X[index] == '0':
    index -= 1

if index == -1:
    print(X)
    exit()

if X[index] == '.':
    print(X[:index])
else:
    print(X[:index+1])