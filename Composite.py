#-------------------------------------------------------------------------------
# Name:        módulo1
# Purpose:
#
# Author:      lenovo
#
# Created:     10/11/2019
# Copyright:   (c) lenovo 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

''' importe de Clases Bases, Builder, pygame y aleatorio'''
from ClasesJuego import *
from Builder import *
import pygame as pyg
import random

'''cuarto de pruebas de personajes'''
def juego(PLAYER):
    DIRS = ["D", "U", "R", "L"]
    VENTANA=pyg.display.set_mode((400,300))
    pyg.display.set_caption("fafds")

    while True:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()
                quit()
            if event.type == pyg.KEYUP:
                if event.key==pyg.K_ESCAPE:
                    pyg.quit()
                    quit()

        PLAYER.images = PLAYER.getSprites()[DIRS[random.randint(0,3)]]
        PLAYER.setXVel(random.randint(-3,3))
        PLAYER.setYVel(random.randint(-3,3))
        PLAYER.update()
        PLAYER.setPosicion([181,123])

        VENTANA.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

        #Draw
        PLAYER.draw(VENTANA)

        pyg.display.update()

        pyg.time.Clock().tick(1)
    pass

def main():
    pyg.init()

    arma=Arma()
    arma.setMaterial("Madera")
    arma.setSprites("Sprites/Armas/" + arma.getMaterial() + "/")

    shel=Escudo()
    shel.setMaterial("Madera")
    shel.setSprites("Sprites/Escudos/" + shel.getMaterial() + "/")

    pers = Personaje()
    pers.setTipo("Pruebas")
    build = BuilderSprites()
    build.setRuta("Personajes/" + pers.getTipo())
    build.MethodDirector()
    pers.setSprites(build.getBuild())
    build = BuildSonidos()
    build.setRuta("Gritos/" + pers.getTipo())
    build.MethodDirector()
    pers.setRuido(build.getBuild())
    pers.addDecor("Smbr", "Sprites/Efectos/Smbr.gif")
    pers.setPosicion([181,123])
    pers.addEquipo("RH", arma)
    pers.addEquipo("LH", shel)
    pers.images = pers.getSprites()["D"]
    pers.update()

    juego(pers)

    pass

if __name__ == '__main__':
    main()
