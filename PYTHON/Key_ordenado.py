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
letters_digit=len(letters)
part1=""
numbers_digit=len(numbers)
part2=""
symbols_digit=len(symbols)
le_suma=letters_digit+numbers_digit+symbols_digit
part3=""
final=""
n=2
for lettersvar in range(1,(nr_letters+1)):
  random_letter=random.randint(0,(letters_digit-1))
  letters_password=letters[random_letter]
  part1=part1 + letters_password
for numbersvar in range(1,(nr_numbers+1)):
  random_number=random.randint(0,(numbers_digit-1))
  numbers_password=numbers[random_number]
  part2=part2 + numbers_password
for symbolsvar in range(1,(nr_symbols+1)):
  random_symbols=random.randint(0,(symbols_digit-1))
  symbols_password=symbols[random_symbols]
  part3=part3 + symbols_password
lucky=[part1,part2,part3]
for randomlucky in range(1,4):
  random_lucky=random.randint(0,n)
  lucky_final= lucky[random_lucky]
  n-=1
  final=final + lucky_final 
  lucky_elimanted=lucky.pop(random_lucky)
print("tu contraseña ultra segura generado aleatoriamente es "+ final)
