UpTo = int(input("Insira o limite:"))
def fizzbuzz(UpTo):
    for n in range(1, UpTo+1):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz", end=" ")
        elif n % 3 == 0:
            print("Fizz", end=" ")
        elif n % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(n, end=" ")

def fizzbuzz_v2(UpTo):
    for n in range(1, UpTo+1):
        if n % 15 == 0:
            print("FizzBuzz", end=" ")
        elif n % 3 == 0:
            print("Fizz", end=" ")
        elif n % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(n, end=" ")

def fizzbuzz_v3(UpTo):
    for i in range(1,UpTo+1):
        print("FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i, end=" ")
    
fizzbuzz(UpTo)
fizzbuzz_v2(UpTo)
fizzbuzz_v3(UpTo)