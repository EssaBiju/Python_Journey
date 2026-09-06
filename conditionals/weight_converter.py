# Problem:
# Write a Python program that asks the user to enter their weight
# and specify whether it is in pounds (L) or kilograms (K).
# Convert the weight to the other unit and display the result.

n=int(input("Weight: "))
s=input("(L)bs or (K)g")
if s.upper()=="L":
    converted=float(n)/2.2
    print(f"Your Weight is {converted}kilos")
else:
    converted=float(n)*2.2
    print(f"Your weight is {converted}pounds")
