import re


def count_words(string):
    dict1 = {}
    res = re.findall(r'\w+', string)
    for i in range(len(res)):
        res[i] = res[i].lower()

    for i in res:
        if i in dict1.keys():
            dict1[i] += 1
        else:
            dict1[i] = 1

    return dict1



print(count_words("A man, a plan, a canal -- Panama")) # => {"a" => 3, "man" => 1,"canal" => 1, "panama" => 1, "plan" => 1}
print(count_words("Doo bee doo bee doo")) # => {"doo" => 3, "bee" =>2}
