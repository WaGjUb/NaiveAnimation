import globais
import math

ESC = chr(27) #Codigo ascii do Esc

fila_teclas = set()

def atualizar_eventos():
    #print(int(globais.yrot))
    #print( math.cos(math.radians(globais.yrot)) * globais.passo)
    #print( math.sin(math.radians(globais.yrot)) * globais.passo)
    for tecla in fila_teclas:
        try:
            tecla_funcao[tecla]()
        except KeyError:
            print("Tecla {} nao faz nada".format(tecla))

def anda_frente():
    print("anda_frente")
    globais.ztrans += math.cos(math.radians(globais.yrot)) * globais.passo
    globais.xtrans -= math.sin(math.radians(globais.yrot)) * globais.passo

def anda_traz():
    print("anda_traz")
    globais.ztrans -= math.cos(math.radians(globais.yrot)) * globais.passo
    globais.xtrans += math.sin(math.radians(globais.yrot)) * globais.passo

def anda_esquerda():
    print("anda_esquerda")
    globais.ztrans -= math.cos(math.radians(globais.yrot + 90)) * globais.passo
    globais.xtrans += math.sin(math.radians(globais.yrot + 90)) * globais.passo

def anda_direita():
    print("anda_direita")
    globais.ztrans += math.cos(math.radians(globais.yrot + 90)) * globais.passo
    globais.xtrans -= math.sin(math.radians(globais.yrot + 90)) * globais.passo

def olha_esquerda():
    print("olha_esquerda")
    globais.yrot -= globais.passo_rotacao

def olha_direita():
    print("olha_direita")
    globais.yrot += globais.passo_rotacao

def sai_do_programa():
    print("sai_do_programa")
    exit(0)

#Dicionario que assimila uma tecla a uma funcao
tecla_funcao = {
    'w': anda_frente,
    's': anda_traz,
    'a': anda_esquerda,
    'd': anda_direita,
    'j': olha_esquerda,
    'l': olha_direita,
    ESC: sai_do_programa

} 

