# TO-DO: Complete the selection_sort() function below


def swap(arr, idx1, idx2):
    temp = arr[idx1]
    arr[idx1] = arr[idx2]
    arr[idx2] = temp
    return arr


def selection_sort(arr):
    for i in range(0, len(arr)):
        cur_idx = i
        min_idx = cur_idx
        for j in range(i, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
            j += 1
        swap(arr, min_idx, i)
        i += 1
    return arr

# take i, compare it to the thing next to it,


def bubble_sort(arr):
    for i in range(0, len(arr)-1):
        no_swap=False
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)
                no_swap=True
            j += 1
        i += 1
    return arr


print("bubble sort: [0, 3, 5, 2, 1, 8, 6, 9, 4, 7]", bubble_sort(
    [0, 3, 5, 2, 1, 8, 6, 9, 4, 7]))

# TO-DO:  implement the Bubble Sort function below


# # STRETCH: implement the Count Sort function below
# def count_sort(arr, maximum=-1):

#     return arr
