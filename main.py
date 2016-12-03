from OpenGL.GLUT import *        # Module For The GLUT Library
from OpenGL.GL import *        # Module For The OpenGL32 Library
from OpenGL.GLU import *    # Module For The GLu32 Library
import time             # Module for sleeping.
from math import *            # Module for trigonometric functions.
from gl_functions import *
from globais import *
import sys            


def main():
    global janela
    #Inicia o OpenGl
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE|GLUT_DEPTH|GLUT_ALPHA)
    glutInitWindowSize(640, 480)
    janela = glutCreateWindow("Projeto de CG")

    #Registra os callbacks
    glutDisplayFunc(desenharCena)   #funcao de desenho
    glutIdleFunc(desenharCena)      #funcao quando em espera    
    glutReshapeFunc(redimensionar)  #funcao de redimensionamento
    glutKeyboardFunc(teclaApertada) #funcao de quando uma tecla e apertada
    glutKeyboardUpFunc(teclaSolta)  #funcao de quando uma tecla e solta
    glutIdleFunc(desenharCena)
    #Inicializa a Janela
    InitGL(640, 480)
    #Inicia a execucao
    glutMainLoop()

if __name__ == "__main__":
    main()
