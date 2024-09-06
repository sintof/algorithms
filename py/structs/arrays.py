from speed import timeit

arr = [10, 20, 30, 40, 50]
print(arr[0])

@timeit
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


@timeit
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


@timeit
def reverse_array(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr


print(linear_search(arr, 30))
print(binary_search(arr, 30))
print(reverse_array(arr))


# https://youtu.be/gDqQf4Ekr2A?si=NUteSmxphMP3yDnU - Arrays