"""
Набор данных представляет собой последовательность целых чисел.
Необходимо выбрать такую подпоследовательность подряд идущих чисел,
чтобы их сумма была минимальной и делилась на 2077, и определить её длину.
Если таких подпоследовательностей несколько, нужно выбрать подпоследовательность наибольшей длины.
"""
with open('27B.txt') as f:
    n = int(f.readline())
    mods = [-10 ** 20] * 2077
    ls = [0] * 2077
    min_sum, s = 10 ** 9 + 1, 0
    max_len = 0
    for i in range(n):
        x = int(f.readline())
        s += x
        if x % 2077 == 0 and s <= min_sum:
            min_sum, max_len = s, i + 1

        p_sum = s - mods[s % 2077]
        p_len = i + 1 - ls[s % 2077]
        if p_sum < min_sum or (p_sum == min_sum and p_len > max_len):
            min_sum, max_len = p_sum, p_len

        if s > mods[s % 2077]:
            mods[s % 2077] = s
            ls[s % 2077] = i + 1
print(max_len)
