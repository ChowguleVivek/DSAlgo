def bubble_sort(arr):
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
    for i in range(len(arr) - 1):
        flag = 0
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = 1
        if flag == 0:
            return arr
    return arr

if __name__ == "__main__":
    l = [3, 5, 1 , 8, 2, 6, 90, 356, 23, 54, 67]
    print(bubble_sort(l))