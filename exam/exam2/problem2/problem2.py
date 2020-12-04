def palindromicSubstrings(s):
    r = 0
    a = [[0 for j in range(len(s))] for i in range(len(s))]
    # print(a)
    for i in range(len(s)):
        for j in range(len(s)-i):
            a[i][j] = 1 if i <= 2 or a[i-2][j+1]==1 and s[j]==s[i+j] else 0
            if a[i][j] == 1:
                r+=1
    return r

if __name__ == "__main__":
    s = "aaa"
    print(palindromicSubstrings(s))