#Password Generator
import random
letters = ['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")
no_letters = int(input("How many letters would you like in your password?\n "))
no_symbols = int(input("How many symbols would you like in your password?\n "))
no_numbers =  int(input("How many numbers would you like in your password?\n "))

password = ""
for letter in range(1, no_letters + 1):
    password += random.choice(letters)
for letter in range(1, no_symbols + 1):
    password += random.choice(symbols)
for letter in range(1, no_numbers + 1):
    password += random.choice(number)
print(password)

#hard level
password_list = []
for letter in range(1, no_letters + 1):
    password_list += random.choice(letters)
for letter in range(1, no_symbols + 1):
    password_list += random.choice(symbols)
for letter in range(1, no_numbers + 1):
    password_list += random.choice(number)
print(password_list)
random.shuffle(password_list)
print(password_list)

hard_password = ""
for char in password_list:
    hard_password += char
print(f"your password is: {hard_password}")