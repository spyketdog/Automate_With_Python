# This program says hello and ask for my name

print("Hello Word! ")

print("What is your name? ") # Ask for the users name
my_name = input()
print("It's is good to meet you, " + my_name)
print("The length of your name is: ")
print(len(my_name))

print("What is your age? ") # Ask users for their age
my_age = input()
print("You will be " + str(int(my_age) + 1) + " in a year.")
