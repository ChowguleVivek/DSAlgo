def merge(l1, l2):
    n = len(l1)
    m = len(l2)
    
    out = [0] * (m+n)
    i, j = 0, 0
    while i < n and j < m:
        if l1[i] <= l2[j]:
            out[i+j] = l1[i]
            i += 1
        else:
            out[i+j] = l2[j]
            j += 1
    
    if i < n:
        for k in range(i+j, m+n):
            out[k] = l1[i]
            i += 1
    if j < m: 
        for k in range(i+j, m+n):
            out[k] = l2[j]
            j += 1
    return out
    
def merge_sort(arr):
    def merge_sort_helper(arr, start, end):
        if start == end:
            return [arr[start]]
        elif end == start+1:
            if arr[start] >= arr[end]:
                return [arr[end], arr[start]]
            else:
                return [arr[start], arr[end]]
        else:
            l1 = merge_sort_helper(arr, start, (start + end) // 2)
            l2 = merge_sort_helper(arr, (start + end) // 2 + 1, end)
            out = merge(l1, l2)
            return out
    return merge_sort_helper(arr, 0, len(arr)-1)

if __name__ == "__main__":
    l1 = [5, 8, 23, 35, 46, 98, 204, 902, 950]
    l2 = [21, 32, 34, 54, 67, 89, 201, 303, 405, 501]
    l3 = [3, 6, 1, 8, 4, 89, 43, 56, 21, 12, 23, 79, 999, 24, 16]
    print(merge(l1, l2))
    print(l3)
    print(merge_sort(l3))