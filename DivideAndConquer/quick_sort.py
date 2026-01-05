def partition(arr, m, p):
    i, j = m, p 
    first = arr[m]
    while i <= j:
        if arr[i] <= first:
            i += 1
        elif arr[j] >= first:
            j -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    temp = arr[j]
    arr[j] = first
    arr[m] = temp
    return j

def quick_sort(arr):
    def quick_sort_helper(arr, m, n):
        if m == n:
            return
        elif m == n-1:
            if arr[m] > arr[n]:
                arr[m], arr[n] = arr[n], arr[m]
        else:
            j = partition(arr, m, n)
            # print(arr[m:n+1])
            if j > m:
                quick_sort_helper(arr, m, j-1)
            if j < n:
                quick_sort_helper(arr, j+1, n)
    quick_sort_helper(arr, 0, len(arr)-1)
    return arr


if __name__ == "__main__":
    l = [65, 70, 75, 80, 60, 55, 50, 45, 9999]
    l2 = [1, 2, 3, 4, 5, 6, 7]
    l3 = l2[::-1] 
    print(l3)
    print(partition(l, 0, len(l)-1), l)
    print(partition(l2, 0, len(l2)-1), l2)
    print(partition(l3, 0, len(l3)-1), l3)
    print("*"*15, '>', "after quick sort", '<', '*'*15)
    print("l", quick_sort(l))
    print('l2', quick_sort(l2))
    print("l3", quick_sort(l3))