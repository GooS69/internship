def connect_dicts(dict1, dict2):
    dict3 = {}
    list = [dict1, dict2]
    if sum(dict2.values()) < sum(dict1.values()):
        list[0], list[1] = list[1], list[0]
    for i in list:
        for j in i.items():
            if j[1] >= 10:
                dict3[j[0]] = j[1]

    sorted_dict = {}
    sorted_keys = sorted(dict3, key=dict3.get)

    for i in sorted_keys:
        sorted_dict[i] = dict3[i]


    return sorted_dict


print(connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 })) # =>{ "c": 11, "b": 12 }
print(connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 })) # =>{ d: 11, "c": 12, "a": 13 }
print(connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 })) # =>{ "c": 11, "b": 12, "a": 15 }
