# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []
    i = 0
    j = 0
    while i < len(arrA) and j < len(arrB):
        if(arrA[i] > arrB[j]):
            merged_arr.append(arrB[j])
            j += 1
        else:
            merged_arr.append(arrA[i])
            i += 1

    if i < len(arrA):
        merged_arr.extend(arrA[i:len(arrA)])
    elif j < len(arrB):
        merged_arr.extend(arrB[j:len(arrB)])

    return merged_arr


# print(merge([0, 1, 2], [1, 2, 5, 30]))

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):

    # base case

    print(arr)
    if len(arr) <= 1:
        return arr

    mid = (len(arr)//2)  # the double slash floors the length
    arr1 = arr[0:mid]
    arr2 = arr[mid:]

    return merge(merge_sort(arr1), merge_sort(arr2))

    # print("arr: ", arr)


print(merge_sort([4, 2, 5, 1]))
