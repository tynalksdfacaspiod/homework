#n = int(input())
#banks = []
#for _ in range(n):
#    data = input().split(",")
#    banks.append((data[0], int(data[1])))

banks = [('sber',10),('tin',5),('vol',6),('ker',12)]

options = {}
for first in banks[:-1]:
    for second in banks[1:]:
        options[first[-1]+second[-1]] = [first, second]

max_amount = max(options.keys())
res_banks = options[max_amount]
print([max_amount, res_banks])
