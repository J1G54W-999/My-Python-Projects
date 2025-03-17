# Write an if statement that checks if the user is loggedin via their username and password
# if successfull, the code should display some sort of a message
# if unsuccessfull the code should display some sort of an error message

username = input("Please provide a username ")
user_no_spaces = username.replace(" ", "_")

password = input("Please provide a password ")

valid_username = "Invader_Zim"
valid_password = "haha"

if user_no_spaces == valid_username and password == valid_password:
    print("Welcome Zim, Destroyer of worlds!")
elif user_no_spaces != valid_username and password == valid_password:
    print("Incorrect username")
elif user_no_spaces == valid_username and password != valid_password:
    print("Incorrect password")
elif user_no_spaces != valid_username and password != valid_password:
    print("Not even close, self destruct initiated!\n3\n2\n1")
