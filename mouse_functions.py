import globais
import numpy as np
from  math import sin, cos, radians
oldx = 0
oldy = 0

def mouseMoveu(x, y):
    global oldy, oldx
    deltax = x - oldx
    deltay = y - oldy

    ondeRodar = np.cross(globais.viewDirection, globais.up)
    matrizRotacao = rotationMatrix(-deltax * globais.passo_rotacao, globais.up) *  rotationMatrix(-deltay * globais.passo_rotacao, ondeRodar)
    globais.viewDirection = np.transpose( matrizRotacao * np.transpose(globais.viewDirection))
    oldy = y
    oldx = x

def rotationMatrix( angulo, vetor ):
    vetor[0,2]= 1
    x = vetor.item(0)
    y = vetor.item(1)
    mat = np.mat([
        [cos(angulo), -sin(angulo), x-(x*cos(angulo))+(y*sin(angulo))],
        [sin(angulo),  cos(angulo), y-(y*cos(angulo))-(x*sin(angulo))],
        [0,0,1]
        ])

    return mat

