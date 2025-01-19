from itertools import permutations

#array = list(map(int, input().split(",")))
array = [1,1,2]

res = []
for combination in list(permutations(array)):
    if not list(combination) in res:
        res.append(list(combination))

print(res)

