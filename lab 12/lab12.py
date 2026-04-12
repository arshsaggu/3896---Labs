def pivot_naive(seq):
    return seq[0]


def partition_naive(seq, pivot):
    less = [x for x in seq if x < pivot]
    equal = [x for x in seq if x == pivot]
    greater = [x for x in seq if x > pivot]
    return [less, equal, greater]


def quicksort_naive(seq):
    if len(seq) <= 1:
        return
    pivot = pivot_naive(seq)
    [less, equal, greater] = partition_naive(seq, pivot)
    quicksort_naive(less)
    quicksort_naive(greater)
    seq[:] = less + equal + greater


def pivot_upgrade(seq, lo, hi):
    return seq[lo]


def quicksort_upgrade(seq):
    __quicksort_upgrade(seq, 0, len(seq))


def __quicksort_upgrade(seq, lo, hi):
    if hi - lo <= 1:
        return
    pivot = pivot_upgrade(seq, lo, hi)
    [a, b, c] = partition_upgrade(seq, pivot, lo, hi)
    __quicksort_upgrade(seq, lo, lo + a)
    __quicksort_upgrade(seq, lo + a + b, hi)


def partition_upgrade(seq, pivot, lo, hi):
    insert_at = lo
    for i in range(lo, hi):
        if seq[i] < pivot:
            seq[i], seq[insert_at] = seq[insert_at], seq[i]
            insert_at += 1
    count_less = insert_at - lo

    for i in range(insert_at, hi):
        if seq[i] == pivot:
            seq[i], seq[insert_at] = seq[insert_at], seq[i]
            insert_at += 1
    count_equal = insert_at - lo - count_less

    count_greater = (hi - lo) - count_less - count_equal
    return [count_less, count_equal, count_greater]