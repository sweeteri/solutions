"""
Имеется набор данных, состоящий из троек положительных целых чисел.
Необходимо выбрать из каждой тройки два числа так,
чтобы сумма всех выбранных чисел делилась на 4 и при этом была максимально возможной.
"""
with open('27B.txt') as f:
    f.readline()
    s = 0
    deltas = set()
    for i in f:
        nums = sorted(map(int, i.split()))
        s += nums[1] + nums[2]
        deltas.add(nums[1] - nums[0])
        deltas.add(nums[2] - nums[0])

if s % 4 == 0:
    print(s)
else:
    new_min_delta = sorted(deltas)[0]
    ss = 0
    for i in sorted(deltas)[1:]:
        if (s - new_min_delta) % 4 == 0 or (s - i) % 4 == 0:
            if (s - new_min_delta) % 4 == 0:
                ss = max(ss, s - new_min_delta)
            if (s - i) % 4 == 0:
                ss = max(ss, s - i)
            print(ss)
            break
        else:
            if (s - (new_min_delta + i)) % 4 == 0:
                new_min_delta += i
