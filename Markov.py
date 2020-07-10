#!/usr/bin/env python

'''
Borrador de Libreto para escenas

1. Aparecen Titulos respectivos
2. Se borran titulos y aparece un objeto circulo
3. 
'''
import numpy as np
from big_ol_pile_of_manim_imports import *
from threading import Thread



#Variables para el calculo de las probabilidades
N = 5                   #Numero de Clientes


def nacimiento(circles, self):
    t1 = 10
    i = 0
    for a in range(0, N*t1,1):
        if t1 == 10:
            self.play(ShowCreation(circles[i]), runtime = 0.5)
            self.play(circles[i].next_to, LEFT*(i+1))
            i = i + 1
            t1 = 0
        t1 = t1 + 1
        self.wait(0.8)
        
    
def muerte(circles, self):
    t2 = 0                               #Tiempo que debe transcurrir
    pass
    
def tiempo():                                   #Definimos un segundo de espera, tomando en cuenta un parte del tiempo en el que duran en ejecutarse las instrucciones
    self.wait()


class Markov(Scene):
    def construct(self):
        #Archivo para cadenas de Markov
        
        #Definimos las Variables Objeto a Utilizar
        title1 = TextMobject("Cadenas de Markov")
        title2 = TextMobject("Procesos de Nacimiento y Muerte")
        
        #Definimos algunas figuras
        
        circles = np.full([N], None)
        for i in range(0, len(circles)):
            circles[i] = Circle(radius = 0.3, color = BLUE)
            circles[i].set_fill(BLUE, opacity = 1)
            circles[i].move_to(LEFT*5)
        
        
        
        
        
        #Animaciones del Video
        self.play(ShowCreation(title1))
        self.wait(2)
        self.play(FadeOut(title1), ShowCreation(title2))
        self.wait(2)
        self.play(FadeOutAndShiftDown(title2))
        self.wait(3)
        
        nacimiento(circles, self)
        self.wait(3)
        
        
        
        
        