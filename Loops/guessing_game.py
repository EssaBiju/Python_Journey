secret_number= 7
a=0
i=3
while a<i:
    guess=int(input("Guess: "))
    a=a+1
    if guess==secret_number:
        print("You Win")
        break
    else:
        print("You Loose")
        


