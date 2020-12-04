def minimumAsciiDltSumForTwoStrings(s1, s2):
    a = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
    for  i in range(1, len(s1), 1):
        a[i][0] += a[i-1][0] + ord(s1[i-1])
    for j in range(1, len(s2), 1):
        a[0][j] = a[0][j-1] + ord(s2[j-1])
    for i in range(len(a), 1):
        for j in range(1, len(a[0]),1):
            if s1[i-1] == s2[j-1]:
                a[i][j] = a[i-1][j-1]
            else:
                n1 = a[i-1][j] + s1[i-1]
                n2 = a[i][j-1] + s2[j-1]
                a[i][j] = min(n1, n2)
    return a[len(s1)][len(s2)]


if __name__ == "__main__":
    print(minimumAsciiDltSumForTwoStrings('sea', 'eat'))