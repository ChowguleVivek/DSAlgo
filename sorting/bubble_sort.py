def bubble_sort(arr):
    """
    Sort given array of size n
    Best Case: 
        No. of comparisions: (n-1)^2
        No. of swaps: 0
    Worst Case:
        No. of comaparisions: (n-1)^2
        No. of swaps: n * (n-1) / 2

    parameters:
        arr: input array

    Returns:
        arr: sorted array
    """
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    l = [2, 5, 6, 14, 37, 45, 4, 7, 23, 89, 62, 34]
    print(bubble_sort(l))