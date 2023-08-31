def LinearSearch(search_space, query):
    num = 0
    while num < len(search_space):
        if query == search_space[num]:
            return num
        num += 1
    return -1
