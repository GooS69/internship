def is_palindrome(string):
    res = ""
    for i in str(string):
        if i.isalpha() or i.isdigit():
            res += i

    res = res.lower()
    return res == res[::-1]


#print(is_palindrome("A man, a plan, a canal -- Panama")) # => True
#print(is_palindrome("Madam, I'm Adam!")) # => True
#print(is_palindrome(333)) # => True
#print(is_palindrome(None)) # => False
#print(is_palindrome("Abracadabra"))# => False
print(is_palindrome(3343))