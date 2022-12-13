'''
Системный администратор раз в неделю создаёт архив пользовательских файлов.
Однако объём диска, куда он помещает архив, может быть меньше,
чем суммарный объём архивируемых файлов. Известно, какой объём занимает файл каждого пользователя.
Администратор отбирает файлы в архив таким образом, что в него будут сохранены файлы наибольшего
возможного количества пользователей.
'''

with open('26.txt') as f:
    s, n = map(int, f.readline().split())
    arr = sorted([int(i) for i in f])
    arr_copy = arr[:]
    test_arr = []
    ind = 0
    for i in range(len(arr)):
        if sum(test_arr) + arr[i] <= s:
            test_arr.append(arr[i])
            ind = i
        else:
            break

    arr = arr[ind + 1:]

    # выгодная замена, чтобы заполнить место по максимуму
    for i in range(len(test_arr) - 1, -1, -1):
        for j in range(len(arr)):
            if sum(test_arr) - test_arr[i] + arr[j] <= s:
                test_arr[i], arr[j] = arr[j], test_arr[i]
            else:
                break
        if sum(test_arr) == s:
            break

print(sum(test_arr), len([i for i in arr_copy if i > test_arr[-1]]))