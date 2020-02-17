#-------------------------------------------------------------------------------
# Name:        Decorator
# Purpose:     Ninguno, una nota
#
# Author:      Pedro Barr, Felipe, Sebastian Mancera
#
# Created:     19/09/1999
# Copyright:   (c) lenovo 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

'''importe de Clases Bases'''
from ClasesJuego import *

'''Notacion: Dc + (Objeto a decorar +) Nombre del decorador
que hereda la clase del objeto a decorar, para poder usarlo
como un objeto de esa clase en la ejecucion'''

#Decorador de Arma, que afecta el efecto que devuelve el arma
class DcArmaDobleFilo(Arma):

    #construye el objeto igual al que le es dado
    def __init__(self, arma: Arma):
        self._material = arma.getMaterial()
        self._sprites = arma.getSprites()
        self._efecto = arma.getEfecto()
        self._durabilidad = arma.getDurabilidad()
        self._factorAtaque = arma.getFactAtaque()

    #decorador para que al devolver el efecto sea uno nuevo
    def getEfecto(self) -> str:
        return "Menos uno al portador o lo que sea"

#Decorador de Arma, que afecta el factor de ataque que devuelve el arma
class DcArmaPotenciada(Arma):

    #construye el objeto igual al que le es dado
    def __init__(self, arma: Arma):
        self._material = arma.getMaterial()
        self._sprites = arma.getSprites()
        self._efecto = arma.getEfecto()
        self._durabilidad = arma.getDurabilidad()
        self._factorAtaque = arma.getFactAtaque()

    #decorador para que al devolver el factor de ataque sea el cuadrado
    def getFactAtaque(self) -> int:
        return self._factorAtaque**2

#pruebas del manejo de las clases
def main():
    #se crea un personaje y se le crea un arma generica en la mano derecha (RH)
    pers = Personaje()
    pers.addEquipo("RH", Arma())
    pers.getEquipo("RH").setMaterial("Madera")
    pers.getEquipo("RH").setDurabilidad(50)
    pers.getEquipo("RH").setFactAtaque(5)

    #se imprime para probar
    print(pers.getEquipo("RH").getFactAtaque())
    print(pers.getEquipo("RH").getEfecto())

    '''se modifica el arma, remplazando por
    un arma decorada'''
    pers.modEquipo("RH",DcArmaDobleFilo(DcArmaPotenciada(pers.getEquipo("RH"))))

    #se imprime y se comprueba
    print(pers.getEquipo("RH").getFactAtaque())
    print(pers.getEquipo("RH").getEfecto())
    pass

if __name__ == '__main__':
    main()
