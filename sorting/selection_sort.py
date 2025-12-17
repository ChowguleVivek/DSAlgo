def selection_sort(arr):
    """
    Sort given array of size n
    Best Case: 
        No. of comparisions: n * (n-1) / 2
        No. of swaps: (n-1)
    Worst Case:
        No. of comaparisions: n * (n-1) / 2
        No. of swaps: (n-1)

    parameters:
        arr: input array

    Returns:
        arr: sorted array
    """
    for i in range(len(arr)):
        min_indx = i
        for j in range(i,len(arr)):
            if arr[j] < arr[min_indx]:
                min_indx = j
        arr[i], arr[min_indx] = arr[min_indx], arr[i]
    return arr

if __name__ == "__main__":
    l = [5, 8, 2, 33, 11, 76, 43, 12, 54, 90, 6, 27]
    print(selection_sort(l))