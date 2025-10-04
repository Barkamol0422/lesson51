from math import *
n=float(input("Enter a number: "))

if n>1:
    for i in range(2, int(sqrt(n)+1)):
        if n%i==0:
            print(n," is not prime number")
        else:
            print(n," is prime number")
else:
    print(n," is not prime number")
