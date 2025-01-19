#array = []
#flag = True
#while flag:
#    s = input()
#    if s:
#        array.append(s)
#    else:
#        flag = False

array = ["qwe", "ewq", "asd", "dsa", "dsas", "qwee", "zxc", "cxz", "xxz", "z", "s", "qweasdzxc", "zzxc"]

by_length = {}

for s in array:
    by_length[len(s)] = [elem for elem in array if len(elem) == len(s)]

by_letters = {}

for length, array in by_length.items():
    for s in array:
        key = ''.join(sorted(s))
        if not key in by_letters.keys():
            by_letters[key] = []
        by_letters[key].append(s)


res = list(by_letters.values())
print(res)
