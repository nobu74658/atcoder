# 階上の関数
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# 文字列sに長さkの回文が含まれているかを判定する関数
def is_palindrome(s, k):
    for i in range(len(s) - k + 1):
        if s[i:i+k] == s[i:i+k][::-1]:
            return True
    return False


# 文字列sを並び替えて得られるすべての文字列を生成する関数
def generate_all_strings(s):
    if len(s) == 1:
        return [s]
    else:
        result = []
        a_z = [0] * 26
        for i in range(len(s)):
            a_z[ord(s[i]) - ord('a')] += 1
            if a_z[ord(s[i]) - ord('a')] > 1:
                continue
            for t in generate_all_strings(s[:i] + s[i+1:]):
                result.append(s[i] + t)
        return result


N, K = map(int, input().split())
S = input()
az = [0] * 26
for i in range(N):
    az[ord(S[i]) - ord('a')] += 1
ct = 0
for i in range(26):
    ct += az[i] // 2
if ct < K //2:
    result = factorial(N)
    for i in range(26):
        result /= factorial(az[i])
    print(int(result))
    exit()
all_strings = set(generate_all_strings(S))
count = 0
for s in all_strings:
    if not is_palindrome(s, K):
        count += 1

print(count)