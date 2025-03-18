import time
import random


def insertionSort(array):
    preSort = time.perf_counter()
    count = 0
    length = len(array)

    for i in range(1, length, 1):
        current = array[i]
        lastElement = i - 1
        while lastElement >= 0 and array[lastElement] > current:
            array[lastElement + 1] = array[lastElement]
            count += 1
            lastElement -= 1
        array[lastElement + 1] = current
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

    result = insertionSort(array)
    isSorted(array)
    if (size <= 100):
        print(array, end="\n\n")

    print(result, end="\n\n")


if __name__ == "__main__":
    main()