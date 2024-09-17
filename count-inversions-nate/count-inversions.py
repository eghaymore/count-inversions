import os

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = merge_sort(leftHalf)
    sortedRight = merge_sort(rightHalf)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    global inversions
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            inversions += len(left) - i
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

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