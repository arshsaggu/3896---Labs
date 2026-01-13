def linear_search(needle, haystack):
    for index, number in enumerate(haystack):
        if number == needle:
            return index
        continue


needle = 5
haystack = [1, 2, 4, 5, 8]
print(linear_search(needle, haystack))


def binary_search(needle, haystack):
    sorted_haystack = sorted(haystack)
    low = 0
    high = len(sorted_haystack) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_haystack[mid] == needle:
            return mid
        elif needle < sorted_haystack[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return None


needle = 3
haystack = [1, 2, 3, 4]
print(binary_search(needle, haystack))