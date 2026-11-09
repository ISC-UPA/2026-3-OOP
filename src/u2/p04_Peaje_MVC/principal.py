import os, sys
from base_datos import consultarPeaje
from vista_peaje import VistaPeaje
from controlador_peaje import Peaje
from peaje import Peaje


if __name__ == '__main__':
    model = consultarPeaje('Norte')
    view = VistaPeaje()
    controller = Peaje(model, view)
    controller.imprimir()

