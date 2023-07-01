import random
print(
    
'''
  ________                                __  .__              _______               ___.                  _________ 
 /  _____/ __ __   ____   ______ ______ _/  |_|  |__   ____    \      \  __ __  _____\_ |__   ___________  \_____   \
/   \  ___|  |  \_/ __ \ /  ___//  ___/ \   __\  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \    /   __/
\    \_\  \  |  /\  ___/ \___ \ \___ \   |  | |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/   |   |   
 \______  /____/  \___  >____  >____  >  |__| |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|      |___|   
        \/            \/     \/     \/             \/     \/          \/            \/    \/     \/          <___>


''')
print("Welcome To The Number Guessing Game!")
print("I am thinking a nummber between 1 to 100")
level=input("Choose a difficulty. Type 'easy' or 'hard':")
if level=="easy":
    attempts=10
    
elif level=="hard":
    attempts=5
rand_number=random.randrange(1,101)
flag=0
while attempts!=0 :
    print(f"you have {attempts} attempts remaining to guess the number.")
    your_guess=int(input("make  a guess:"))
    if your_guess>rand_number:
        print("Too High.")
        print("Guess Again:")
        attempts=attempts-1
    elif your_guess<rand_number:
        print("Too Low.")
        print("Guess Again:")
        attempts=attempts-1
    elif your_guess==rand_number:
        flag=flag+1
        print("You Win!")
        attempts=0
if flag==0 and attempts==0 :
    print("the number is: ",rand_number)
    print("You loose!")
    
       
    