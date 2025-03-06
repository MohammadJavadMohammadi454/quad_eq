import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

delta = b**2 - 4*a*c

if delta > 0:
    root1 = (-b + math.sqrt(delta)) / (2*a)
    root2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"Real roots: {root1} and {root2}")
elif delta == 0:
    root = -b / (2*a)
    print(f"The equation has one double root: {root}")
else:
    print("The equation has no real roots.")
    