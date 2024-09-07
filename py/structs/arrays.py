from utils.speed import timeit
from random import randint


arr = [10, 30, 20, 70, 40, 50]


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


@timeit
def find_max_min(arr):
    max_val, min_val = arr[0], arr[0]
    for num in arr[1:]:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    return max_val, min_val


@timeit
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


@timeit
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


@timeit
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        d = arr[i]
        k = i - 1
        while arr[k] > d and k >= 0:
            arr[k + 1] = arr[k]
            k -= 1
        arr[k + 1] = d

    return arr


@timeit
def merge_sort_fun(arr):
    def merge_sort(arr, left, right):
        if left >= right:
            return

        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        merge(arr, left, mid, right)

    def merge(arr, left, mid, right):
        left_copy = arr[left : mid + 1]
        right_copy = arr[mid + 1 : right + 1]

        l, r = 0, 0
        sc = left

        while l < len(left_copy) and r < len(right_copy):
            if left_copy[l] < right_copy[r]:
                arr[sc] = left_copy[l]
                l += 1
            else:
                arr[sc] = right_copy[r]
                r += 1
            sc += 1

        while l < len(left_copy):
            arr[sc] = left_copy[l]
            l += 1
            sc += 1

        while r < len(right_copy):
            arr[sc] = right_copy[r]
            r += 1
            sc += 1

    merge_sort(arr, 0, len(arr) - 1)
    return arr


def start():
    random_numbers = False
    to_print = True
    if random_numbers:
        arr = [randint(0, 100) for _ in range(1000)]
    else:
        arr = [10, 30, 20, 70, 40, 50]

    if to_print:
        print(linear_search(arr, 30))
        print(binary_search(arr, 30))
        print(reverse_array(arr))
        print(find_max_min(arr))
        print(bubble_sort(arr))
        print(selection_sort(arr))
        print(insertion_sort(arr))
        print(merge_sort_fun(arr))

    else:
        linear_search(arr, 30)
        binary_search(arr, 30)
        reverse_array(arr)
        find_max_min(arr)
        bubble_sort(arr)
        selection_sort(arr)
        insertion_sort(arr)
        merge_sort_fun(arr)


# https://youtu.be/gDqQf4Ekr2A?si=NUteSmxphMP3yDnU - Arrays
