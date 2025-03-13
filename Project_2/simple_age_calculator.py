# Simple interactive scripte that calculates your age
# Enter your birthday and it will tell you your age
# Also does a quick basic addition calculation

print("Hello, My name is Beamo. ")

name = input("What is your name? ")

print("Hello, " + name + ". Nice to meet you. ")

print("If you tell me your birth year, I'll tell you how old you are ")

birth_year = input("What year were you born? ")
age = 2024 - int(birth_year)

print("okay, so that means you are " + str(age))

print("I'm also a quick-math wiz, ask me any 2 numbers and ill give you the sum. ")
First = input("Okay, enter a number ")
Second = input("Now another number ")
Sum = (float(First) + float(Second))

print("Easy, that would be " + str(Sum))

print("Thanks, I had fun. Bye :) ")
