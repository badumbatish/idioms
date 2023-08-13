def normal_binary_search(val, arr, left_ptr, right_ptr):
    """
        Normal binary search

    >>> normal_binary_search(2, [1,2,3,33, 44], 0, 4)
    1


    >>> normal_binary_search(3, [1,2,3,33, 44], 0, 4)
    2
    >>> normal_binary_search(4, [1,2,3,33, 44], 0, 4)
    -1
    >>> normal_binary_search(4, [], 0, 0)
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
    """
        Lower bound binary search

    >>> lb_binary_search(2, [1,2,2,2, 3,33], 0, 5)
    1


    >>> lb_binary_search(2, [], 0, 0)
    0
    """
    while left_ptr < right_ptr:
        middle_ptr = (left_ptr + right_ptr) // 2

        if arr[middle_ptr] < val:
            left_ptr = middle_ptr + 1
        else:
            right_ptr = middle_ptr

    return left_ptr


def ub_binary_search(val, arr, left_ptr, right_ptr):
    """
        Upper bound binary search

    >>> ub_binary_search(2, [1,2,2,2, 3,33], 0, 5)
    4


    >>> ub_binary_search(2, [], 0, 0)
    0

    >>> ub_binary_search(2, [2], 0, 1)
    1
    """
    while left_ptr < right_ptr:
        middle_ptr = (left_ptr + right_ptr) // 2

        if arr[middle_ptr] <= val:
            left_ptr = middle_ptr + 1
        else:
            right_ptr = middle_ptr

    return left_ptr
