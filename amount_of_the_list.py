from itertools import permutations


#n = int(input())
#array = [int(input()) for _ in range(n)]
#c = int(input())
n = 6
array = [3, -5, -7, 12, -2, 5]
c = -5

combinations = list(permutations(array, r=4))

for combination in combinations:
    amount = sum(combination)
    if amount in [c-2,c-1,c,c+1,c+2]:
        print(combination, amount, sep="\n")
        break
