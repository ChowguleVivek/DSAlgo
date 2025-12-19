def insertion_sort(arr):
    """
    Sort given array of size n
    Best Case: 
        No. of comparisions: (n-1)
        No. of swaps: 0
    Worst Case:
        No. of comaparisions: n * (n-1) / 2
        No. of swaps: n * (n-1) / 2

    parameters:
        arr: input array

    Returns:
        arr: sorted array
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i
        while j > 0 and arr[j-1] > key:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = key
    return arr

if __name__ == "__main__":
    l = [3, 2, 6, 7, 1, 9, 34, 76, 12, 90, 65]
    print(insertion_sort(l))