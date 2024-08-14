# N = int(input())
# A = list(map(int, input().split()))

def printChar(s, n):
    if (len(s) > n):
        return (s[n])
    else:
        return ('*')
    
# 初めにdが出てくるまでの文字列を取得する関数
def getFirstString(Sn):
    firstString = ''
    for i in range(len(Sn)-1, -1, -1):
        if (Sn[i] != '*' and Sn[i] != '\n'):
            firstString = Sn[:i+1]
            break
    return firstString

N = int(input())
Sn = []
for i in range(N):
    s = input()
    Sn.append(s)

answer = ''
isEnd = [False] * N
index = 0
while (isEnd.count(False) > 0):
    dump = ''
    for i in range(N-1, -1, -1):
        c = printChar(Sn[i], index)
        if (c == '*'):
            isEnd[i] = True
        if (not isEnd.count(False) == 0):
            dump += c
    index += 1
    answer += getFirstString(dump)
    if (not isEnd.count(False) == 0):
        answer += '\n'

print(getFirstString(answer))