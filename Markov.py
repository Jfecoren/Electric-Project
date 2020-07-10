#!/usr/bin/env python

'''
Borrador de Libreto para escenas

1. Aparecen Titulos respectivos
2. Se borran titulos y aparece un objeto circulo
3. Aparecen cada segundo la cantidad de objetos a atender
4. Cada segundo los objetos cambian de color mostrando que ya han sido atendidos
5. Los objetos atendidos salen de la cola, mostrando espacio para los demas objetos
'''
import numpy as np
from big_ol_pile_of_manim_imports import *
from threading import Thread



#Variables para el calculo de las probabilidades
N = 10                   #Numero de llegadas
tiempoTranscurso = 2 #Tiempo entre cada aparicion de objeto (llegada)

def nacimiento(self, objetoC, time=1, i=0):
        self.play(ShowCreation(objetoC), run_time = time/4)
        self.play(objetoC.next_to, LEFT*(i+1)*0.5)
        self.wait(time/2)
        
    
def muerte(self, objetoC, time=1, i=0):                     #muerte dell objeto
    if i>0:
        self.play(objetoC.set_color, BLUE)
        self.play(objetoC.shift, RIGHT*3)
    
def tiempo():                                   #Definimos un segundo de espera, tomando en cuenta un parte del tiempo en el que duran en ejecutarse las instrucciones
    self.wait()


class Markov(Scene):
    def construct(self):
        #Archivo para cadenas de Markov
        
        #Definimos las Variables Objeto a Utilizar
        title1 = TextMobject("Cadenas de Markov")
        title2 = TextMobject("Procesos de Nacimiento y Muerte")
        cantidad = TextMobject("N = "+str(N))
        cantidad.move_to(UP*2)
        #Definimos algunas figuras
        
        circles = np.full([N], None)
        for i in range(0, len(circles)):
            circles[i] = Circle(radius = 0.2, color = RED)
            circles[i].set_fill(RED, opacity = 1)
            circles[i].move_to(LEFT*5)
        
        
        
        #Animaciones del Video
        self.play(ShowCreation(title1))
        self.wait(2)
        self.play(FadeOut(title1), ShowCreation(title2))
        self.wait(2)
        self.play(FadeOutAndShiftDown(title2))
        self.wait(3)
        
        self.play(Write(cantidad))
        for n in range(0,len(circles)):
            Thread(target = nacimiento(self, circles[n], tiempoTranscurso, n)).start()
            Thread(muerte(self, circles[n-1], tiempoTranscurso, n)).start()
        self.wait(3)
        
        
        
        
        