#!/usr/bin/env python

'''
Borrador de Libreto para escenas

1. Aparecen Titulos respectivos
2. Se borran titulos y aparece un objeto circulo
3. Se toma la distribucion de  nacimiento/muerte y aparecen y se sirven los objetos respectivos
'''
import numpy as np
from big_ol_pile_of_manim_imports import *
from threading import Thread
from scipy import stats


#Variables para el calculo de las probabilidades
N = 15                   #Numero de llegadas
tiempoEspera = 0.1          #Tiempo de espera aproximado del recorrido del vector de tiempo t, para saber si en t hay un -1, un 0, o un 1

# Parámetro de llegada (clientes/segundos)
lam = 2/60

# Parámetro de servicio (servicios/segundos)
nu = 3/60

class Markov(Scene):
    def construct(self):
        #Archivo para cadenas de Markov
        
        #Definimos las Variables Objeto a Utilizar
        title1 = TextMobject("Cadenas de Markov")
        title2 = TextMobject("Procesos de Nacimiento y Muerte")
        cantidad = TextMobject("N = "+str(N))
        cantidad.move_to(UP*2)
        #Definimos algunas figuras
        
        serviceSquare = Square(side_length = 0.8)
        serviceSquare.move_to(RIGHT*3)
        circles = np.full([N], None)
        for i in range(0, len(circles)):
            circles[i] = Circle(radius = 0.2, color = RED)
            circles[i].set_fill(RED, opacity = 1)
            circles[i].move_to(LEFT*5)
        
        # Distribución de los tiempos de llegada entre cada cliente
        X = stats.expon(scale = 1/lam)
        # Distribución de los tiempos de servicio a cada cliente
        Y = stats.expon(scale = 1/nu)

        # Intervalos entre llegadas (segundos desde último cliente)
        t_inte = np.ceil(X.rvs(N)).astype('int')
        # Tiempos de las llegadas (segundos desde el inicio)
        t_lleg = [t_inte[0]]
        for i in range(1, len(t_inte)):
            siguiente = t_lleg[i-1] + t_inte[i]
            t_lleg.append(siguiente)
        # Tiempos de servicio (segundos desde inicio de servicio)
        t_serv = np.ceil(Y.rvs(N)).astype('int')

        # Inicialización del tiempo de inicio y fin de atención
        inicio = t_lleg[0]          # primera llegada
        fin = inicio + t_serv[0]    # primera salida

        # Tiempos en que recibe atención cada i-ésimo cliente (!= que llega)
        t_aten = [inicio]
        for i in range(1, N):
            inicio = np.max((t_lleg[i], fin))
            fin = inicio + t_serv[i]
            t_aten.append(inicio)

        # Inicialización del vector temporal para registrar eventos
        t = np.zeros(t_aten[-1] + t_serv[-1] + 1)

        # Asignación de eventos de llegada (+1) y salida (-1) de clientes
        for c in range(N):
            i = t_lleg[c]
            t[i] += 1
            j = t_aten[c] + t_serv[c]
            t[j] -= 1
            
            
        self.play(ShowCreation(title1))                     #Se crean los titulos
        self.wait(2)
        self.play(FadeOut(title1), FadeIn(title2))
        self.wait(2)
        self.play(FadeOut(title2))
        self.play(Write(cantidad))
        self.play(FadeIn(serviceSquare))
        
        
        #Definimos el primer objeto que ya ha aparecido
        obL = 0
        obS = 0
        
        for recorrido in range(len(t)):                                 #For que va a recorrer el vector t para reconocer si hay 1 o -1
        
            if t[recorrido] == 1:                                               #Si hay 1, agregara un objeto
                if obL == 0:                                                        #Agrega el objeto inicial para evitar colisiones en el codigo entre los objetos
                    self.play(ShowCreation(circles[0]), run_time = 0.5)
                    self.play(circles[0].move_to, serviceSquare.get_center())
                elif circles[obS] in self.mobjects:                         #Si el objeto que se esta sriviendo anteriormente, sigue en pantalla, el objeto de llegada se coloca en la fila
                    self.play(ShowCreation(circles[obL]), run_time = 0.5)
                    self.play(circles[obL].next_to, circles[obL - 1].get_center()+LEFT*2)
                        
                else:                                                                   #Si ya no hay un objeto en pantalla, va directamente a la estacion de servicio
                    self.play(ShowCreation(circles[obL]), run_time = 0.5)
                    self.play(circles[obL].move_to, serviceSquare.get_center())
                    
                obL += 1
        
        
            if t[recorrido] == -1:                                          #Si hay un -1 en el vector, el objeto actualmente sirviendose, se retira
                #self.play(circles[obS].shift, RIGHT)
                self.play(FadeOut(circles[obS]))
                self.remove(circles[obS])
                
                for corrimiento in range(N, 0, -1):             #Movemos los objetos que estaban en cola, una posicion siguiente, cuando un objeto ya termino de ser servido
                    if obS < N - corrimiento:
                        if  circles[obS + corrimiento] in self.mobjects:
                            self.play(circles[obS+corrimiento].move_to, circles[obS+corrimiento-1].get_center())
                                        
                obS += 1
            self.wait(tiempoEspera)                                 #Tiempo de espera aproximado entre cada recorrido del vector t.
        
        
        
        
    