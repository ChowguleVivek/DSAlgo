def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i
        while j > 0 and arr[j-1] > key:
            # print(l)
            # print("j ", j, "i ", i)
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = key
    return arr

if __name__ == "__main__":
    l = [3, 2, 6, 7, 1, 9, 34, 76, 12, 90, 65]
    print(insertion_sort(l))