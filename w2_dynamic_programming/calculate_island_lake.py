
def water_in_lake(arr):
    # print("aaa")
    top = arr[0]
    curtop = arr[0]
    verifyTop = 0
    remember_id = 0
    sum = 0
    i = 0
    verifying = False
    while i < len(arr):
        # for i in range(1, len(arr)):
        if curtop > arr[i]:
            sum += (curtop-arr[i])
        else:
            curtop = arr[i]
            remember_id = i
            verifyTop = arr[i]
        i += 1
    print(sum)


def water_in_lake2(arr):
    possibleheight1, possibleheight2, arrsum = [0 for a in range(
        len(arr))], [0 for a in range(len(arr))], [0 for a in range(len(arr))]
    max = 0
    arrsum = [0 for a in range(len(arr))]
    for i in range(len(arr)):
        if max < arr[i]:
            max = arr[i]
        possibleheight1[i] = max
    max = 0
    for i in range(len(arr)-1, -1, -1):
        if max < arr[i]:
            max = arr[i]
        possibleheight2[i] = max
    for i in range(0, len(arr), 1):
        if possibleheight1[i] < possibleheight2[i]:
            arrsum[i] = possibleheight1[i] - arr[i]
        else:
            arrsum[i] = possibleheight2[i] - arr[i]
    return sum(arrsum)

def main():
    arr = [1, 3, 2, 4, 1, 3, 1, 4, 5, 2, 2, 1, 4, 2, 2]
    print(arr, "=", water_in_lake2(arr))
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(arr, "=", water_in_lake2(arr))

main()
