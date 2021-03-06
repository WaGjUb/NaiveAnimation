from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import globais
from key_functions import *
from objeto import *
import sys

def desenharCena():#funcao de desenho

	#Atualiza o Pool de eventos
	atualizar_eventos()

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);


        res = np.add(globais.viewPos, globais.viewDirection)

        glLoadIdentity()
        gluLookAt(globais.viewPos.item(0),
                  globais.viewPos.item(1),
                  globais.viewPos.item(2),
                  res.item(0),
                  res.item(1),
                  res.item(2),
                  globais.up.item(0),
                  globais.up.item(1),
                  globais.up.item(2))
        	

        glLightfv(GL_LIGHT0, GL_POSITION, (1.0, 1.0, 1.0, 1.0))

        desenha_objetos()
	glutSwapBuffers()

def redimensionar(largura, altura):
	if altura == 0:
		altura = 1
	glViewport(0, 0, largura, altura)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(45.0, float(largura)/float(altura), 0.1, 100.0)
	glMatrixMode(GL_MODELVIEW)

def teclaSolta(tecla, x, y):#funcao de quando uma tecla e solta
	print("tecla solta "+str(tecla)+" x "+str(x)+" y "+str(y))
	try:
		fila_teclas.remove(tecla)
		atualizar_eventos()
	except KeyError:
		print("Como voce soltou a tecla {} sem aperta-la ?".format(tecla))

def teclaApertada(tecla, x, y):#funcao de quando uma tecla e apertada
	print("tecla "+str(tecla)+" x "+str(x)+" y "+str(y))
	fila_teclas.add(tecla)
	atualizar_eventos()

def teclaEspecial(tecla, x, y):#funcao para teclas especiais
	print("tecla especial "+str(tecla)+" x "+str(x)+" y "+str(y))

def InitGL( altura, largura):
	glClearColor(0.0,0.0,0.0,0.0)     #cor de fundo branca
	glClearDepth(1.0)        #abilita limpar o buffer de prof.

	glShadeModel(GL_SMOOTH)        #Configura como sera de. a ilum.
	glDepthFunc(GL_LESS)        #Funcao usada no depth-test
	glEnable(GL_DEPTH_TEST)        #Habilita o deph-test

	glMatrixMode(GL_PROJECTION)    #Projecao perspectiva
	glLoadIdentity()        #reseta a matriz de projecao
	#gluPerspective angulo_de_visao aspecto plano_near plano_far
	gluPerspective(45.0, float(largura/altura), 0.1, 100.0)
	glMatrixMode(GL_MODELVIEW)    #Projecao perspectiva
        luzAmbiente()


def luzAmbiente():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)

    glLightfv(GL_LIGHT0, GL_POSITION, (0.0, 1.0, 0.0, 0.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.0, 0.0, 0.0, 1.0))
    glLightfv(GL_LIGHT1, GL_SPECULAR, (1.0, 0.0, 0.0, 1.0))
    glLightfv(GL_LIGHT1, GL_DIFFUSE, (1.0, 0.0, 0.0, 1.0))
