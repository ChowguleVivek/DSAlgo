def dnc_min_max(arr):
    """
    given an array of size n
    Best Case: 
        total: (3n/2 - 2)
    Worst Case:
        total: (3n/2 - 2)
    Average Case:
        total: (3n/2 - 2)

    parameters:
        arr: input array
    returns:
        2D tuple: 
            first elm: min val from array
            second elm: max val from array
    """
    def dnc(arr, i, j):
        if i == j:
            return arr[i], arr[i]
        if i == j-1:
            if arr[i] > arr[j]:
                return arr[j], arr[i]
            else:
                return arr[i], arr[j]
        else:
            mid = (i+j) // 2
            min1, max1 = dnc(arr, i, mid)
            min2, max2 = dnc(arr, mid+1, j)
            mini = min(min1, min2)
            maxi = max(max1, max2)
            return mini, maxi
    return dnc(arr, 0, len(arr)-1)

if __name__ == "__main__":
    l = [4, 6, 1, 9, 37, 82, 30, 88, 23, 64, 90]
    print(dnc_min_max.__doc__)
    print(dnc_min_max(l))