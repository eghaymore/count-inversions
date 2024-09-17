import os

def merge_sort(arr):
    # base case
    if len(arr) <= 1:
        return arr

    # split down middle
    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    # recursion
    sortedLeft = merge_sort(leftHalf)
    sortedRight = merge_sort(rightHalf)

    # merge step
    global inversions
    result = []
    i = j = 0

    while i < len(sortedLeft) and j < len(sortedRight):
        if sortedLeft[i] <= sortedRight[j]:
            result.append(sortedLeft[i])
            i += 1
        else:
            result.append(sortedRight[j])
            inversions += len(sortedLeft) - i
            j += 1

    result.extend(sortedLeft[i:])
    result.extend(sortedRight[j:])

    return result

#
# main
#
inversions = 0
arr = []
script_dir = os.path.dirname(__file__)
# reading example-1
ex_one = open(os.path.join(script_dir, "example-1.txt"))
for num in ex_one:
    arr.append(int(num))
result = merge_sort(arr)
print("Inversion for example 1: ", inversions) #should be 28

# reading example-2
inversions = 0
arr = []
ex_two = open(os.path.join(script_dir, "example-2.txt"))
for num in ex_two:
    arr.append(int(num))
result = merge_sort(arr)
print("Inversion for example 2: ", inversions) #should be 2407905288