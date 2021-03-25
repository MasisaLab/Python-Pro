#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#--------------------------------------------------------------
chocolateada=[]
final=""
n=nr_letters+nr_numbers+nr_symbols
for lettersvar in range(1,(nr_letters+1)):
  chocolateada.append(random.choice(letters))
for numbersvar in range(1,(nr_numbers+1)):
  chocolateada.append(random.choice(numbers))
for symbolsvar in range(1,(nr_symbols+1)):
  chocolateada.append(random.choice(symbols))
for finish in range(1,n+1):
  finish_random=random.choice(chocolateada)
  n-=1
  final= final+ finish_random
  chocolateada.remove(finish_random)
print("tu contraseña ultra segura generado aleatoriamente es "+ final )
