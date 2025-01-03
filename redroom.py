import time
import string
import random
import pyfiglet
from colorama import Fore, init
 

def redroom_game():
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
        print("You Lost The Danger in this room try again")
        print(f'Danger in room {danger1} and {danger2}')
    else:
        if user_choice_room not in rooms:
            print("You typed wrong room name please try again")
        else:
            print("Congratulations You Escaped The Red Room")


