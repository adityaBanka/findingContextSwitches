import time
import random


def selectionSort(array):

    preSort = time.perf_counter()
    count = 0
    length = len(array)

    for i in range(0, length, 1):
        small = i
        for j in range(i, length, 1):
            if (array[j] < array[small]):
                small = j
        array[i], array[small] = array[small], array[i]
        count += 1

    postSort = time.perf_counter()
    return (postSort - preSort, count)


def sort(array):
    return (selectionSort(array))


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

    result = selectionSort(array)
    isSorted(array)
    if (size <= 100):
        print(array, end="\n\n")

    print(result, end="\n\n")


if __name__ == "__main__":
    main()