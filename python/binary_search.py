def normal_binary_search(val, arr, left_ptr, right_ptr):
    """
        Normal binary search

    >>> normal_binary_search(2, [1,2,3,33, 44], 0, 4)
    1


    >>> normal_binary_search(3, [1,2,3,33, 44], 0, 4)
    2
    >>> normal_binary_search(4, [1,2,3,33, 44], 0, 4)
    -1
    """
    while left_ptr < right_ptr:
        middle_ptr = (left_ptr + right_ptr) // 2

        if arr[middle_ptr] == val:
            return middle_ptr
        elif arr[middle_ptr] > val:
            right_ptr = middle_ptr
        else:
            left_ptr = middle_ptr + 1

    return -1


def lb_binary_search(val, arr, left_ptr, right_ptr):
    # TODO : add this
    pass


def ub_binary_search(val, arr, left_ptr, right_ptr):
    # TODO : add this
    pass
