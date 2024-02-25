b=float(input("Ingrese la base: "))
h=float(input("Ingrese la altura: "))
almacendat= open("pruebaproyecto.txt", "a")
artrian=b*h/2
almacendat.write("Base: "+str(b)+ "," +"Altura: "+str(h)+ "," +"Area triangulo: "+str(artrian))
almacendat.close()
