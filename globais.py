import numpy as np
#Globais

#Olhar para cima, baixo, esquerda, direita
up = np.mat([0.0,1.0,0.0])
viewDirection = np.mat([0.0,0.0,1.0])
sensibilidade = 0.05

#Indicam a tranlacao do mundo 
#(ilusao de mover a camera)
xtrans = 1.0
ytrans = 1.0
ztrans = -5.0
viewPos = np.mat([ xtrans, ytrans, ztrans ])

#tamanho do passo dado
passo = 0.2
passo_rotacao = 0.003

janela = None
rtri = 0

# referencias dos objs
# devem ser criados quando tivermos o contexto do opengl
chaleira = None
planta = None
