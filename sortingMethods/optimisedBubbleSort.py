import time
import random

def optimisedBubbleSort(array):

    preSort = time.perf_counter()
    count = 0
    length = len(array)

    for i in range(0, length, 1):
        swapped = False
        for j in range(0, length-i-1, 1):
            if (array[j+1] < array[j]):
                swapped = True
                array[j+1], array[j] = array[j], array[j+1]
                count += 1

        if swapped == False:
            postSort = time.perf_counter()
            return (postSort - preSort, count)

    postSort = time.perf_counter()
    return (postSort - preSort, count)


def isSorted(array):
    length = len(array)
    for i in range(0, length-1, 1):
        if (array[i + 1] < array[i]):
            print("List is NOT SORTED")
            return
    print("List is SORTED")


def main():
    size = int(input("Enter the size of arary to be sorted: "))
    array = []
    for i in range(0, size):
        array.append(random.randint(1, (size+1)//2))

    isSorted(array)
    if (size <= 100):
        print(array, end="\n\n")

    result = optimisedBubbleSort(array)
    isSorted(array)
    if (size <= 100):
        print(array, end="\n\n")

    print(result, end="\n\n")


if __name__ == "__main__":
    main()