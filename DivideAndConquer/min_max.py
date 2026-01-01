def min_max(arr):
    """
    parameters:
        arr: input array
    returns:
        2D tuple: 
            first elm: min val from array
            second elm: max val from array
    """
    mini = maxi = arr[0]
    for i in range(len(arr)):
        if arr[i] < mini:
            mini = arr[i]
        elif arr[i] > maxi:
            maxi = arr[i]
    return mini, maxi

if __name__ == "__main__":
    l = [4, 6, 1, 9, 37, 82, 30, 88, 23, 64, 90]
    print(min_max.__doc__)
    print(min_max(l))