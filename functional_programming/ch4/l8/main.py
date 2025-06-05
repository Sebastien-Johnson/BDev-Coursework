def sum_nested_list(lst):
    size = int()

    if len(lst) == 0:
        return size
    if isinstance(lst[0], int) == True:
        return size + lst[0] + sum_nested_list(lst[1:])
    if isinstance(lst[0], list) == True:
        return size + sum_nested_list(lst[0]) + sum_nested_list(lst[1:])
