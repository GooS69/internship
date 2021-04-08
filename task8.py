def multiply_numbers(*inputs):
    if not inputs:
        return None
    res = 1
    flag = True

    for elem in inputs:
        for i in str(elem):
            if i.isdigit():
                flag = False
                res *= int(i)

    if flag:
        return None
    else:
        return res


print(multiply_numbers()) # => None
print(multiply_numbers('ss')) # => None
print(multiply_numbers('1234')) # => 24
print(multiply_numbers('sssdd34')) # => 12
print(multiply_numbers(2.3)) # => 6
print(multiply_numbers([5, 6, 4])) # => 120
print(multiply_numbers(2, "a3d", [1, 3, 1]))
print(multiply_numbers())