player= input("Elija Piedra,Papel o Tijera ")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
Game=["Piedra","Papel","Tijera"]
pc=random.randint(0,2)
pc_choose=Game[pc]
if player=="Tijera":
  if pc_choose == "Tijera":
    print(scissors)
    print("lo que eligio la pc")
    print(scissors)
    print ("lo que elejistes")

    print("EMPATE")
  elif pc_choose=="Piedra":
    print(rock)
    print("lo que eligio la pc")
    print(scissors)
    print("lo que elijistes tu")

    print ("PERDISTES") 
  elif pc_choose=="Papel":
    print(paper)
    print("lo que eligio la pc")
    print(scissors)
    print("lo que elijistes tu")

    print ("GANASTES") 
elif player=="Papel" :
  if pc_choose == "Tijera":
    print(scissors)
    print("lo que eligio la pc")
    print(paper)
    print ("lo que elejistes")

    print("PERDISTES")
  elif pc_choose=="Piedra":
    print(rock)
    print("lo que eligio la pc")
    print(paper)
    print("lo que elijistes tu")

    print ("GANASTES") 
  elif pc_choose=="Papel":
    print(paper)
    print("lo que eligio la pc")
    print(paper)
    print("lo que elijistes tu")

    print ("EMPATE") 
elif player=="Piedra" :
  if pc_choose == "Tijera":
    print(scissors)
    print("lo que eligio la pc")
    print(rock)
    print ("lo que elejistes")

    print("GANASTES")
  elif pc_choose=="Piedra":
    print(rock)
    print("lo que eligio la pc")
    print(rock)
    print("lo que elijistes tu")

    print ("EMPATE") 
  elif pc_choose=="Papel":
    print(paper)
    print("lo que eligio la pc")
    print(rock)
    print("lo que elijistes tu")

    print ("PERDISTES") 