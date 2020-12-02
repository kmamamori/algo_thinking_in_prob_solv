def isSubset(nums, k):
    if (sum(nums)) % k != 0:
        print('a')
        return False
    res = []
    setgoal = sum(nums) / k
    isUsed = [0 for i in range(len(nums))]
    maxindex = len(nums)
    while True and maxindex < 0:
        i = 0
        if nums[i] > setgoal or nums[i] < 0:
            print('b')
            return False
        if nums[i] == setgoal:
            res.append([nums.pop(i)])
        else:
            # goal = setgoal - nums[i]
            t = adding2numbers(nums, setgoal)
            if t == []:
                return False
            else:
                temp = []
                for j in t:
                    temp.append(nums[j])
                res.append(temp)
                for j in t:
                    nums.pop(j)
        maxindex -= 1
        i += 1

    if len(res) != k:
        print('c')
        print('res', res)
        return False
    if len(nums) != 0:
        print('d')
        return False
    return True


def subsetsHelper(arr, s, isUsed, subset, k, N, c, l):
    if s[c] == subset:
        if (c == k - 2):
            return True
        return subsetsHelper(arr, s, isUsed, subset, k, N, c + 1, N - 1)
    for i in range(l, -1, -1):
        if (isUsed[i]):
            continue
        t = s[c] + arr[i]
        if (t <= subset):
            isUsed[i] = True
            s[c] += arr[i]
            n = subsetsHelper(arr, s, isUsed, subset, k, N, c, i - 1)
            isUsed[i] = False
            s[c] -= arr[i]
            if (n):
                return True
    return False


def isSubsets(arr, k):
    if (k == 1):
        return True
    if (len(arr) < k):
        return False
    total = sum(arr)
    if (total % k != 0):
        return False
    subset = total // k
    s = [0 for i in range(k)]
    isUsed = [False for i in range(len(arr))]

    s[0] = arr[-1]
    isUsed[-1] = True
    return subsetsHelper(arr, s, isUsed, subset, k, len(arr), 0, len(arr) - 1)


def adding2numbers(testingarray, target):
    additionarray = []
    for i in range(len(testingarray) - 1, -1, -1):
        if target == 0 and len(additionarray) == 2:
            return additionarray
        if target > testingarray[i] and len(additionarray) == 0:
            target -= testingarray[i]
            additionarray.append(testingarray[i])
        elif testingarray[i] == target and len(additionarray) == 1:
            additionarray.append(testingarray[i])
            return additionarray


if __name__ == "__main__":
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    print(isSubsets(nums, k))
