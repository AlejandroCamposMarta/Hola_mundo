#Tarea_14
#Alejandro Campos Marta
#358436

from tkinter import*

triangulo=Tk()

triangulo.geometry("500x500")
triangulo.title("358436, Alejandro Campos Marta")

vacio=Label(triangulo, text="")
vacio.pack()

labelins=Label(triangulo,text="Introduzca la base y la altura deseada para el triangulo: ")
labelins.pack()

vacio=Label(triangulo, text="")
vacio.pack()

labelbase=Label(triangulo,text="Base")
labelbase.pack()

base=Entry(triangulo) #Aqui va la base
base.pack()

multip=Label(triangulo, text="x")
multip.pack()

labelalt=Label(triangulo,text="Altura")
labelalt.pack()

altura=Entry(triangulo) #Aqui va la altura
altura.pack()

vacio=Label(triangulo,text="")
vacio.pack()

resultado=Label(triangulo, text="El area es: ")
resultado.pack()

#def donde va la correcion para la introduccion de las letras y las operacion para el boton
def areatraingulo():
    try:
        b=float(base.get())
        h=float(altura.get())
        artrian=b*h/2
        resultado["text"]= "El area es: "+ str(artrian)
    except ValueError:
        resultado["text"]= "Ingrese valores numericos por favor"   
    almacendat= open("pruebaproyecto.txt", "a")
    artrian=b*h/2
    almacendat.write("Base: "+str(b)+ ", " +"Altura: "+str(h)+ ", " +"Area triangulo: "+(str(artrian)+"\n"))
    almacendat.close()


operacion=Button(triangulo, text="Resultado", command=areatraingulo)
operacion.pack()

triangulo.mainloop()