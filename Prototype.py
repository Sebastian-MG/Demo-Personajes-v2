#-------------------------------------------------------------------------------
# Name:        Prototype y ObjectFactory
# Purpose:     Ninguno, una nota
#
# Author:      Pedro Barr, Felipe, Sebastian Mancera
#
# Created:     19/09/1999
# Copyright:   (c) Estudiantes 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

'''importar copy, AbstractFactory y las Clases Base'''
import copy
from Abstract import *
from ClasesJuego import *

#Clase abstracta Prototype
class Prototype:
    #Prototipo que se generara
    _prototipo = None

    #getter (Obviously)
    def getPrototipo(self):
        return self._prototipo

    #metodo para clonar, se debe sobreescribir
    def clone(self):
        pass

#Clase para un prototipo generico de personaje
class PrototipoPersonaje(Prototype):

    def __init__(self):
        self._prototipo = Personaje()

    #metodo para clonar a profundidad sobreescrito
    def clone(self):
        return copy.deepcopy(self)

'''Clase para un prototipo de un personaje,
con tipo, Sprites y sonidos inicializados'''
class PersonajePruebas(Prototype):

    def __init__(self):
        #inicializar el prototipo
        self._prototipo = Personaje()
        self._prototipo.setTipo("Pruebas")

        #inicializar fabrica abstracta
        fabrica=FactoryPersonaje()

        #inicializar constructores
        builders = fabrica.getBuiders()

        #settear y construir cada constructor
        builders["Sprt"].setRuta("Personajes/Pruebas")
        builders["Sprt"].MethodDirector()
        builders["Sond"].setRuta("Gritos/Pruebas")
        builders["Sond"].MethodDirector()

        #añadir sprites, sonidos (y sombras) al prototipo
        self._prototipo.setSprites(builders["Sprt"].getBuild())
        self._prototipo.setRuido(builders["Sond"].getBuild())

    #metodo para clonar a profundidad sobreescrito
    def clone(self):
        return copy.deepcopy(self)

#Clase para un prototipo generico de Equipamento
class PrototipoEquipamento(Prototype):

    def __init__(self):
        self._prototipo = Equipamento()

    #metodo para clonar a profundidad sobreescrito
    def clone(self):
        return copy.deepcopy(self)

#Clase para un prototipo de un escudo de madera
class EscudoMadera(Prototype):

    def __init__(self):
        #inicializar el prototipo
        self._prototipo = Escudo()
        self._prototipo.setMaterial("Madera")
        self._prototipo.setDurabilidad(25)

        #añadir sprites al prototi
        self._prototipo.setSprites("Sprites/Escudos/" + self._prototipo.getMaterial() + "/")

    #metodo para clonar a profundidad sobreescrito
    def clone(self):
        return copy.deepcopy(self)

#Clase para un prototipo de un arma de madera
class ArmaMadera(Prototype):

    def __init__(self):
        #inicializar el prototipo
        self._prototipo = Arma()
        self._prototipo.setMaterial("Madera")
        self._prototipo.setDurabilidad(25)
        self._prototipo.setFactAtaque(19)

        #añadir sprites al prototi
        self._prototipo.setSprites("Sprites/Armas/" + self._prototipo.getMaterial() + "/")

    #metodo para clonar a profundidad sobreescrito
    def clone(self):
        return copy.deepcopy(self)

'''clase abstracta ObjectFactory,
para llamar a los prototipos desde
cualquier clase con solo inicializar
la factoria (esta clase rompe el principio
Abierto-Cerrado por fuerza)'''
class ObjectFactory:

    @staticmethod
    def initialize():
        '''al inicializar la factoria se
        inicializan todos los posibles prototipos'''
        ObjectFactory._Personaje = PrototipoPersonaje()
        ObjectFactory._Prueba = PersonajePruebas()
        ObjectFactory._Equipamento = PrototipoEquipamento()
        ObjectFactory._EscudoMadera = EscudoMadera()
        ObjectFactory._ArmaMadera = ArmaMadera()

    @staticmethod
    def getTipoPersonaje(tipo: str) -> Personaje():
        '''getter para devolver cualquier prototipo
        de personaje al pasar el tipo requerido'''
        if tipo==None:
            pass
        elif tipo.upper()=="PRUEBA":
            return ObjectFactory.getPrueba()
        return ObjectFactory.getPersonaje()

    #getters (Obviously)
    @staticmethod
    def getPersonaje() -> Personaje():
        return ObjectFactory._Personaje.clone().getPrototipo()

    @staticmethod
    def getPrueba() -> Personaje():
        return ObjectFactory._Prueba.clone().getPrototipo()

    @staticmethod
    def getEquipamento() -> Personaje():
        return ObjectFactory._Equipamento.clone().getPrototipo()

    @staticmethod
    def getEscudoMadera() -> Personaje():
        return ObjectFactory._EscudoMadera.clone().getPrototipo()

    @staticmethod
    def getArmaMadera() -> Personaje():
        return ObjectFactory._ArmaMadera.clone().getPrototipo()

#pruebas del manejo de las clases
def main():
    #inicializar la factoria, y por ende los prototipos
    ObjectFactory.initialize()

    #inicializar un personaje generico, sin tipo, Sprites ni sonidos
    pers1=ObjectFactory.getPersonaje()

    #inicializar un personaje de tipo prueba, con Sprites y sonidos
    pers2=ObjectFactory.getPrueba()

    '''añadir un escudo de madera (con
    Sprites) a la mano izquierda (LH)
    del personaje'''
    pers2.modEquipo("LH",ObjectFactory.getEscudoMadera())

    '''añadir un arma de madera (con
    Sprites) a la mano derecha (RH) del
    personaje'''
    pers2.modEquipo("RH",ObjectFactory.getArmaMadera())

    '''añadir un objeto generico (sin
    Sprites) al inventario del
    personaje'''
    pers2.modEquipo(pers2.getLenEquipamento(),ObjectFactory.getEquipamento())
    for keys in pers2.getEquipamento():
        print(pers2.getEquipo(keys))
    pass

if __name__ == '__main__':
    main()