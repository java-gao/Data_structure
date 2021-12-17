
def get_next(string):
    i = 0
    j = -1
    next_array = [None for i in range(len(string))]
    next_array[0] = -1
    while i < len(string) - 1:
        if j == -1 or string[i] == string[j]:
            i += 1
            j += 1
            next_array[i] = j
        else:
            j = next_array[j]
    return next_array


def index_kmp(sub_string, string, pos):
    i = pos
    j = 0
    next_array = get_next(sub_string)
    print(next_array)
    while i < len(string) and j < len(sub_string):
        print(i)
        print(j)
        if j == -1 or string[i] == sub_string[j]:
            i += 1
            j += 1
        else:
            j = next_array[j]

        print('--------------')
    if j > len(sub_string) - 1:
        return i - len(sub_string)
    else:
        return -1


t = 'abcabc'
a = index_kmp(t, 'cabcabc', 0)
print(a)
