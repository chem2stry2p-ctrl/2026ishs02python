import mymath
number = int(input("Enter a Number: "))
print(f"{number}! = {mymath.factorial(number)}")
print(f"{number}! = {mymath.factorial_iter(number)}")