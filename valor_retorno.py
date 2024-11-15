def soma(x,y):
    T = x + y
    x= 0 #este valor não sera alterado na variavel global
    print(id(x))
    y= 0
    print(id(x))
    return T
x= soma(10,5)
print(soma(10,5))
x= int(input("X:"))
y= int(input("Y:"))
z= int(input("Z:"))
print(soma(x,soma(y,z)))