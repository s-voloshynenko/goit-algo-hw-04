import timeit
import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1

        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        
        lst[j + 1] = key
    return lst

def timsort(lst):
    return sorted(lst)

def generate_array(size):
    return [random.randint(0, 10000) for _ in range(size)]

def measure_time(array, sort_algo):
    time = timeit.timeit(lambda: sort_algo(array.copy()), number=10)
    print(f"Sort time of {sort_algo.__name__} for {len(array)} size array is {time:.6f} secs.")

sizes = [100, 1000, 5000, 10000]

def main():
    for size in sizes:
        array = generate_array(size)
        print(f"\nArray size: {size}")
        measure_time(array, merge_sort)
        measure_time(array, insertion_sort)
        measure_time(array, timsort)

if __name__ == "__main__":
    main()
