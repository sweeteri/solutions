with open('27b.txt') as f:
    n = int(f.readline())
    min_0, min_1 = 1001, 1001
    k_0, k_1 = 0, 0
    k = 0

    for i in f:
        x = int(i)
        if x % 2:
            k_1 += 1
            min_1 = min(min_1, x)
            if x > min_0:
                k += k_0
        else:
            k_0 += 1
            min_0 = min(min_0, x)
            if x > min_1:
                k += k_1
print(k)
