import random
import time
import string
import pyfiglet
from colorama import Fore
bot_score = 0
player_score = 0
game_continue = False

def redroom_game():
    global game_continue
    red_room_title = pyfiglet.figlet_format("Welcome To Red Room")
    print(Fore.RED + red_room_title)
    print(Fore.RESET)
    print("Red Room List : ")
    print('----------------')
    available_room_name = []
    def generate_room_name():
        for i in range(2):
            asciiLetter = []
            lowerWord = []
            digits = []
            hex = []     
            asciiLetter.append(random.choice(string.ascii_letters))
            lowerWord.append(random.choice(string.ascii_lowercase))
            digits.append(random.choice(string.digits))
            hex.append(random.choice(string.hexdigits))
            available_room_name.append(asciiLetter[0])
            available_room_name.append(lowerWord[0])
            available_room_name.append(digits[0])
            available_room_name.append(hex[0])
        combineRoomName = ''.join(available_room_name)
        return combineRoomName
    room1 = generate_room_name()
    room2 = generate_room_name()[7:15]
    room3 = generate_room_name()[15:23]
    room4 = generate_room_name()[23:31]
    room5 = generate_room_name()[31:39]
    print(room1)
    time.sleep(1)
    print(room2)
    time.sleep(1)
    print(room3)
    time.sleep(1)
    print(room4)
    time.sleep(1)
    print(room5)
    rooms = [room1,room2,room3,room4,room5]
    danger1 = random.choice(rooms)
    danger2 = random.choice(rooms)
    user_choice_room = input("Enter Room Name : ")
    user_choice_room_no_whiteSpace = user_choice_room.strip()
    if(user_choice_room_no_whiteSpace in [danger1, danger2]):
        print(Fore.RED + "You Lost The Danger in this room try again")
        print(Fore.RESET)
        print(f'Danger in room {danger1} and {danger2}')
        time.sleep(2)
        game_continue == False
    else:
        if user_choice_room not in rooms:
            print(Fore.RED + "You typed wrong room name please try again")
            print(Fore.RESET)
        else:
            print(Fore.YELLOW + "Congratulations You Escaped The Red Room")
            print(Fore.RESET)


def stone_paper_scissors(player_name):
    global bot_score
    global game_continue
    global player_score
    stone_paper_scissors_title = pyfiglet.figlet_format("Stone, Paper & Scissors")
    print(Fore.BLUE + stone_paper_scissors_title)
    print(Fore.RESET)
    print("Are You Ready ?")
    user_init_choice = input("Enter 'y' for YES or Enter 'n' for NO : ")
    choices = ["stone","paper","scissors"]
    user_init_choice = user_init_choice.lower()
    if user_init_choice == 'y':
        print("You have only 5 chance best of luck")
        print(Fore.YELLOW + "WARNING : if you press any wrong key bot wins")
        print(Fore.RESET)
        time.sleep(4)
        for i in range(5):
            user_choice = input("Enter (Stone, Paper & Scissors) : ")
            user_choice = user_choice.strip()
            bot_choice =random.choice(choices)
            
            if user_choice == bot_choice:
                print(Fore.YELLOW + "---- >>>> It's tie")
                print(Fore.RESET)
                print(Fore.BLUE)
                print(f'------ {player_name} : {user_choice}')
                print("------ Bot : ",bot_choice)
                print(Fore.RESET)
            
            elif (
                (user_choice == 'stone' and bot_choice == 'scissors') or
                (user_choice == 'scissors' and bot_choice == 'paper') or
                (user_choice == 'paper' and bot_choice == 'stone')
            ) : 
                print(Fore.YELLOW+f"---- >>>> {player_name} gain 1 point")
                print(Fore.RESET)
                player_score = player_score + 1
                print(Fore.BLUE)
                print(f'------ {player_name} : {user_choice}')
                print("------ Bot : ",bot_choice)
                print(Fore.RESET)

            else:
                print(Fore.RED+"---- >>>> Bot Win")
                print(Fore.RESET)
                bot_score = bot_score + 1
                print(Fore.BLUE)
                print(f'-------- {player_name} : {user_choice}')
                print("------- Bot : ",bot_choice)
                print(Fore.RESET)

            print(Fore.CYAN)
            print('Bot Score ',bot_score)
            print('Player Score ',player_score)
            print(Fore.RESET)

        if player_score > bot_score:
            print(f"Player {player_name} : Win")
        elif player_score == bot_score:
            print("Tie try once")
            stone_paper_scissors(f'( {user_name} ) Player No. {main_player}')
        else:
            print("Bot Wins")
            print(Fore.RED + f"{main_player} ( {user_name} ) lost you are eliminated ")
            print(Fore.RESET)
            game_continue = False
            quit()

    else:
        print("Thanks for playing")
        quit()
            


welcome_note = "WELCOME TO SQUID GAME"
print(Fore.CYAN + pyfiglet.figlet_format(welcome_note))
print(Fore.RESET)
players = []
main_player = random.randint(1,50)
last_player = random.randint(1,50)
user_name = input("Enter Your Name : ").capitalize()
print("You have been selected to player no. ",main_player)
for i in range(1,51):
    if i == main_player:
        players.append(f'{main_player} ( {user_name} )')
        continue
    if i == last_player:
        players.append(f'{last_player}')
        continue
    else:
        players.append(i)
 
print(f"Total Alive Player's {len(players)}")
print(f'Player\'s : {players}')
print("Are you Entering the game ? ")
user_opinion = input("Enter 'y' for YES or Enter 'n' for NO\nEnter : ")
if user_opinion == 'n' or user_opinion == 'N':
     print("Thanks for playing")
     quit()
else:
    game_continue = True
while game_continue:
    
    print("First Game Is Stone, Paper & Scissors")
    stone_paper_scissors(f'( {user_name} ) Player No. {main_player}')
    time.sleep(1)
    print(f"Congratualations {user_name} You have done your first game")
    time.sleep(4)
    print('---------------')
    print("Next Game is Red Room")
    time.sleep(2)
    print("Rules are very simple : \nThere are 5 room but 2 rooms has danger you have to choose\n safe one to stay let go\n game starts in 2 seconds")
    time.sleep(2)
    redroom_game()
    break