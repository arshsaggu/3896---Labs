def bubble_sort(seq):
    for j in range(len(seq) - 1, 0, -1):
        for i in range(0, j):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]


def selection_sort(seq):
    for i in range(len(seq)):
        min_index = i
        for j in range(i + 1, len(seq)):
            if seq[j] < seq[min_index]:
                min_index = j
        seq[i], seq[min_index] = seq[min_index], seq[i]


def insertion_sort(seq):
    for i in range(1, len(seq)):
        candidate = seq[i]
        j = i - 1
        while j >= 0 and seq[j] > candidate:
            seq[j + 1] = seq[j]
            j -= 1
        seq[j + 1] = candidate