# Demo-Personajes-v2
### Juan Sebastian Mancera Gaitán 20171020047
### Luis Felipe Corredor 20171020056
### Pedro Enrique Barrera 20171020057

#### El ejecutable del juego es el archivo Launcher.py
#### Juego realizado en Python 3 junto a las siguientes librerias:

copy => Prototype

pygame => ClasesJuego, Launcher, Game, Decorator, Composite, Pantalla

gc => Launcher, Game, Pantalla, StrategyJuego

os => Pantalla, Game

tkinter => Launcher

PIL => LAuncher

enum=> Tipos

functools => Launcher

math => Launcher

random => ClasesJuego, Launcher, Game, Decorator, Composite, Pantalla

##### Modulo Builder : 

Para la version 2 se amplio la clase Builder_Sprites para que construyera 4 objetos en diferentes direcciones, cada una agregada a un diccionario que era atributo propio privado de la clase Builder_Sprites, por su parte el modulo Builder_Sonidos no se expandió.
![]()


##### Modulo Abstract:

Se reemplaza el patrón abstract Factory que se habia planteado de forma diferente para la version 1, esta version 2 solo posee como dependencia el modulo Builder y su funcionamiento es realizar su contrucción a través de los Builders tomandolos como productos y almacenandolos en un directorio que es su atributo propio.

Para esta versión 2 la factoria no crea un personaje, solo crea las partes con las cuales el prototype realizara el armado de cada personaje.

![]()

#### Modulo ClasesJuego

Para versión 2 se replanteo el funcionamiento de las clases base haciendo que estas directamente fueran heredadas de la clase Sprite, se añadieron mas atributos para que la jugabilidad pudiera darse correspondiente a la extension de la clase Builder, en las 4 direcciones con velocidad en X,Y y métodos para que pudiera actualizarse en una pantalla que fuera otorgada.

![]()

#### Modulo Prototype:

Para version 2 se reestructuro el funcionamiento de la clase Prototype, ahora creandole dependencia a clasesJuego y siendo el encargado de fusionar lo traido a la clase Abstract y a la clase ClasesJuego creando un personaje totalmente jugable con los Sprite que traen las factorias de la clase Abstract.

Se crea un personaje prototipo,un arma prototipo y un escudo prototipo al acceder a las factorias y se inicializa un objeto estatico llamado ObjectFactory el cual provee los prototipos y realiza un método de fácil acceso para la creacion de los mismos.

![]()


#### Modulo Composite(Modulo de Prueba):

En este módulo se intentó recrear el concepto del patrón Composite graficando en pantalla un personaje que trae sus Builders directamente y los settea sin hacer uso de alguna Factoria o Prototype solo para comprobar el resultado de graficar en pantalla y sobreponer la sombra del porsonaje, el personaje y sus armas.


![]()


#### Modulo Decorator 


































![]()
