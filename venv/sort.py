def bubble_sort(data):
    flag = 0
    for i in range(len(data)):
        if flag == 1 and i > 0:
            break
        for j in range(len(data) - 1, i, -1):
            if data[j] < data[j - 1]:
                flag = 0
                temp = data[j]
                data[j] = data[j - 1]
                data[j - 1] = temp


def select_sort(data):
    for i in range(len(data)):
        min = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min]:
                min = j
        if min != i:
            temp = data[i]
            data[i] = data[min]
            data[min] = temp


def insert_sort(data):
    for i in range(1, len(data)):
        elem = data[i]
        location = i - 1
        if data[i] < data[i - 1]:
            while location > -1:
                if data[location] > elem:
                    data[location + 1] = data[location]
                else:
                    break
                location -= 1
            data[location + 1] = elem


def shell_sort(data):
    increment = len(data)
    while increment > 1:
        increment = increment // 3 + 1
        for i in range(increment, len(data)):
            elem = data[i]
            location = i - increment
            if elem < data[i - increment]:
                while location > -1:
                    if data[location] > elem:
                        data[location + increment] = data[location]
                    else:
                        break

                    location -= increment
                data[location + increment] = elem
        print(data)
        print(increment)


def heap_adjust(data, s, m):
    j = 2 * s
    temp = data[s]
    while j <= m:
        if j < m and data[j] < data[j + 1]:
            j += 1
        if temp >= data[j]:
            break
        data[s] = data[j]
        s = j
        j = j * 2

    data[s] = temp


def heap_sort(data):
    for i in range((len(data) - 1) // 2, 0, -1):
        print(i)
        heap_adjust(data, i, len(data) - 1)
    print(data)
    for i in range(len(data) - 1, 0, -1):
        temp = data[1]
        data[1] = data[i]
        data[i] = temp
        heap_adjust(data, 1, i - 1)


def merge(sr, tr, s, m, n):
    i = s
    j = m + 1
    k = s
    while i <= m and j <= n:
        if sr[i] < sr[j]:
            tr[k] = sr[i]
            i += 1
        else:
            tr[k] = sr[j]
            j += 1
        k += 1

    if i <= m:
        for a in range(i, m + 1):
            tr[k] = sr[a]
            k += 1

    if j <= n:
        for b in range(j, n + 1):
            tr[k] = sr[b]
            k += 1


def msort(sr, tr1, s, t):
    tr2 = [0] * 10
    if s == t:
        # print(s)
        tr1[s] = sr[s]
    else:
        m = (s + t) // 2
        msort(sr, tr2, s, m)
        # print('tr2', tr2)
        msort(sr, tr2, m + 1, t)
        # print('tr2', tr2)
        merge(tr2, tr1, s, m, t)
        # print('tr1', tr1)


def merge_sort(data):
    data1 = data.copy()
    msort(data, data1, 0, len(data) - 1)
    print(data1)


def merge_pass(data, tr, s, n):
    i = 0
    while i <= n - 2 * s + 1:
        merge(data, tr, i, i + s - 1, i + 2 * s - 1)
        i = i + 2 * s

    if i < n - s + 1:
        merge(data, tr, i, i + s - 1, n)
    else:
        for j in range(i, n + 1):
            tr[j] = data[j]


def merge_sort2(data):
    rt = [0] * 10
    k = 1
    while k < len(data):
        merge_pass(data, rt, k, len(data) - 1)
        k = k * 2
        merge_pass(rt, data, k, len(data) - 1)
        k = k * 2
    print(data)


def partition(data, low, high):
    pivotkey = data[low]
    while low < high:
        while low < high and data[high] >= pivotkey:
            high -= 1
        temp = data[low]
        data[low] = data[high]
        data[high] = temp
        while low < high and data[low] <= pivotkey:
            low += 1
        temp = data[low]
        data[low] = data[high]
        data[high] = temp
    return low


def qsort(data, low, high):
    if low < high:
        pivot = partition(data, low, high)
        qsort(data, low, pivot - 1)
        qsort(data, pivot + 1, high)


def quick_sort(data):
    qsort(data, 0, len(data)-1)
