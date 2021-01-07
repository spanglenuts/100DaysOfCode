#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
pw = ""
for n1 in range(0,nr_letters):
  if n1 != nr_letters:
    pw += random.choice(letters)


for n2 in range(0,nr_symbols):
  if n2 != nr_symbols:
    pw += random.choice(symbols)

  
for n3 in range(0,nr_numbers):
  if n3 != nr_numbers:
    pw += random.choice(numbers)

print(f"Your EASY password is {pw}")

#HARD MODE CODE...

pw = []
for n1 in range(0,nr_letters):
  if n1 != nr_letters:
    pw.append(random.choice(letters))


for n2 in range(0,nr_symbols):
  if n2 != nr_symbols:
    pw.append(random.choice(symbols))

  
for n3 in range(0,nr_numbers):
  if n3 != nr_numbers:
    pw.append(random.choice(numbers))


# pw = ''.join(random.sample(pw, len(pw)))

random.shuffle(pw)
hpw = ""
for char in pw:
  hpw += char

print(f"Your HARD password is {hpw}")
