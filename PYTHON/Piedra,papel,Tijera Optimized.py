import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lifes=7
word_1list=["oso hormiguero","babbon","camel"]
word_choice=random.choice(word_1list)
completed=""
print(f"palabra elegida : {word_choice}")
n,end,guess,letter,var,Buble=0,0,"",[],"",0
sum=[]
for display in word_choice:
    letter.append("_")
def Winner_default():
    global n,lifes,end,sum,Buble
    for voice in word_choice: 
        Buble+=1  
        if voice==guess:
            letter.insert(n,voice)
            letter.pop(n+1)
        elif voice!=guess and Buble==len(word_choice):
            end=letter.count(guess)
            if end==0 and lifes>=0:
                end="vacio"
                lifes-=1
                sum.append(end)
                print(f"{stages[lifes]}")
            else :
                print("you lose")
        elif "vacio" not in sum and Buble==len(word_choice) :
            if lifes>=0:
                lifes-=1
                print(f"{stages[lifes]}")
            else:
                print("you lose")
        n+=1
    Buble=0
    print(f"{letter}")
while not var==word_choice :
    if lifes==0:
        break
    for lol in range(0,len(word_choice)):
        completed+=letter[lol]
        var=completed
    guess=input("Adivina que palabra sigue: ").lower()
    completed=""
    n=0
    Winner_default()
if lifes ==0:
      print("You Lose")
else:
      print("You Win")
