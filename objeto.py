from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import objloader

fila_objetos = []

def adiciona_objeto(obj):
    global fila_objetos
    fila_objetos.append(obj)

def desenha_objetos():
    global fila_objetos
    for o in fila_objetos:
        o.update()
        o.draw()

class objeto(objloader.ObjLoader):

    def __init__(self, filename,
                 translation = [0.0,0.0,0.0],
                 rotation    = [0.0,0.0,0.0,0.0],
                 scale       = [0.0,0.0,0.0],
                 translateHook = None,
                 rotateHook    = None,
                 scaleHook     = None):
        
        self.filename    = filename
        self.translation = translation
        self.rotation    = rotation
        self.scale       = scale
        
        self.translateHook = translateHook
        self.rotateHook    = rotateHook
        self.scaleHook     = scaleHook
        
        super(objeto, self).__init__(filename)

    def update(self):
        if self.translateHook != None:
            self.translateHook(self.translation)

        if self.rotateHook != None:
            self.rotateHook(self.rotation)

        if self.scaleHook != None:
            self.scaleHook(self.scale)    
            
    def draw(self):
        glScalef(*self.scale)
        glTranslatef(*self.translation)
        glRotatef(*self.rotation)
        glCallList(self.gl_list)
        

