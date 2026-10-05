import random  # You need to add this import at the top

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', 
           '[', ']', '{', '}', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?', '\\', '|']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


print("welcome to password generator")
nr_letters = int(input("how many letters would you like to use? \n"))
nr_symbols = int(input(f"how many symbols you would use? \n"))
nr_numbers = int(input(f"how many numbers would you like ? \n"))


password = ""
for char in range(0,nr_letters):
    password += random.choice(letters)
    
for char in range(0,nr_symbols):
    password += random.choice(symbols)

for char in range(0,nr_numbers):
    password += random.choice(numbers)
    
    
print(password)
