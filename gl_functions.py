from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import globais
from key_functions import *
import sys

def desenharCena():#funcao de desenho
    #Atualiza o Pool de eventos
    atualizar_eventos()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity()
    glRotatef(globais.yrot, 0,1.0,0)
    glTranslatef(globais.xtrans,globais.ytrans,globais.ztrans)

    #triangulo
    glRotatef(globais.rtri,0.3,1.0,0.5)
    glBegin(GL_TRIANGLES)                    # Start Drawing The Pyramid
   
    glColor3f(1.0,0.0,0.0)            # Red
    glVertex3f( 0.0, 1.0, 0.0)        # Top Of Triangle (Front)
    glColor3f(0.0,1.0,0.0)            # Green
    glVertex3f(-1.0,-1.0, 1.0)        # Left Of Triangle (Front)
    glColor3f(0.0,0.0,1.0)            # Blue
    glVertex3f( 1.0,-1.0, 1.0)
    
    glColor3f(1.0,0.0,0.0)            # Red
    glVertex3f( 0.0, 1.0, 0.0)        # Top Of Triangle (Right)
    glColor3f(0.0,0.0,1.0)            # Blue
    glVertex3f( 1.0,-1.0, 1.0)        # Left Of Triangle (Right)
    glColor3f(0.0,1.0,0.0)            # Green
    glVertex3f( 1.0,-1.0, -1.0)        # Right 
    
    glColor3f(1.0,0.0,0.0)            # Red
    glVertex3f( 0.0, 1.0, 0.0)        # Top Of Triangle (Back)
    glColor3f(0.0,1.0,0.0)            # Green
    glVertex3f( 1.0,-1.0, -1.0)        # Left Of Triangle (Back)
    glColor3f(0.0,0.0,1.0)            # Blue
    glVertex3f(-1.0,-1.0, -1.0)        # Right Of 
        
        
    glColor3f(1.0,0.0,0.0)            # Red
    glVertex3f( 0.0, 1.0, 0.0)        # Top Of Triangle (Left)
    glColor3f(0.0,0.0,1.0)            # Blue
    glVertex3f(-1.0,-1.0,-1.0)        # Left Of Triangle (Left)
    glColor3f(0.0,1.0,0.0)            # Green
    glVertex3f(-1.0,-1.0, 1.0)        # Right Of Triangle (Left)
    glEnd()    
    
    globais.rtri  = globais.rtri + 0.2
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
    glClearColor(1.0,1.0,1.0,1.0)     #cor de fundo branca
    glClearDepth(1.0)        #abilita limpar o buffer de prof.
    glShadeModel(GL_FLAT)        #Configura como sera de. a ilum.
    glDepthFunc(GL_LESS)        #Funcao usada no depth-test
    glEnable(GL_DEPTH_TEST)        #Habilita o deph-test
    glMatrixMode(GL_PROJECTION)    #Projecao perspectiva
    glLoadIdentity()        #reseta a matriz de projecao
    
    #gluPerspective angulo_de_visao aspecto plano_near plano_far
    gluPerspective(46.0, float(largura/altura), 0.1, 100.0)
