def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    l = [3, 2, 6, 7, 1, 9, 34, 76, 12, 90, 65]
    print(bubble_sort(l))