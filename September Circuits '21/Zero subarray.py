tc = int(input())

for _ in range(tc):
    n, x, y = map(int, input().split())
    arr = list(map(int, input().split()))
    original_arr = arr

    arr.sort()
    #print(arr)

    for i in range(n):
        if arr[i] == 0:
            continue

        if x > 0 and arr[i] == 1:
            #print(x, arr[i], "1")
            arr[i] -= 1
            x -= 1

        elif y > 0:
            #print(y, arr[i], "2")
            arr[i] = 0
            y -= 1

    #print(arr)
    c_max = 0
    max_so_far = 0

    for i in range(n):
        if arr[i] != 0:
            c_max = 0

        else:
            c_max += 1
            max_so_far = max(c_max, max_so_far)
    print(max_so_far)
