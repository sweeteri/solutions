"""
Дана последовательность натуральных чисел.
Найти подпоследовательность подряд идущих чисел,
чтобы их сумма была максимальной и делилась на 69, и определить её длину.
Гарантируется, что такая подпоследовательность существует.
Если таких подпоследовательностей несколько, нужно выбрать подпоследовательность наименьшей длины.
"""
with open('27A.txt') as f:
    n = int(f.readline())
    s, max_sum = 0, 0
    mods = [10 ** 9] * 69
    ls = [0] * 69
    min_len = 0
    for i in range(n):
        x = int(f.readline())
        s += x
        if s % 69 == 0:
            max_sum, min_len = s, i + 1

        p_sum = s - mods[s % 69]
        p_len = i + 1 - ls[s % 69]
        if p_sum > max_sum or (p_sum == max_sum and min_len > p_len):
            max_sum, min_len = p_sum, p_len

        if s < mods[s % 69]:
            mods[s % 69], ls[s % 69] = s, i + 1

print(min_len)





