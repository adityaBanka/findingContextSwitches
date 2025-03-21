import time
import random
import concurrent.futures
import multiprocessing
import matplotlib.pyplot as plt
import numpy as np

from sortingMethods.bubbleSort import bubbleSort
from sortingMethods.optimisedBubbleSort import optimisedBubbleSort
from sortingMethods.selectionSort import selectionSort
from sortingMethods.doubleSelectionSort import doubleSelectionSort
from sortingMethods.insertionSort import insertionSort
from sortingMethods.quickSort import qsort as quickSort


class attributes:
    def __init__(self):  # default configuration to run all sorting techniques 5 times to geenerate a single graph
        self.minCores = multiprocessing.cpu_count()
        self.maxCores = multiprocessing.cpu_count()
        self.coreUpdateSize = 1
        self.coreTestSize = 1
        self.minArraySize = 100
        self.maxArraySize = 5000
        self.arrayUpdateSize = 100
        self.processTestSize = 5
        self.sortingOptions = "012345"

    def set_default_parallel(self, minArraySize, maxArraySize, arrayUpdateSize, processTestSize, sortingOptions):
        self.minCores = multiprocessing.cpu_count()
        self.maxCores = multiprocessing.cpu_count()
        self.coreUpdateSize = 1
        self.coreTestSize = 1
        self.minArraySize = minArraySize
        self.maxArraySize = maxArraySize
        self.arrayUpdateSize = arrayUpdateSize
        self.processTestSize = processTestSize
        self.sortingOptions = sortingOptions

    def set_default_multiProcess(self, minCores, maxCores, coreUpdateSize, coreTestSize, sortingOptions):
        self.minCores = minCores
        self.maxCores = maxCores
        self.coreUpdateSize = coreUpdateSize
        self.coreTestSize = coreTestSize
        self.minArraySize = 1000
        self.maxArraySize = 5000
        self.arrayUpdateSize = 50
        self.processTestSize = 5
        self.sortingOptions = sortingOptions

    def set_custom(self, minCores, maxCores, coreUpdateSize, coreTestSize, minArraySize, maxArraySize, arrayUpdateSize,
                   processTestSize, sortingOptions):
        self.minCores = minCores
        self.maxCores = maxCores
        self.coreUpdateSize = coreUpdateSize
        self.coreTestSize = coreTestSize
        self.minArraySize = minArraySize
        self.maxArraySize = maxArraySize
        self.arrayUpdateSize = arrayUpdateSize
        self.processTestSize = processTestSize
        self.sortingOptions = sortingOptions


def plot_results(results):
    plt.figure(figsize=(12, 6))

    # Plot 1
    plt.subplot(1, 2, 1)
    for func_name, data in results.items():
        plt.plot(data['size'], data['time'], label=func_name,
                 linewidth=1, marker=".", markersize=5)
    plt.xlabel('Array Size')
    plt.ylabel('Time Taken')
    plt.title('Plot 1: Size vs Time Taken')
    plt.legend()
    plt.grid(True, linestyle="dashed")

    # Plot 2
    plt.subplot(1, 2, 2)
    for func_name, data in results.items():
        plt.plot(data['size'], data['swap'], label=func_name,
                 linewidth=1, marker=".", markersize=2)
    plt.xlabel('Array Size')
    plt.ylabel('Number of Swaps')
    plt.title('Plot 2: Size vs Number of Swaps')
    plt.legend()

    plt.tight_layout()
    plt.grid(True, linestyle="dashed")
    plt.show()


def main(numeber_of_workers, testingMode="default"):
    preTime = time.perf_counter()

    if (testingMode == "default"):
        functions = [bubbleSort, optimisedBubbleSort, selectionSort,
                     doubleSelectionSort, insertionSort, quickSort]
    elif (testingMode == "test"):
        functions = [selectionSort]
    else:
        functions = [bubbleSort, optimisedBubbleSort]

    executor = concurrent.futures.ProcessPoolExecutor(
        max_workers=numeber_of_workers)
    futures = {}
    results = {func.__name__: {'size': [], 'time': [], 'swap': []}
               for func in functions}
    # results = {}

    limit = [1000, 10001, 100]
    if (testingMode == "default"):
        limit = [100, 5001, 50]

    for size in range(limit[0], limit[1], limit[2]):
        array = []
        for i in range(1, size, 1):
            array.append(random.randint(1, size))

        for func in functions:
            future = executor.submit(func, array.copy())
            futures[future] = (func.__name__, size)

    for future in concurrent.futures.as_completed(futures):
        func_name, size = futures[future]
        result = future.result()
        if (testingMode == "default"):
            print(f"{size}\t{result}\t{func_name}")
        part1, part2 = future.result()
        results[func_name]['size'].append(size)
        results[func_name]['time'].append(part1)
        results[func_name]['swap'].append(part2)

        # func_name, size = futures[future]
        # #result = future.result()
        # part1, part2 = future.result()
        # if( (func_name, size) is not results.keys()):
        #     results[func_name, size] = []
        # results[(func_name, size)].append((part1, part2))

        # # if((func_name, size) is results.keys()):
        # #     results[(func_name, size)][0] += part1
        # #     results[(func_name, size)][1] += part2
        # # else:
        # #     results[(func_name, size)].append(part1, part2)

        # # results[func_name]['size'].append(size)
        # # results[func_name]['time'].append(part1)
        # # results[func_name]['swap'].append(part2)
        # print(f"{size}\t{results[(func_name, size)][0][0]}\t{func_name}")

    executor.shutdown()
    postTime = time.perf_counter()
    if (testingMode == "default"):
        print(postTime - preTime)
        plot_results(results)
    return (postTime - preTime)


def testing():  # done to see the point of diminishing returns of using more cores with selection sort

    cores = []
    timeTaken = []

    minCore = 14
    maxCore = 24
    number_of_tests = 3

    for i in range(minCore, maxCore, 1):
        cores.append(i)
        print(i, end="\t")
        currentTime = 0

        for j in range(0, number_of_tests, 1):
            localTime = main(i, "test")
            currentTime += localTime
            print(localTime, end=" ")

        currentTime /= number_of_tests

        timeTaken.append(currentTime)
        print(currentTime)

    plt.plot(cores, timeTaken)
    plt.show()


if __name__ == "__main__":

    textInput = input("Enter what are we doing today? ")
    if textInput == "test":
        testing()
    elif textInput == "main":
        # main(61)
        main(multiprocessing.cpu_count() - 2)


def internalFunction(test: attributes):
    functions = [bubbleSort, optimisedBubbleSort, selectionSort, doubleSelectionSort, insertionSort, quickSort]

    # results = {function.__name__: {'size': [], 'time': [], 'swap': []}
    #            for function in functions}
    results = {}

    testNumber = 0
    while (testNumber <= test.processTestSize):
        executor = concurrent.futures.ProcessPoolExecutor(max_workers=test.coreTestSize)
        futures = {}
        arraySize = test.minArraySize
        while (arraySize <= test.maxArraySize):
            array = [random.randint(1, (arraySize + 1) // 2) for i in range(arraySize + 1)]
            for function in functions:
                future = executor.submit(function, array.copy())
                futures[future] = (fucntion.__name__, arraySize)
            arraySize += test.updateArray

            for future in concurrent.futures.as_completed(futures):
                func_name, size = futures[future]
                # result = future.result()
                part1, part2 = future.result()

                if ((func_name, size) is results.keys()):
                    results[(func_name, size)][0] += part1
                    results[(func_name, size)][1] += part2
                else:
                    results[(func_name, size)] = (part1, part2)
                # results[func_name]['size'].append(size)
                # results[func_name]['time'].append(part1)
                # results[func_name]['swap'].append(part2)

        testNumber += 1


def fucntion(test: attributes):
    coreCount = test.minCores
    while (coreCount <= test.maxCores):
        preTime = time.perf_counter()



