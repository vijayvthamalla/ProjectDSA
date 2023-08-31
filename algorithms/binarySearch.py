def check_location(search_space, query, mid):
    mid_num = search_space[mid]
    if mid_num == query:
        if mid - 1 >= 0 and search_space[mid - 1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_num < query:
        return 'left'
    else:
        return 'right'


def BinarySearch(search_space, query):
    lo, hi = 0, len(search_space) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        val = check_location(search_space, query, mid)
        if val == 'found':
            return mid
        elif val == 'left':
            hi = mid - 1
        elif val == 'right':
            lo = mid + 1
    return -1
