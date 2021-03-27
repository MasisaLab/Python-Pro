from art import logo
import random
def BlackJack():
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    is_game_over=False
    user_cards = []
    computer_cards = []
    for i in range(2):
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
    def calculate_score(card) :
        sum(card)
        if sum(card)==21 and len(card)==2:
            return 0
        elif sum(card)>21 and 11 in card:
            card.remove(11)
            card.append(1)
            print("salvado tu As se convertio en 1")
            return sum(card)
        return sum(card)
    if calculate_score(user_cards)==0 or calculate_score(computer_cards)==0 or calculate_score(user_cards)>21 or calculate_score(computer_cards)>21 :
        is_game_over=True
    n=-1
    while is_game_over==False :
        n+=1
        print(f"tus cartas {user_cards}, tu puntaje {calculate_score(user_cards)}")
        print(f"la primera carta de la computadora es {computer_cards[0]}")
        game=input("escribe Y para recibir una carta o N para terminar el juego : ")
        if game=="Y":
            user_cards.append(random.choice(cards))
            calculate_score(user_cards)
        if calculate_score(user_cards)==0 or calculate_score(computer_cards)==0 or calculate_score(user_cards)>21 or calculate_score(computer_cards)>21 :
            is_game_over=True
        elif game=="N":
            is_game_over=True
    while calculate_score(computer_cards)<17 and n>=1:
        computer_cards.append(random.choice(cards))
        calculate_score(computer_cards)
    print("------------------------------------")
    def compare(c1,c2):
        if c2==c1 :
            print("Empataron 🙃")
        elif c2==0  : 
            print("you Lose, tu oponente saco BalckJack 😱")
        elif c1==0:
            print("You Win, Sacastes BlackJack 😎")
        elif c1>21 :
            print("You Lose, 😭")
        elif c2>21 :
             print("You Win, 😁")
        elif c1>c2 :
             print("You Win, 😃")
        else :
            print("You lose, 😤")
    compare(calculate_score(user_cards),calculate_score(computer_cards))
    print(f"tus cartas {user_cards}, tu puntaje {calculate_score(user_cards)}")
    print(f"la carta de la computadora es {computer_cards}, su puntaje {calculate_score(computer_cards)}")
    print("------------------------------------")
    init=input("Quiere seguir Jugando Y O N : ")
    if init=="Y":
        BlackJack()
    elif init=="N" :
        return "Hasta la proxima"
BlackJack()