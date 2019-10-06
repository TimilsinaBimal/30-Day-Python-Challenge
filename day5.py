# During the last week track of training,
# Shoshanna achieves the following times in sec
# rounds - 66, 57, 54, 53, 64, 52, 59
# Found her best score using bubble sort


def bubbleSort(arr):
    bestFigure = 0
    n = len(arr)
    for i in range(n-1):
        if(arr[i] > arr[i+1]):
            bestFigure = arr[i]
            arr[i+1] = arr[i]
        else:
            bestFigure = arr[i+1]
    return bestFigure


rounds = [66, 57, 54, 53, 64, 52, 59]
print(f"The best score of Shoshanna is:  {bubbleSort(rounds)}")
