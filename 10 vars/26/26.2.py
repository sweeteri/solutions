with open('26.txt') as f:
    s, n = map(int, f.readline().split())
    base_arr = sorted([int(i) for i in f], reverse=True)
    arr = []
    ss = 0
    ind = 0

    for i in range(n):
        if ss + base_arr[i] <= s:
            arr.append(base_arr[i])
            ss += base_arr[i]
            ind = i
        else:
            break

    base_arr = base_arr[ind + 1:]

    if s == sum(arr):
        print(len(arr), min(arr))
    elif s > sum(arr) and (s - sum(arr) in base_arr):
        print(len(arr) + 1, s - sum(arr))
    else:
        for j in base_arr:
            if j + sum(arr) <= s:
                print(len(arr) + 1, j)
                break
