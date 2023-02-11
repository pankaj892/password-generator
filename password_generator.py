import random

print("Welcome to your password generator!")

# Ask user for length of password
length = int(input("How many characters would you like your password to be? "))

#input validation\error handling
#check if length is less than 6
if length < 6 or length == "":
    print("Your password must be at least 6 characters long or more.It cannot be blank.")
    exit()
else:
    length = int(input("How many characters would you like your password to be? "))

# Ask user for number of passwords to generate
number = int(input("How many passwords would you like to generate? "))

#input validation\error handling
#check if number is less than 1 or greater than 100
if number < 1 or number > 100:
    print("Please enter a number between 1 and 100.")
    number = int(input("How many passwords would you like to generate? "))

# Define characters to use in password
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+?><"

print("Here are your passwords:")

# Loop through number of passwords to generate
for pwd in range(number):
    password = ""
    # Loop through length of password
    for c in range(length):
        password += random.choice(chars)
    print(password)

print("Thank you for using the password generator!")