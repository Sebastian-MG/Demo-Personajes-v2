#-------------------------------------------------------------------------------
# Name:        ClasesJuego
# Purpose:     Ninguno, una nota
#
# Author:      Pedro Barr, Felipe, Sebastian Mancera
#
# Created:     19/09/1999
# Copyright:   (c) lenovo 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from pygame import sprite, image
import random

#Clase padre equipamento (Dispuesta a cambios, y a ser extendible)
class Equipamento(sprite.Sprite):

    '''El atributo efecto podria ser confus
    en la ejecucion, posiblemente lo reemplazemos'''
    _material=None
    _sprites = None
    _efecto = None
    _durabilidad = None

    def __init__(self):
        sprite.Sprite.__init__(self)

    #getters (obviamente)
    def getMaterial(self) -> str:
        return self._material

    def getSprites(self) -> dict:
        return self._sprites

    def getEfecto(self):
        return self._efecto

    def getDurabilidad(self) -> int:
        return self._durabilidad

    #setters (obviamente)
    def setMaterial(self, mat: str):
        self._material = mat

    def setSprites(self, sprts: dict):
        self._sprites = sprts

    def setEfecto(self, efect):
        self._efecto = efect

    def setDurabilidad(self, dureza: int):
        self._durabilidad = dureza

#Clase hijo Escudo (Dispuesta a cambios)
class Escudo(Equipamento):

    #constructor con el unico atributo propio
    def __init__(self):
        sprite.Sprite.__init__(self)
        ''' el radio se supone que se usara en
        la implementacion'''
        self._radio = None

    #getters (obviamente)
    def getRadio(self):
        return self._radio

    #setters (obviamente)
    def setRadio(self, rad):
        self._radio = rad

    def update(self, direc: str, hand: list):
        self.image = image.load(self.getSprites() + direc + ".gif")
        self.rect=self.image.get_rect()
        self.rect.center = (hand[0], hand[1])
        #self.rect.left = hand[0]
        #self.rect.top =  hand[1]

    #metodo para dibujarse en una ventana
    def draw(self, marco):
        marco.blit(self.image, self.rect)

#Clase hijo Arma (Dispuesta a cambios, y a ser extendible)
class Arma(Equipamento):

    #constructor con el unico atributo propio
    def __init__(self):
        sprite.Sprite.__init__(self)
        #Atributo propio de la clase hijo
        self._factorAtaque = None

    #getters (obviamente)
    def getFactAtaque(self):
        return self._factorAtaque

    #setters (obviamente)
    def setFactAtaque(self, atk):
        self._factorAtaque = atk

    def update(self, direc: str, hand: list):
        self.image = image.load(self.getSprites() + direc + ".gif")
        self.rect=self.image.get_rect()
        self.rect.center = (hand[0], hand[1])

    #metodo para dibujarse en una ventana
    def draw(self, marco):
        marco.blit(self.image, self.rect)

#Clase principal Personaje (Dispuesta a cambios)
class Personaje(sprite.Sprite):

    #constructor con los atributos propios
    def __init__(self):
        sprite.Sprite.__init__(self)
        '''posible implementacion de _velocidad, _direccion, _objetivo'''
        self._tipo=None
        self._equipamento={}
        self._sprites = None
        self._ruido = None
        self._decorados = {}
        self._posicion=None
        self._velocidadX = 0
        self._velocidadY = 0
        self._direccion = 0
        self.ind = 0
        self._vida = 100
        self._fuerza = 3

    #getters (obviamente)
    def getTipo(self) -> str:
        return self._tipo

    def getSprites(self) -> list:
        return self._sprites

    def getRuidos(self) -> list:
        return self._ruido

    def getDecorados(self) -> list:
        return self._decorados

    def getEquipamento(self) -> list:
        return self._equipamento

    def getPosicion(self) -> list:
        return self._posicion

    def getXVel(self) -> int:
        return self._velocidadX

    def getYVel(self) -> int:
        return self._velocidadY

    def getDireccion(self) -> int:
        return self._direccion

    def getVida(self) -> int:
        return self._vida

    def getFuerza(self) -> int:
        return self._fuerza

    #setters (obviamente)
    def setTipo(self, tip: str):
        self._tipo = tip

    def setSprites(self, sprts: list):
        self._sprites = sprts

    def setRuido(self, rudo: list):
        self._ruido = rudo

    def setDecorados(self, decor: list):
        self._decorados = decor

    def setEquipamento(self, equipo: list):
        self._equipamento = equipo

    def setPosicion(self, pos: list):
        self._posicion = pos

    def setXVel(self, x: int):
        self._velocidadX = x

    def setYVel(self, y: int):
        self._velocidadY = y

    def setDireccion(self, direct: int):
        self._direccion = direct

    def setVida(self, vita: int):
        self._vida = vita

    def setFuerza(self, mayfourth: int):
        self._fuerza = mayfourth

    #metodos propios de la clase

    #vacia el inventario de objetos
    def clearEquipamento(self) -> None:
        self.setEquipamento({})

    #Añade o remplaza un objeto en el inventario
    def addEquipo(self, key, equipo):
        self._equipamento[str(key)] = equipo

    #modifica un objeto en el inventario, llamando al metodo addEquipo
    def modEquipo(self, key, equipo):
        self.addEquipo(key, equipo)

    #elimina un objeto del inventario
    def popEquipo(self, key):
        self._equipamento.pop(str(key))

    #getter de la cantidad de objetos en el inventario (sin manos)
    def getLenEquipamento(self) -> int:
        n=0
        if "RH" in self._equipamento:
            n+=1
        if "LH" in self._equipamento:
            n+=1
        return len(self._equipamento)-n

    #getter para un objeto en el inventario
    def getEquipo(self, key: str) -> Equipamento:
        return self._equipamento[str(key)]

    #getters de la posicion en X y Y
    def getXPos(self) -> int:
        return self._posicion[0]

    def getYPos(self) -> int:
        return self._posicion[1]

    #setters de la posicion X y Y:
    def setXPos(self, x: int):
        self._posicion[0] = x

    def setYPos(self, y: int):
        self._posicion[1] = y

    #añade un decorador
    def addDecor(self, clave: str, decor: sprite):
        self._decorados[str(clave)] = decor

    #elimina un decorador
    def popDecor(self, clave: str):
        self._decorados.pop(str(clave))

    #devuelve la cantidad de decoradores
    def getLenDecor(self) -> int:
        n=0
        if "Smbr" in self._decorados:
            n+=1
        return len(self._decorados)-n

    #Modificador de vida
    def modVida(self, modif: int):
        self.setVida(self.getVida() + modif)

    #Metodo que define si se ha chocado con algun objeto
    def choque(self, obj) -> bool:
        if self.rect.colliderect(obj):
            return True
        return False

    #Metodo que invierte la direccion en la que va el personaje
    def invertDir(self, direct: int) -> int:
        if direct == 0:
            return random.randint(1,8)
        if direct <= 4:
            n=4
        elif direct <= 8:
            n=-4
        return direct + n

    #Metodo que hace a los NPCs moverse solos por el ambiente
    def existir(self, direct: int, factor_cambio: int, objetivo=None):
        if factor_cambio == 10:
            direct = self.invertDir(self._direccion)
        elif factor_cambio <= 5:
            direct = 0
        elif factor_cambio <= 8:
            direct = self._direccion
        else:
            direct = direct
        if direct==0:
            self.setXVel(0)
            self.setYVel(0)
            self.ind = 0
        elif direct==1:
            self.setXVel(-5)
            self.setYVel(-5)
            self.images = self.getSprites()["U"]
        elif direct==2:
            self.setXVel(0)
            self.setYVel(-5)
            self.images = self.getSprites()["U"]
        elif direct==3:
            self.setXVel(5)
            self.setYVel(-5)
            self.images = self.getSprites()["R"]
        elif direct==4:
            self.setXVel(5)
            self.setYVel(0)
            self.images = self.getSprites()["R"]
        elif direct==5:
            self.setXVel(5)
            self.setYVel(5)
            self.images = self.getSprites()["D"]
        elif direct==6:
            self.setXVel(0)
            self.setYVel(5)
            self.images = self.getSprites()["D"]
        elif direct==7:
            self.setXVel(-5)
            self.setYVel(5)
            self.images = self.getSprites()["L"]
        elif direct==8:
            self.setXVel(-5)
            self.setYVel(0)
            self.images = self.getSprites()["L"]
        self._direccion = direct

    #Metodos para hallar el centro de la mano izquierda y derecha
    def centroLH(self, direct: str, imag: int) -> list:
        if direct=="U":
            if imag==0:
                aux_X=5
                aux_Y=40
            elif imag==1:
                aux_X=7
                aux_Y=40
            elif imag==2:
                aux_X=5
                aux_Y=34
        elif direct=="D":
            if imag==0:
                aux_X=32
                aux_Y=40
            elif imag==1:
                aux_X=32
                aux_Y=36
            elif imag==2:
                aux_X=30
                aux_Y=40
        elif direct=="L":
            if imag==0:
                aux_X=16
                aux_Y=41
            elif imag==1:
                aux_X=13
                aux_Y=41
            elif imag==2:
                aux_X=20
                aux_Y=43
        elif direct=="R":
            if imag==0:
                aux_X=21
                aux_Y=41
            elif imag==1:
                aux_X=25
                aux_Y=41
            elif imag==2:
                aux_X=17
                aux_Y=42
        return [aux_X,aux_Y]

    def centroRH(self, direct: str, imag: int) -> list:
        if direct=="U":
            if imag==0:
                aux_X=32
                aux_Y=40
            elif imag==1:
                aux_X=33
                aux_Y=34
            elif imag==2:
                aux_X=30
                aux_Y=40
        elif direct=="D":
            if imag==0:
                aux_X=5
                aux_Y=40
            elif imag==1:
                aux_X=7
                aux_Y=40
            elif imag==2:
                aux_X=5
                aux_Y=36
        elif direct=="L":
            if imag==0:
                aux_X=16
                aux_Y=41
            elif imag==1:
                aux_X=23
                aux_Y=42
            elif imag==2:
                aux_X=14
                aux_Y=40
        elif direct=="R":
            if imag==0:
                aux_X=22
                aux_Y=41
            elif imag==1:
                aux_X=18
                aux_Y=43
            elif imag==2:
                aux_X=24
                aux_Y=41
        return [aux_X,aux_Y]

    def update(self):
        if self.getXVel()==0 and self.getYVel()==0:
            self.image = image.load(self.images[0])
            aux_ind=0
        else:
            self.ind +=1
            aux_vel = 3
            if self.ind <= aux_vel:
                self.image = image.load(self.images[1])
                aux_ind=1
            elif self.ind <= 2*aux_vel:
                self.image = image.load(self.images[2])
                aux_ind=2
            else:
                self.image = image.load(self.images[2])
                aux_ind=2
                self.ind = 0
        self.rect=self.image.get_rect()
        self.rect.left = self.getXPos() + self.getXVel()
        self.setXPos(self.rect.left)
        self.rect.top = self.getYPos() + self.getYVel()
        self.setYPos(self.rect.top)
        if self.getSprites()["U"] is self.images:
            aux_dir="U"
        if self.getSprites()["D"] is self.images:
            aux_dir="D"
        if self.getSprites()["L"] is self.images:
            aux_dir="L"
        if self.getSprites()["R"] is self.images:
            aux_dir="R"
        centro = self.centroLH(aux_dir,aux_ind)
        if 'LH' in self.getEquipamento().keys() and self.getEquipo('LH'):
            self.getEquipo("LH").update(aux_dir,[self.getXPos() + centro[0], self.getYPos() + centro[1]])
        centro = self.centroRH(aux_dir,aux_ind)
        if 'RH' in self.getEquipamento().keys() and self.getEquipo('RH'):
            self.getEquipo("RH").update(aux_dir,[self.getXPos() + centro[0], self.getYPos() + centro[1]])

    def drawSombra(self, marco):
        marco.blit(image.load(self.getDecorados()["Smbr"]), (self.getXPos() + 5 ,self.getYPos() + 42))

    #metodo para dibujarse en una ventana
    def draw(self, marco):
        self.drawSombra(marco)
        if self.getSprites()["U"] is self.images:
            if 'LH' in self.getEquipamento().keys() and self.getEquipo('LH'):
                self.getEquipo("LH").draw(marco)
            if 'RH' in self.getEquipamento().keys() and self.getEquipo('RH'):
                self.getEquipo("RH").draw(marco)
            marco.blit(self.image, self.rect)
        if self.getSprites()["D"] is self.images:
            marco.blit(self.image, self.rect)
            if 'RH' in self.getEquipamento().keys() and self.getEquipo('RH'):
                self.getEquipo("RH").draw(marco)
            if 'LH' in self.getEquipamento().keys() and self.getEquipo('LH'):
                self.getEquipo("LH").draw(marco)
        if self.getSprites()["L"] is self.images:
            if 'RH' in self.getEquipamento().keys() and self.getEquipo('RH'):
                self.getEquipo("RH").draw(marco)
            marco.blit(self.image, self.rect)
            if 'LH' in self.getEquipamento().keys() and self.getEquipo('LH'):
                self.getEquipo("LH").draw(marco)
        if self.getSprites()["R"] is self.images:
            if 'LH' in self.getEquipamento().keys() and self.getEquipo('LH'):
                self.getEquipo("LH").draw(marco)
            marco.blit(self.image, self.rect)
            if 'RH' in self.getEquipamento().keys() and self.getEquipo('RH'):
                self.getEquipo("RH").draw(marco)

#pruebas del manejo de las clases
def main():
    #blablabla, creamos un personaje vacio de nombre generico
    pers = Personaje()
    pers.setTipo("Link")
    pers.setSprites(["",""])
    pers.setRuido([""])
    pers.setPosicion([0,0])

    '''Añadimos un arma y un escudo generico a su
    mano derecha (RH) y su mano izquierda (LH)'''
    pers.addEquipo("RH", Arma())
    pers.addEquipo("LH", Escudo())

    '''Añadimos un objetos genericos en posiciones
    genericas de su inventario'''
    for i in range(3):
        pers.addEquipo(pers.getLenEquipamento()+1,Equipamento())

    '''Llenamos genericamente los atributos de
    los objetos en su inventario'''
    for keys in pers.getEquipamento():
        pers.getEquipo(keys).setMaterial("Madera")
        pers.getEquipo(keys).setDurabilidad(50)
        if keys=="LH":
            pers.getEquipo(keys).setRadio(1)
        elif keys=="RH":
            pers.getEquipo(keys).setFactAtaque(5)

    '''eliminamos el elemento en posicion 3
    del inventario (para probar el metodo pop)'''
    pers.popEquipo(3)

    '''eliminamos todo en el inventario
    (para probar los metodos get, set y clear )'''
    dicc=pers.getEquipamento()
    pers.clearEquipamento()
    pers.setEquipamento(dicc)

    '''remplazamos el escudo generico por uno más
    especifico (para probar el metodo mod)'''
    sqdo=Escudo()
    sqdo.setMaterial("Metal")
    sqdo.setDurabilidad(70)
    sqdo.setEfecto(None)
    sqdo.setRadio(5)
    pers.modEquipo("LH",sqdo)

    '''imprimimos todo para validar que todos
    los cambios han sido correctos (easy peasy)'''
    print(pers.getTipo(),":",pers.getSprites(),",",pers.getRuidos())
    for keys in pers.getEquipamento():
        print(keys,"->",pers.getEquipo(keys).getMaterial(), pers.getEquipo(keys).getDurabilidad(), end=" ")
        if keys=="LH":
            print(pers.getEquipo(keys).getRadio())
        elif keys=="RH":
            print(pers.getEquipo(keys).getFactAtaque())
        else:
            print()
    pass

if __name__ == '__main__':
    main()
