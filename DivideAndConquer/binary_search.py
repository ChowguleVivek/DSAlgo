def binary_search(arr, key):
    start = 0
    end = len(arr)-1

    while start <= end:

        mid = (start+end) // 2
    
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid + 1
        elif arr[mid] > key:
            end = mid -1

    return -1

if __name__ == "__main__":
    l = [1, 2, 3, 6, 7, 9, 12, 34, 65, 76, 90]
    print(binary_search(l, 90))
    print(binary_search(l, 9))
    print(binary_search(l, 1))
    print(binary_search(l, 4))