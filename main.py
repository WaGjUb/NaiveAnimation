from OpenGL.GLUT import *        # Module For The GLUT Library
from OpenGL.GL import *        # Module For The OpenGL32 Library
from OpenGL.GLU import *    # Module For The GLu32 Library
import time             # Module for sleeping.
from math import *            # Module for trigonometric functions.
from gl_functions import *
from globais import *
from objloader import *
import sys            


def main():
	global janela

	#Inicia o OpenGl
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE|GLUT_DEPTH|GLUT_ALPHA)
	glutInitWindowSize(640, 480)
	janela = glutCreateWindow("Projeto de CG")

	globais.chaleira = ObjLoader("res/obj/teapot.obj")
	globais.planta = ObjLoader("res/obj/planta.obj")

	#Inicializa a Janela
	InitGL(640, 480)

	#Registra os callbacks
	glutDisplayFunc(desenharCena)   #funcao de desenho
	glutReshapeFunc(redimensionar)  #funcao de redimensionamento
	glutIdleFunc(desenharCena)      #funcao quando em espera    
	glutKeyboardFunc(teclaApertada) #funcao de quando uma tecla e apertada
	glutKeyboardUpFunc(teclaSolta)  #funcao de quando uma tecla e solta
	#Inicia a execucao
	glutMainLoop()

if __name__ == "__main__":
	main()
