def pickUpSticks(n):
    # Array to store the total way
    arr = [0] * (n + 1)
    arr[0] = 1
    arr[1] = 1
    arr[2] = 2
    for i in range(3, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]
    return arr[n]

n = int(input())
res = pickUpSticks(n)
print(res)