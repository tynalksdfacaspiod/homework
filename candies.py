from math import factorial as fact
candies = int(input())
packages = int(input())

def func(candies, packages):
    if (candies < packages) or candies==0 or packages == 0:
        return 0
    if candies == packages:
        return 1
    return func(candies-1, packages-1) + packages * func(candies-1, packages)

res = func(candies, packages)
if func(candies, packages):
    print(res)
else:
    print("No solution")
