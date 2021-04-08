def sort_list(list = None):
    if len(list) == 0 or not list:
        return list
    min_elem = min(list)
    max_elem = max(list)
    for i in range(len(list)):
        if list[i] == min_elem:
            list[i] = max_elem
        elif list[i] == max_elem:
            list[i] = min_elem
    list.append(min_elem)
    return list


print(sort_list([]))  # => []
print(sort_list([2, 4, 6, 8]))  # => [8, 4, 6, 2, 2]
print(sort_list([1]))  # => [1, 1]
print(sort_list([1, 2, 1, 3]))  # => [3, 2, 3, 1, 1]
