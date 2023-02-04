"""
Необходимо определить максимальную разницу двух элементов этой последовательности,
такую, что она кратна 137 и расстояние между двумя элементами не менее 5.
"""
with open('27B.txt') as f:
    n = int(f.readline())
    q = [int(f.readline()) for _ in range(4)]
    mod_min = [10 ** 5 + 1] * 137
    mod_max = [0] * 137
    max_delta = 0
    for _ in range(n - 4):
        x = int(f.readline())
        # checking only previous ones
        if mod_max[x % 137] != 0:
            max_delta = max(max_delta, abs(x - mod_max[x % 137]))
        if mod_min[x % 137] != 10 ** 5 + 1:
            max_delta = max(max_delta, abs(x - mod_min[x % 137]))

        mod_max[q[0] % 137] = max(mod_max[q[0] % 137], q[0])
        mod_min[q[0] % 137] = min(mod_min[q[0] % 137], q[0])
        q.append(x)
        q.pop(0)

print(max_delta)
