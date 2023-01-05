import random



def choices():
    choices =("rock","paper","scissors")
    pc_choice = random.choice(choices)
    user_choice = input("what is your choice: ")

    if user_choice not in choices:
        print("Not a valid answer")
        return None,None
    
    print(f"computer answer: {pc_choice}")
    print(f"Your answer: {user_choice}")
    return pc_choice,user_choice

def check(user_choice,pc_choice,u_wins,p_wins):
    if pc_choice == "rock" and user_choice == "scissors":
        p_wins +=1
        print("PC won")
    elif pc_choice == "paper" and user_choice == "rock":
        p_wins +=1
        print("PC won")
    elif pc_choice == "scissors" and user_choice == "paper":
        p_wins +=1
        print("PC won")
    elif pc_choice == "rock" and user_choice == "paper":
        u_wins +=1
        print("You won")
    elif pc_choice == "Paper" and user_choice == "scissors":
        u_wins +=1
        print("You won")
    elif pc_choice == "scissors" and user_choice == "rock":
        u_wins +=1
        print("You won")
    elif pc_choice == user_choice:
        print("It's a tie")
    return p_wins, u_wins

    
def run_game():
     user_wins =0
     pc_wins = 0
     rounds = 1
     
     while True:
        print("#"*20)
        print("Round: ",rounds)
        print("#"*20)

        print(f"computer wins: {pc_wins}")
        print(f"your wins: {user_wins}")
        rounds +=1

        pc_option, user_option = choices()
        pc_wins,user_wins = check(user_option,pc_option,user_wins,pc_wins)
        

        if pc_wins ==2:
            print("PC WINS THE GAME")
            break
        elif user_wins ==2:
            print("YOU WIN THE GAME")
            break

            
run_game()