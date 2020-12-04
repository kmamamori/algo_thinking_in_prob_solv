

def perfectSquares(n):
    a = [0 for i in range(n+1)]
    for i in range(1, n+1, 1):
        m, j = 10000, 1
        while j*j <= i:
            m = min(m, a[i-j*j]+1)
            j += 1
        a[i] = m
    return a[n]

if __name__ == "__main__":
    print(perfectSquares(12))