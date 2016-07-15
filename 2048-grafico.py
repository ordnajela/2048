# -*- encoding: utf-8 -*-
import sys
import random
import pygame

puntaje = 0

def izquierda(matriz):
    global puntaje
    x = len(matriz[0])
    y = len(matriz)
    i = 0
    j = 0
    k = 0
    for j in range (y):
        i = 0
        for i in range (x):
            #print("vuelta: " + str(i))
            if matriz[j][i] != 0:
                k = i+1
                for k in range (k,x):
                    if matriz[j][k] == matriz [j][i]:
                        #print (str(j)+" "+str(k)+" = "+str(j)+" "+str(i))
                        matriz[j][i] = matriz[j][i] * 2
                        puntaje += matriz[j][i]
                        matriz[j][k] = 0
                        break
                    else:
                        if matriz[j][k] != 0:
                            break
        #print("-------------------------")
    j = 0
    for j in range (y):
        i = 0
        while i < x:
            #print("vuelta: " + str(i))
            if matriz[j][i] == 0:
                if i+1 < x:
                    if matriz[j][i+1] != 0:
                        #print("cambio")
                        matriz[j][i] = matriz[j][i+1]
                        matriz[j][i+1] = 0
                        i = 0
                    else:
                        i+=1
                else:
                    break
            else:
                i+=1
        #print("-------------------------")
    return matriz

def derecha(matriz):
    global puntaje
    x = 0
    y = len(matriz)
    i = len(matriz[0]) - 1
    j = 0
    k = 0
    for j in range(y):
        i = len(matriz[0]) - 1
        while i >= x:
            #print("vuelta: " + str(i))
            if matriz[j][i] != 0:
                k = i-1
                while k >= x:
                    if matriz[j][k] == matriz [j][i]:
                        #print (str(j)+" "+str(k)+" = "+str(j)+" "+str(i))
                        matriz[j][i] = matriz[j][i] * 2
                        puntaje += matriz[j][i]
                        matriz[j][k] = 0
                        break
                    else:
                        if matriz[j][k] != 0:
                            break
                    k-=1
            i-=1
        #print("-------------------------")

    x = 0
    y = len(matriz)
    i = len(matriz[0]) - 1
    j = 0
    for j in range(y):
        i = len(matriz[0]) - 1
        while i >= x:
            #print("vuelta: " + str(i))
            if matriz[j][i] == 0:
                if i-1 >= x:
                    if matriz[j][i-1] != 0:
                        #print("cambio")
                        matriz[j][i] = matriz[j][i-1]
                        matriz[j][i-1] = 0
                        i = len(matriz[0]) - 1
                    else:
                        i-=1
                else:
                    break
            else:
                i-=1
        #print("-------------------------")
    return matriz

def arriba(matriz):
    global puntaje
    x = len(matriz[0])
    y = len(matriz)
    i = 0
    j = 0
    k = 0
    for j in range (x):
        i = 0
        for i in range (y):
            #print("vuelta: " + str(i))
            if matriz[i][j] != 0:
                k = i+1
                for k in range (k,y):
                    if matriz[k][j] == matriz [i][j]:
                        matriz[i][j] = matriz[i][j] * 2
                        puntaje += matriz[i][j]
                        matriz[k][j] = 0
                        break
                    else:
                        if matriz[k][j] != 0:
                            break
        #print("-------------------------")
    j = 0
    for j in range (x):
        i = 0
        while i < y:
            #print("vuelta: " + str(i))
            if matriz[i][j] == 0:
                if i+1 < y:
                    if matriz[i+1][j] != 0:
                        #print("cambio")
                        matriz[i][j] = matriz[i+1][j]
                        matriz[i+1][j] = 0
                        i = 0
                    else:
                        i+=1
                else:
                    break
            else:
                i+=1
        #print("-------------------------")
    return matriz

def abajo(matriz):
    global puntaje
    x = len(matriz[0])
    y = 0
    i = len(matriz) - 1
    j = 0
    k = 0
    for j in range(x):
        i = len(matriz) - 1
        while i >= y:
            #print("vuelta: " + str(i))
            if matriz[i][j] != 0:
                k = i-1
                while k >= y:
                    if matriz[k][j] == matriz [i][j]:
                        matriz[i][j] = matriz[i][j] * 2
                        puntaje += matriz[i][j]
                        matriz[k][j] = 0
                        break
                    else:
                        if matriz[k][j] != 0:
                            break
                    k-=1
            i-=1
        #print("-------------------------")

    x = len(matriz)
    y = 0
    i = len(matriz[0])
    j = 0
    for j in range(x):
        i = len(matriz[0]) - 1
        while i >= y:
            #print("vuelta: " + str(i))
            if matriz[i][j] == 0:
                if i-1 >= y:
                    if matriz[i-1][j] != 0:
                        #print("cambio")
                        matriz[i][j] = matriz[i-1][j]
                        matriz[i-1][j] = 0
                        i = len(matriz[0]) - 1
                    else:
                        i-=1
                else:
                    break
            else:
                i-=1
        #print("-------------------------")
    return matriz

def agregarnum(matriz):
    x = random.randint(0,3)
    y = random.randint(0,3)
    while matriz[x][y] != 0 :
        if matriz[x][y] == 0:
            num = random.choice([2,4])
            matriz[x][y] = num
            return matriz
        x = random.randint(0,3)
        y = random.randint(0,3)
    num = random.choice([2,4])
    matriz[x][y] = num
    return matriz

def mostrar(matriz):
    for j in range (len(matriz)):
        cadena = ""
        for i in range (len(matriz[0])):
            cadena += str(matriz[j][i]) + ' '
        print cadena
    print "------------------------"

def suma(matriz, direccion):
    matriz_original = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    matriz_original[0] = list(matriz[0])
    matriz_original[1] = list(matriz[1])
    matriz_original[2] = list(matriz[2])
    matriz_original[3] = list(matriz[3])

    if direccion == 'd':
        matriz = derecha(matriz)
    if direccion == 'a':
        matriz = izquierda(matriz)
    if direccion == 's':
        matriz = abajo(matriz)
    if direccion == 'w':
        matriz = arriba(matriz)


    if matriz_original != matriz:
        matriz = agregarnum(matriz)
        return matriz

    return matriz_original

def perdiste(matriz):
    for j in range (len(matriz)):
        for i in range (len(matriz[0])):
            if matriz[j][i] == 0:
                return False
    for j in range (len(matriz)):
        for i in range (len(matriz[0])):
            if i+1 < len(matriz[0]):
                if matriz[j][i] == matriz[j][i+1]:
                    return False
    for j in range (len(matriz[0])):
        for i in range (len(matriz)):
            if i+1 < len(matriz):
                if matriz[i][j] == matriz[i+1][j]:
                    return False
    return True
#Funcionando, nota. mejorar la función "agregarnum" leyendo los 0 en la matriz y generando una lista que indique las posiciones libres, estas serán seleccionadas aleatoriamente

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 180, 0)
RED = (255, 0, 0)
YELLOW = (153,153,0)
DARK_YELLOW = (210,210,0)
GRAY = (50,50,50)
ORANGE = (240,120,0)
DARK_ORANGE = (232,54,2)
PINK = (255,0,255)
PURPLE = (115,67,131)
BLUE = (0,0,180)
DARK_RED = (255,150,120)

def mostrar_graf(matriz, screen, x, y):
    global puntaje
    screen.fill(WHITE)
    alto = len(matriz)
    ancho = len(matriz[0])
    ub_x = 0
    ub_y = 0

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(WHITE)
    font = pygame.font.Font(None, 30)

    ajuste = 0

    pygame.draw.rect(screen, BLACK, [x, y, 400, 400], 2)
    for i in range(alto):
        ub_x = 0
        for j in range(ancho):
            if(matriz[i][j] != 0):
                ajuste = len(str(matriz[i][j]))*10
                text = font.render(str(matriz[i][j]), 1, BLACK)
                caso = matriz[i][j] % 2049
                if caso == 2:
                    COLOR = GRAY
                if caso == 4:
                    COLOR = GREEN
                if caso == 8:
                    COLOR = ORANGE
                if caso == 16:
                    COLOR = DARK_ORANGE
                if caso == 32:
                    COLOR = PINK
                if caso == 64:
                    COLOR = RED
                if caso == 128:
                    COLOR = YELLOW
                if caso == 256:
                    COLOR = DARK_YELLOW
                if caso == 512:
                    COLOR = PURPLE
                if caso == 1024:
                    COLOR = BLUE
                if caso == 2048:
                    COLOR = DARK_RED
                pygame.draw.rect(background, COLOR, [x+ub_x, y+ub_y, 100, 100], 0)
                background.blit(text, [x+ub_x+60-ajuste, y+ub_y+50])
                #screen.blit(background, (0, 0))
            ub_x += 100
        ub_y += 100
    puntos = font.render("PUNTOS: "+str(puntaje), 1, RED)
    background.blit(puntos, [150,20])
    screen.blit(background, (0, 0))
    #Agregar texto dentro del regtángulo y meter eso a un ciclo que imprima cada cuadro de la matriz

def main():
    global puntaje
    pygame.init()
    size = [450, 500]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("2048")
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(0)



    Matriz=[[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]

    Matriz=agregarnum(Matriz)
    Matriz=agregarnum(Matriz)
    screen.fill(WHITE)
    #    font = pygame.font.Font(None, 30)
    #    mensaje = font.render("Bienvenido, presione las flechas para comenzar", 1, BLACK)
    #    screen.blit(mensaje, [20,20])
    mostrar_graf(Matriz, screen, 15, 50)
    while not perdiste(Matriz):
        # if pygame.time.get_ticks()%1000 == 0:
        #     pygame.mixer.init()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                #Dibujar
    #                    if pygame.time.get_ticks()%1000 < 600:
    #                        puntaje -= 100
                    Matriz = suma(Matriz, 'a')
                    mostrar_graf(Matriz, screen, 15, 50)
                    mostrar(Matriz)
                elif event.key == pygame.K_RIGHT:
                    #Dibujar
                   # if pygame.time.get_ticks()%1000 < 600:
                   #     puntaje -= 100
                    Matriz = suma(Matriz, 'd')
                    mostrar_graf(Matriz, screen, 15, 50)
                    mostrar(Matriz)
                elif event.key == pygame.K_UP:
                    #Dibujar
    #                    if pygame.time.get_ticks()%1000 < 600:
    #                        puntaje -= 100
                    Matriz = suma(Matriz, 'w')
                    mostrar_graf(Matriz, screen, 15, 50)
                    mostrar(Matriz)
                elif event.key == pygame.K_DOWN:
                    #Dibujar
    #                    if pygame.time.get_ticks()%1000 < 600:
    #                        puntaje -= 100
                    Matriz = suma(Matriz, 's')
                    mostrar_graf(Matriz, screen, 15, 50)
                    mostrar(Matriz)
            pygame.display.flip()
            clock.tick(60)

    #
    #    Matriz = agregarnum(Matriz)
    #
    #    d = 0
    #    while not perdiste(Matriz):
    #        print("\n\n\n\n\n")
    #        print("Puntos:"+str(puntaje))
    #        mostrar(Matriz)
    #        d = input()
    #        Matriz = suma(Matriz,str(d))
    #    mostrar(Matriz)
    #    print("Perdiste :C")
    #    return 0


if __name__ == "__main__":
    sys.exit(main())
