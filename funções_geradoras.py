#for i in range (10):
#    print(i)
#    i=0

#def funcaoA():
#    x= 0
#    while x < 10:
#        x = x + 1
#        return x 
#print(funcaoA())

def funcaoB():
    x= 0
    while x < 10:
        x= x +1 
        yield x #devolve o valor e mantem o estado 
for i in funcaoB():
    print(i)
    i = 0