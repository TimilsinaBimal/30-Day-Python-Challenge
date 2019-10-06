# During the last week track of training,
# Shoshanna achieves the following times in sec
# rounds - 66, 57, 54, 53, 64, 52, 59
# Found her best score using bubble sort


def bubbleSort(arr):
    bestFigure = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if(arr[j] > arr[j+1]):
                bestFigure = arr[j]
                arr[j+1] = arr[j]
                arr[j] = arr[j + 1]
            else:
                bestFigure = arr[j+1]
    return bestFigure


rounds = [66, 57, 54, 53, 64, 52, 59]
print(f"The best score of Shoshanna is:  {bubbleSort(rounds)}")
