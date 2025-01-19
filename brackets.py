n = 3

def f(brackets=""):
    global res
    if len(brackets) == 2*n:
        res.append(brackets)
        return None
    
    if brackets.count("(") < n:
        f(brackets+"(")

    if brackets.count(")") < brackets.count("("):
        f(brackets+")")

res = []
f()
print(res)
