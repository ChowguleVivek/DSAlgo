def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    l = [2, 5, 6, 14, 37, 45, 4, 7, 23, 89, 62, 34]
    print(bubble_sort(l))