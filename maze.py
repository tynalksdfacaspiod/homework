n = 4
m = 4

def f(i,j):
    if i==n-1 and j==m-1:
        return 1
    if i>n-1 or j>m-1:
        return 0
    return f(i,j+1)+f(i+1,j)

res = f(0,0)
print(res)
