alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def encrypt():
    n=0
    Crypt=""
    for i in text :
        n=0
        for id in range (0,len(alphabet)):
            n+=1
            if n>=27:
                n= 1
            elif i ==alphabet[id] :
                indice= id + shift
                Crypt+=alphabet[indice]
                n= 0
            elif n==len(alphabet):
                Crypt+=" "
    print(f"Su Valor Encryptado es {Crypt}")
if direction=="encode":
    encrypt()
        

          


