alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
end="Y"
def Cesa_Crypt(shift_e):
    decrypt=""
    if direction=="decode":
        shift_e*= -1
    for letters in text:
        indice=alphabet.index(letters)
        indice_old=indice+shift_e
        if indice_old>26 or indice_old<0:
            indice_old=indice_old%26   
        decrypt+=alphabet[indice_old]
    print(f"su texto {direction} es {decrypt}")
while end== "Y" :
    Cesa_Crypt(shift)
    end=input("Quiere Seguir realizando otra operacion: " +"Y/N ")
    
