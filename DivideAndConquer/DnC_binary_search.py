def binary_search(arr, key, start, end):
    if start == end:
        if arr[start] == key:
            return start
    elif start > end:
        return -1
    else:

        mid = (start + end) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search(arr, key, start, mid-1)
        else:
            return binary_search(arr, key, mid+1, end)

if __name__ == "__main__":
    l = [1, 2, 3, 6, 7, 9, 12, 34, 65, 76, 90]
    print(binary_search(l, 90, 0, len(l)-1))
    print(binary_search(l, 9, 0, len(l)-1))
    print(binary_search(l, 1, 0, len(l)-1))
    print(binary_search(l, 4, 0, len(l)))
