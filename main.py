from OpenGL.GLUT import *        # Module For The GLUT Library
from OpenGL.GL import *        # Module For The OpenGL32 Library
from OpenGL.GLU import *    # Module For The GLu32 Library
import time             # Module for sleeping.
from math import *            # Module for trigonometric functions.
from gl_functions import *
from globais import *
from objloader import *
from mouse_functions import *
from objeto import *
import sys            


def main():
        global janela

	#Inicia o OpenGl
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE|GLUT_DEPTH|GLUT_ALPHA)
	glutInitWindowSize(640, 480)
	janela = glutCreateWindow("Projeto de CG")

        adiciona_objeto( objeto("res/obj/teapot.obj", scale=[0.5,0.5,0.5]) )
	#globais.chaleira = ObjLoader("res/obj/teapot.obj")
	#globais.planta = ObjLoader("res/obj/planta.obj")

	#Inicializa a Janela
	InitGL(640, 480)

	#Registra os callbacks
	glutDisplayFunc(desenharCena)   #funcao de desenho
	glutReshapeFunc(redimensionar)  #funcao de redimensionamento
	glutIdleFunc(desenharCena)      #funcao quando em espera    
	glutKeyboardFunc(teclaApertada) #funcao de quando uma tecla e apertada
	glutKeyboardUpFunc(teclaSolta)  #funcao de quando uma tecla e solta
        glutPassiveMotionFunc(mouseMoveu)
	#Inicia a execucao
	glutMainLoop()

if __name__ == "__main__":
	main()
