s = input()

def func(s):
    res = 0
    d = {"IV": 4,
         "IX": 9,
         "XL": 40,
         "XC": 90,
         "CD": 400,
         "CM": 900,
         "I": 1,
         "V": 5,
         "X": 10,
         "L": 50,
         "C": 100,
         "D": 500,
         "M": 1000}
    
    if len(s) == 1:
        return d[s[0]]

    for i in range(len(s)-1):
        
        try:
            num = s[i] + s[i+1]
        except:
            return res
        
        if num in d:
            res += d[num]
            s = s[1:]
        else:
           res += d[s[i]]
           if i == len(s)-2:
               res += d[s[i+1]]

    return res

print(func(s))
