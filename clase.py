import sys

cadena = "TesT" 
cadena_minuscula = cadena.lower() 
print(cadena) 
print(cadena_minuscula) 
#Para terminar, si escribimos esto:
cadena = "TesT" 
cadena = cadena.lower() 
print(cadena)

"""
función
Datos
Algoritimo
Return
(1 problema, una funcion )

"""
cadena="abcdefghtaaaaAahhh"
fragmento="a" or "A"
def posiciones(cadena, fragmento) : 
    posicion = -1 
    for i in range(cadena.count(fragmento)): 
        posicion = cadena.index (fragmento, posicion + 1) 
        print("Posición n°{}:{}".format( i + 1, posicion)) 
    return posicion


posiciones(cadena, fragmento)

