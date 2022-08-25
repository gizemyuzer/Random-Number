import random

num_range=(1,100)
random_num=random.randint(num_range[0],num_range[1])
guess=""
game_on=True

while game_on:
    while guess!= random_num:
        guess=int(input("What is your guess?"))
        if guess<random_num:
            print("Too low, try again.")
        elif guess> random_num:
            print("Too high, try again.")
        else:
            print(f"You did it! the number was {random_num}.")
            game_on=False

    play_again=input("Do you want to play again?(y/n)").lower
    if play_again== "y":
        random_num=random.randint(num_range[0],num_range[1])
        guess=""
