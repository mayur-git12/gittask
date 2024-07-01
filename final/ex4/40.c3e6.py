winning_num = 66
guess = 1
number = int(input("enter num:"))
game_over=False
while not game_over:
    if number==winning_num:
        print(f"you win & you guessd num in {guess}times")
        game_over=True
    else:
        if number<winning_num:
            print("low")
            guess=guess+1
            game_over=False
            number=int(input("guess again:"))
        else:
            print("high")
            guess=guess+1
            game_over=False     
            number=int(input("guess again:"))  
