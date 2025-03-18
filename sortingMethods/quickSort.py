import time
import random


def partition_for_quickSort(array, low, high):
    pivot_index = random.randint(low, high)
    array[pivot_index], array[high] = array[high], array[pivot_index]
    pivot = array[high]

    count = 0
    i = low - 1
    for j in range(low, high):
        if (array[j] <= pivot):
            i += 1
            array[i], array[j] = array[j], array[i]
            count += 1
    array[i + 1], array[high] = array[high], array[i + 1]
    count += 1
    return (count, i + 1)


def quickSort(array, low, high):
    preSort = time.perf_counter()
    count = 0
    if high-low > 1:
        count, pivot = partition_for_quickSort(array, low, high)
        res = quickSort(array, low, pivot - 1)
        count += res[1]
        res = quickSort(array, pivot + 1, high)
        count += res[1]
    postSort = time.perf_counter()
    return (postSort - preSort, count)

def sort(array):
    return quickSort(array, low = 0, high = len(array) - 1)

def isSorted(array):
    length = len(array)
    for i in range(0, length-1):
        if (array[i + 1] < array[i]):
            print("List is NOT SORTED\n")
            return
    print("List is SORTED\n")


def main():
    size = int(input("Enter the size of arary to be sorted: "))
    array = []
    for i in range(0, size):
        array.append(random.randint(1, (size+1)//2))

    isSorted(array)
    if (size <= 100):
        print(array, end="\n\n")

    result = quickSort(array, 0, size-1)
    isSorted(array)
    if (size <= 100):
        print(array, end="\n\n")

    print(result, end="\n\n")


if __name__ == "__main__":
    main()