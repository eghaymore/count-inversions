#Count inversion
#Sam Collins
#Needs a file named "test_1.txt" to run. Each integer must be placed in its own line.

# Function to merge two halves and count inversions
def merge_and_count_inversions(array, temp_array, left, mid, right):
    i = left    # Starting index for the left subarray
    j = mid + 1 # Starting index for the right subarray
    k = left    # Starting index for the sorted array
    inversion_count = 0

    while i <= mid and j <= right:
        if array[i] <= array[j]:
            temp_array[k] = array[i]
            i += 1
        else:
            temp_array[k] = array[j]
            inversion_count += (mid - i + 1) # Count inversions
            j += 1
        k += 1
    while i <= mid:
        temp_array[k] = array[i]
        i += 1
        k += 1
    while j <= right:
        temp_array[k] = array[j]
        j += 1
        k += 1
    for i in range(left, right + 1):
        array[i] = temp_array[i]

    return inversion_count

# Function to perform merge sort and count inversions
def sort_and_count_inversions(array, temp_array, left, right):
    if left >= right:
        return 0

    mid = (left + right) // 2

    left_inversions = sort_and_count_inversions(array, temp_array, left, mid)
    right_inversions = sort_and_count_inversions(array, temp_array, mid + 1, right)
    merge_inversions = merge_and_count_inversions(array, temp_array, left, mid, right)

    return left_inversions + right_inversions + merge_inversions

# Function to initiate sorting and inversion counting
def count_inversions(array):
    n = len(array)
    temp_array = [0] * n
    return sort_and_count_inversions(array, temp_array, 0, n - 1)

# Function to load the array from a text file
def load_array_from_file(filename):
    array = []
    with open(filename, 'r') as file:
        for line in file:
            array.append(int(line.strip()))  # Read each line as an integer
    return array

# Main
if __name__ == "__main__":
    filename = "test_1.txt"
    array = load_array_from_file(filename)
    result = count_inversions(array)
    print(f"Number of inversions in {filename}: {result}")
