def merge_sort(lst):
    if len(lst) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(lst) // 2
        left = lst[:r]
        right = lst[r:]

        # Sort the two halves
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Until we reach either end of either left or right, pick larger among
        # elements left and right and place them in the correct position at A[p..r]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        # When we run out of elements in either left or right,
        # pick up the remaining elements and put in A[p..r]
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1


if __name__ == '__main__':
    # array = [6, 5, 12, 10, 9, 1]
    array = list(map(int, input().split()))
    merge_sort(array)
    print(*array)
