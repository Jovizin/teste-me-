import random
num1 = random.randint(0,10)
num2 = random.randint(0,10)
num3 = random.randint(0,10)
print(f"Foram gerados os números {num1}, {num2} e {num3}!")
print("Que convertidos pra valores binários, ficam: ")
print(f"{num1} = {bin(num1)[2:]}")
print(f"{num2} = {bin(num2)[2:]}")
print(f"{num3} = {bin(num3)[2:]}")