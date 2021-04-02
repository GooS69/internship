def multiply_numbers(inputs = None):
    if not inputs:
        return inputs
    res = 1
    flag = True

    for i in str(inputs):
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