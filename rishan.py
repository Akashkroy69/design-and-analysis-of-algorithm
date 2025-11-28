import random
num=random.randint(1,100)
while True:
   guess=int(input("Guess a number(1-100): "))
   if num==guess:
        print("Correct Guess")
        break
   elif num<guess:
       print("That is incorrect. Try a smaller number.")
   elif num>guess:
       print("That is incorrect. Try a greater number.")
