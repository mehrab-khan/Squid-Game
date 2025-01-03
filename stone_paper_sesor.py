import random
bot_score = 0
player_score = 0
choices = ["stone","paper","scissors"]
print("You have only 5 chance best of luck")
for i in range(6):
    
    user_choice = input("Enter (Stone, Paper & Scissors) & Press 0 for Quit : ")
    bot_choice =random.choice(choices)
    print(bot_choice)
    if user_choice == bot_choice:
        print("It's tie")
        print("User Choice : ",user_choice)
        print("Bot : ",bot_choice)
     
    elif (
        (user_choice == 'stone' and bot_choice == 'scissors') or
        (user_choice == 'scissors' and bot_choice == 'paper') or
        (user_choice == 'paper' and bot_choice == 'stone')
    ) : 
        print("Player Win")
        player_score = player_score + 1
        print("User Choice : ",user_choice)
        print("Bot : ",bot_choice)

    else:
        print("Bot Win")
        bot_score = bot_score + 1
        print("User Choice : ",user_choice)
        print("Bot : ",bot_choice)
