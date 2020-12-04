def integerBreak(n):
    if n > -1:
        m = [0 for i in range(n+1)]
        m[0], m[1] = 0,1
        for i in range(1, n+1):
            for j in range(1, i):
                m[i] = max(m[i], j*(i-j), m[i-j]*j)
        return m[-1]
    return 0

if __name__ == "__main__":
    print(integerBreak(2))
    print(integerBreak(10))