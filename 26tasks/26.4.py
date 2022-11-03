'''В текстовом файле записан набор натуральных чисел, не превышающих 10**9
Гарантируется, что все числа различны. Необходимо определить сколько в наборе таких пар
чисел, что числа в паре имеют разную четность, а их сумма тоже присутствует в файле,
и чему равна наибольшая из сумм таких пар'''


with open('26.txt') as f:
    n = int(f.readline())
    lst = [int(x) for x in f]
    d = set(lst)
    res = []
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if (lst[i] + lst[j]) % 2:
                s = lst[i] + lst[j]
                if s in d:
                    res.append(s)

print(len(res), max(res))