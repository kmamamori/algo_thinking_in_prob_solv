def permutationHelper(arr):
    if len(arr) == 1:
        return [[arr[0]]]
    else:
        t = []
        newarr = arr[1:]
        for i in range(0, len(newarr)):
            param = [newarr[i]] + newarr[0:i] + newarr[i + 1:len(newarr)]
            tt = permutationHelper(param)
            for i in range(0, len(tt)):
                if len(tt[i]) > 1:
                    t.append([arr[0]] + tt[i])
                else:
                    t.append([arr[0], tt[i][0]])
        return t

def permutation(arr):
    res = []
    for i in range(len(arr)):
        a = permutationHelper([arr[i]] + arr[0:i] + arr[i + 1:])
        for r in a:
            res.append(r)
    return res


if __name__ == "__main__":
  
    arr = []
    print(permutation(arr))
    arr = [1]
    print(permutation(arr))
    arr = [1, 2]
    print(permutation(arr))
    arr = [1, 2, 3]
    print(permutation(arr))
    arr = [1, 2, 3, 4]
    print(permutation(arr))