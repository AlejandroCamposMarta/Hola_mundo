import random
numtot = int
carta1= int
carta2= int
cartaextra= str
roboext= int

carta1=random.randint(1,13)
carta2=random.randint(1,13)
print (carta1)
print (carta2)

numtot=(carta1+carta2)
while numtot<21:
    print(("Quieres otra carta?"))
    cartaextra (input("Si/No\n"))

    if cartaextra== "si":
        roboext=random.randint(1,21)
        print("El numero de su carta es:"+roboext)
        numtot= (numtot+roboext)
    elif cartaextra== "no":
        break
        
    else:
        print("\nInserte con su eleccion con la primer letra minuscula")
    