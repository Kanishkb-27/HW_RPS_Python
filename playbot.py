import random
def check_win(player_move,ai_move):
    if player_move=="rock":
        if ai_move=="rock":
            print("Draw")
        elif ai_move=="paper":
            print("AI wins")
        else:
            print("You win!")
    elif player_move=="paper":
            if ai_move=="rock":
                print("You win!")
            elif ai_move=="paper":
                print("Draw")
            else:
                print("AI wins")
    elif player_move=="scissors":
            if ai_move=="rock":
                print("AI wins")
            elif ai_move=="paper":
                print("You win!")
            else:
                print("Draw")
    else:
         print("Invalid input")
def game():
     print("Welcom to a game of rock, paper, scissors")
     possible_moves=["rock","paper","scissors"]
     while True:
               player_move=input("Enter your move (rock, paper, or scissors): ").lower()
               ai_move=random.choice(possible_moves)
               check_win(player_move,ai_move)
if __name__=="__main__":
    game()