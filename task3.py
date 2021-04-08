def max_odd(list = None):
    if not list:
        return None
    res = float("-inf")
    for i in list:
        if((type(i) == float or type(i) == int) and i % 2 == 1 and i > res):
            res = i

    if res != float("-inf"):
        return res
    else:
        return None


print(max_odd([1, 2, 3, 4, 4])) # => 3
print(max_odd([21.0, 2, 3, 4, 4])) # => 21
print(max_odd(['ololo', 2, 3, 4, [1, 2], None])) # => 3
print(max_odd(['ololo', 'fufufu'])) # => None
print(max_odd([2, 2, 4])) # => None