#Globais

#Olhar para cima, baixo, esquerda, direita
xrot = 0            # x rotacao
yrot = 0            # y rotacao

#Indicam a tranlacao do mundo 
#(ilusao de mover a camera)
xtrans = -1
ytrans = -1
ztrans = -5

#tamanho do passo dado
passo = 0.01
passo_rotacao = 0.3 #graus

janela = None
rtri = 0

# referencias dos objs
# devem ser criados quando tivermos o contexto do opengl
chaleira = None
planta = None
