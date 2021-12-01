import time, random, copy, sys

list_10 = [random.randint(1000, 1000000) for o in range(10)]
list_100 = [random.randint(1000, 1000000) for o in range(100)]
list_10000 = [random.randint(1000, 1000000) for o in range(10000)]
c = time.time()

Q_compCount = 0
Q_perCount = 0

def bubble_sort(lst):
    s = 0
    f = 0
    max_item = len(lst)
    for i in range(0, len(lst) - 1):
        max_item -= 1
        for j in range(0, max_item):
            f += 1
            if lst[j] > lst[j + 1]:
                s += 1
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    print('Кол-во перестановок: ', s)
    print('Кол-во сравнений: ', f)
    return lst

def sel_sort(lst):
    s = 0
    f = 0
    max_item = lst[0]
    l_item = len(lst)
    for i in range(0, len(lst)):
        l_item -= 1
        max_ID = 0

        for j in range(0, l_item + 1):
            f += 1
            if max_item < lst[j]:
                max_ID = j
                max_item = lst[j]
            if j == l_item:
                s += 1
                lst[j], lst[max_ID] = lst[max_ID], lst[j]

        max_item = lst[0]
    print('Кол-во перестановок: ', s)
    print('Кол-во сравнений: ', f)
    return lst

def insert_sort(lst):
    s = 0
    f = 0
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j - 1] > lst[j]:
            lst[j - 1], lst[j] = lst[j], lst[j - 1]
            s += 1
            f += 1
            j -= 1

    print('Кол-во перестановок: ', s)
    print('Кол-во сравнений: ', f)
    return lst

def Shell_sort(lst):
    s = 0
    f = 0
    last_ID = len(lst) - 1
    step = len(lst) // 2
    while step > 0:
        for i in range(step, last_ID + 1, 1):
            j = i
            delta = j - step
            while delta >= 0 and lst[delta] > lst[j]:
                s += 1
                f += 1
                lst[delta], lst[j] = lst[j], lst[delta]
                j = delta
                delta = j - step
        step //= 2
    print('Кол-во перестановок: ', s)
    print('Кол-во сравнений: ', f)
    return lst

def quick_sort(lst):
    global Q_perCount, Q_compCount
    less = []
    equal = []
    more = []
    if len(lst) <= 1:
        return lst
    else:
        mid = lst[0]
        for i in lst:
            Q_compCount += 1
            if i < mid:
                less.append(i)
            elif i > mid:
                more.append(i)
            elif i == mid:
                equal.append(i)

        Q_perCount += 2
        return quick_sort(less) + equal + quick_sort(more)


print(" ")
print("Вставка")
print('Старый список из 10 элементов: ', list_10)
list = list_10.copy()
c = time.time()
insert_sort(list)
deltaTime = time.time() - c
print('Отсортированный список: ', list)
print('Время выполнения программы: ', deltaTime)

print(" ")
print('Старый список из 100 элементов: ', list_100)
list = list_100.copy()
c = time.time()
insert_sort(list)
deltaTime = time.time() - c
print('Отсортированный список: ', list)
print('Время выполнения программы: ', deltaTime)

print(" ")
print('Старый список из 10000 элементов: ', list_10000)
list = list_10000.copy()
c = time.time()
insert_sort(list)
deltaTime = time.time() - c
print('Отсортированный список: ', list)
print('Время выполнения программы: ', deltaTime)


# =============================

print(" ")
print("Сортирровка пузырьком")
print('Старый список из 10 элементов: ', list_10)
list = list_10.copy()
c = time.time()
bubble_sort(list)
deltaTime = time.time() - c
print('Отсортированный список: ',list)
print('Время выполнения программы: ', deltaTime)

print('Старый список из 100 элементов: ', list_100)
list = list_100.copy()
c = time.time()
bubble_sort(list)
deltaTime = time.time() - c
print('Отсортированный список: ',list)
print('Время выполнения программы: ', deltaTime)

print('Старый список из 10000 элементов: ', list_10000)
list = list_10000.copy()
c = time.time()
bubble_sort(list)
deltaTime = time.time() - c
print('Отсортированный список: ',list)
print('Время выполнения программы: ', deltaTime)

# =============================

print(" ")
print("Сортирровка выбором")
print('Старый список из 10 элементов: ', list_10)
list = list_10.copy()
c = time.time()
sel_sort(list)
deltaTime = time.time() - c
print('Отсортированный список: ',list)
print('Время выполнения программы: ', deltaTime)

print('Старый список из 100 элементов: ', list_100)
list = list_100.copy()
c = time.time()
sel_sort(list)
deltaTime = time.time() - c
print('Отсортированный список: ',list)
print('Время выполнения программы: ', deltaTime)

print('Старый список из 10000 элементов: ', list_10000)
list = list_10000.copy()
c = time.time()
sel_sort(list)
deltaTime = time.time() - c
print('Отсортированный список: ',list)
print('Время выполнения программы: ', deltaTime)

# =============================

print(" ")
print("Сортирровка Шелла")
print('Старый список из 10 элементов: ', list_10)
list = list_10.copy()
c = time.time()
Shell_sort(list)
deltaTime = time.time() - c
print('Отсортированный список: ',list)
print('Время выполнения программы: ', deltaTime)

print('Старый список из 100 элементов: ', list_100)
list = list_100.copy()
c = time.time()
Shell_sort(list)
deltaTime = time.time() - c
print('Отсортированный список: ',list)
print('Время выполнения программы: ', deltaTime)

print('Старый список из 10000 элементов: ', list_10000)
list = list_10000.copy()
c = time.time()
Shell_sort(list)
deltaTime = time.time() - c
print('Отсортированный список: ',list)
print('Время выполнения программы: ', deltaTime)

# ==================================

print(" ")
print("Быстрая сортировка")
print('Старый список из 10 элементов: ', list_10)
list = list_10.copy()
c = time.time()
list = quick_sort(list)
deltaTime = time.time() - c
print('Количество перестановок', Q_perCount)
print('Количество сравнений', Q_compCount)
Q_perCount = 0
Q_compCount = 0
print('Отсортированный список: ',list)
print('Время выполнения программы: ', deltaTime)

print('Старый список из 100 элементов: ', list_100)
list = list_100.copy()
c = time.time()
list = quick_sort(list)
deltaTime = time.time() - c
print('Количество перестановок', Q_perCount)
print('Количество сравнений', Q_compCount)
Q_perCount = 0
Q_compCount = 0
print('Отсортированный список: ',list)
print('Время выполнения программы: ', deltaTime)

print('Старый список из 10000 элементов: ', list_10000)
list = list_10000.copy()
c = time.time()
list = quick_sort(list)
deltaTime = time.time() - c
print('Количество перестановок', Q_perCount)
print('Количество сравнений', Q_compCount)
Q_perCount = 0
Q_compCount = 0
print('Отсортированный список: ',list)
print('Время выполнения программы: ', deltaTime)