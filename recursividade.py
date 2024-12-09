def contar(n):
    if n == 100:
        return n
    return contar(n+1)
print(contar(10))