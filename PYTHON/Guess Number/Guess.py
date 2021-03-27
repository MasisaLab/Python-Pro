from art import logo
import random
def game():
    print(logo)
    number=[]
    for i in range(1,101):
        number.append(i)
    pc=random.choice(number)
    print("Intenta adivinar el numero elegido 1 al 100 ")
    difficulty=input("Que dificultad quieres 'easy' o 'hard' : ")
    if difficulty=="easy" :
        n= 10
    elif difficulty=="hard":
        n=5
    else :
        print("Dificultad invalida")
        game()
    vida=0
    def final():
        reinicio=input("Quiere Volver a jugar 'y' o 'n' : ")
        if reinicio == "y":
            game()
        else :
            return
    while vida<=n:
        user=int(input("Ingrese lo que cree que eligio: "))
        if user==pc :
            print("You Win")
            vida=n+1
            final()
        elif user<pc :
            print("Es un numero muy bajo")
        elif user>pc:
            print("Es un numero muy alto")
        vida+=1
    print("Has perdido")
    final()
game()
        


