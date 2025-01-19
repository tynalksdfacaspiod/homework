from itertools import product


l1 = [1, 2, 3, 4]


res = []
a = product(l1, repeat=4)
for i in a:
    res.append(list(set(i)))


res2 = []
length = len(res)
for i in range(length):
    if not res[i] in res2:
        res2.append(res[i])
        isUnique = True

print(res2, len(res2))
