'''The "Oracle Orb" is a fortune telling game. 
The player asks a question, shakes the orb, and then looks at the dice to see the answer. 
The player can then ask another question and repeat the process. 
The player can ask as many questions as they like. 
The Oracle Orb is always right!
'''

import random

# Welcome message
print("Welcome, I am the Great Oracle Orb!")

# Initalises the play_again variable
play_again = "Y"

# While loop contains the logic for the game
# Will keep running game until play_again != "Y"
while play_again == "Y":
    input("Ask me any question and I shall bestow my wisdom upon you: ")
    print("Intersting question. Hmmm... let me think about this one...")

    # Generate a random number between 1 and 20
    answer = random.randint(1, 20)

    # Long conditional statement that determines which output to print based on random number
    if answer==1:
        print("It is certain.")
    elif answer==2:
        print("It is decidedly so.")
    elif answer==3:
        print("Without a doubt.")
    elif answer==4:
        print("Yes definitely.")
    elif answer==5:
        print("You may rely on it.")
    elif answer==6:
        print("As I see it, yes.")
    elif answer==7:
        print("Most likely.")
    elif answer==8:
        print("Outlook good.")
    elif answer==9:
        print("Yes.")
    elif answer==10:
        print("Signs point to yes.")
    elif answer==11:
        print("Reply hazy, try again.")
    elif answer==12:
        print("Ask again later.")
    elif answer==13:
        print("Better not tell you now.")
    elif answer==14:
        print("Cannot predict now.")
    elif answer==15:
        print("Concentrate and ask again.")
    elif answer==16:
        print("Don't count on it.")
    elif answer==17:
        print("My reply is no.")
    elif answer==18:
        print("My sources say no.")
    elif answer==19:
        print("Outlook not so good.")
    elif answer==20:
        print("Very doubtful.")

    # Asks user if they want to play again
    play_again = input("Do you seek more answers from the Great Oracle Orb more questions? Y/N: ")

# End game outside While loop
print("Until you return. Farewell!")
