#Password Generator Project

import random

print("Welcome to the Password Generator")
numbers_of_letter = int(input("How many letters would you like in your password?\n"))
numbers_of_symbol = int(input("How many symbols would you use?\n "))
numbers_of_number = int(input("How many numbers would you use?\n "))

letters = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

your_password = []

for letter in range (0, numbers_of_letter):
    your_password.append (random.choice(letters))
for symbol in range (0, numbers_of_symbol):
    your_password += random.choice(symbols)
for number in range (0, numbers_of_number):
    your_password += random.choice(numbers)

random.shuffle(your_password)
password = ""
for char in your_password:
    password += char
print(f"Here is your password: {password}")