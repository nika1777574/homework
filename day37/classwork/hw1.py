


def my_len(x):
    n = 0
    for _ in x: n += 1
    return n


def my_insert(lst, idx, val):
    lst.append(val)
    i = my_len(lst) - 1
    while i > idx:
        lst[i], lst[i-1] = lst[i-1], lst[i]
        i -= 1
    return lst

def my_range(start, stop, step):
    if step == 0: return []
    r, i = [], start
    while (i < stop if step > 0 else i > stop):
        r.append(i)
        i += step
    return r