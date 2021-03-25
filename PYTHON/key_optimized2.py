Primero=input("Ingrese el primer numero")
Segundo=input("Ingrese el primer segundo")
Tercero=input("Ingrese el primer tercer")
if Primero > Segundo:
  a=Primero
  if a>Tercero:
    print(f"Este es el numero mayor {a}")
  else :
    print(f"Este es el numero mayor {Tercero}")
elif Segundo>Tercero:
  print(f"Este es el numero mayor {Segundo}")
else:
  print(f"Este es el numero mayor {Tercero}")

  