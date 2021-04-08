def coincidence(list = None, range = None):
    if(not list or not range):
        return []
    res = []
    for i in list:
        if (type(i) == float or type(i) == int) and i >= min(range) and i <= max(range):
            res.append(i)
    return res

#print(coincidence([1, 2, 3, 4, 5], range(3,6))) # => [3, 4, 5]
#print(coincidence()) # => []
#print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1,4))) # => [1, 2, 2.5]
print(coincidence([1, 2, 3], range(0)))
print(coincidence(range(0)))