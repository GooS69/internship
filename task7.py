def combine_anagrams(list):
    sort = []
    res = []
    for i in range(len(list)):
        list[i] = list[i].lower()

    for i in list:
        if sorted(i) in sort:
            res[sort.index(sorted(i))].append(i)
        else:
            sort.append(sorted(i))
            res.append([i])

    return res


print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams",
                        "scream"]))  # => [ ["cars", "racs", "scar"], ["four"], ["for "],["potatoes"], ["creams", "scream"] ]
