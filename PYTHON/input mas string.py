# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
small = 15
Medium = 20
Large = 25
small_pepperoni = 2
Medium_pepperoni = 3
Large_pepperoni = 3
Chees_Extra = 1
S = "S"
M="M"
L="L"
Y="Y"
N ="N"
Total_pay = 0
if size == S:
 Total_pay = small
 if add_pepperoni == Y:
   Total_pay +=small_pepperoni
   if extra_cheese == Y:
       Total_pay +=Chees_Extra
       print(f"monto total a pagar {Total_pay}")
   else :
      print(f"monto total a pagar {Total_pay}")
 else:
    print(f"monto total a pagar {Total_pay}")      
elif size == str(M):
 Total_pay = Medium
 if add_pepperoni == Y:
   Total_pay +=Medium_pepperoni
   if extra_cheese == Y:
       Total_pay +=Chees_Extra
       print(f"monto total a pagar {Total_pay}")
   else :
      print(f"monto total a pagar {Total_pay}")
 else:
    print(f"monto total a pagar {Total_pay}")
elif size == L :
 Total_pay = Large
 if add_pepperoni == Y:
   Total_pay +=Large_pepperoni
   if extra_cheese == Y:
       Total_pay +=Chees_Extra
       print(f"monto total a pagar {Total_pay}")
   else :
      print(f"monto total a pagar {Total_pay}")
 else:
    print(f"monto total a pagar {Total_pay}")  
else :
  print("Ingrese Datos Validos")     
