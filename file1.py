import random

def random_division():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 1000)
    result = num2 / num1
    print(f"Random numbers: {num2} / {num1} = {result}")

random_division()
