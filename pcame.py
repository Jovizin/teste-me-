import numpy
import random
num1 = random.randint(0,10)
num2 = random.randint(0,10)
num3 = random.randint(0,10)
print(f"Foram gerados os números {num1}, {num2} e {num3}!")
print("Que convertidos pra valores binários, ficam: ")
print(f"{num1} = {numpy.binary_repr(num1)}")
print(f"{num2} = {numpy.binary_repr(num2)}")
print(f"{num3} = {numpy.binary_repr(num3)}")