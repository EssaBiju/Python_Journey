n=int(input("Weight: "))
s=input("(L)bs or (K)g")
if s.upper()=="L":
    converted=float(n)/2.2
    print(f"Your Weight is {converted}kilos")
else:
    converted=float(n)*2.2
    print(f"Your weight is {converted}pounds")
