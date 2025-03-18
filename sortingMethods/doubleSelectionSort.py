import time
import random


def doubleSelectionSort(array):

    preSort = time.perf_counter()
    count = 0
    length = len(array)

    for i in range(0, length//2, 1):
        small = i
        big = i
        for j in range(i, length-i, 1):
            if (array[j] < array[small]):
                small = j
            elif (array[j] > array[big]):
                big = j
        array[i], array[small] = array[small], array[i]
        count += 1
        if (big == i):
            big = small
        array[length - i - 1], array[big] = array[big], array[length - i - 1]
        count += 1

    postSort = time.perf_counter()
    return (postSort - preSort, count)


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

    result = doubleSelectionSort(array)
    isSorted(array)
    if (size <= 100):
        print(array, end="\n\n")

    print(result, end="\n\n")


if __name__ == "__main__":
    main()