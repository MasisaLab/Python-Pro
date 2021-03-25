from art import logo
print(logo) 
#Add
def add(n1,n2):
    return n1 +n2 
#Substract
def Sub(n1,n2):
    return n1- n2
#Multiply
def Mult(n1,n2):
    return n1*n2
#Divid
def Divi(n1,n2):
    return n1/n2
def calculadora():   
    calculate={"+":add, "-":Sub,"*":Mult,"/":Divi }
    nu1=float(input("Ingrese el primer numero "))
    def call():
        for i in calculate:
            print(i)
    fas="Y"
    while fas=="Y" :
        call()
        n=input("Ingrese el operador a realizar ")
        nu2=float(input("Ingrese el segundo numero "))
        finish =calculate[n](nu1,nu2)
        print(f" {nu1} {n} {nu2} = {finish}")
        fas=input("Quiere seguir realizando operaciones Y o una nueva operacion N: ") 
        if fas=="Y" :
            nu1=finish
        elif fas=="N":
            calculadora()
        else:
            print("hasta luego")
calculadora()