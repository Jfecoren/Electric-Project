#!/usr/bin/env python

'''
Borrador de Libreto para escenas

1. Aparecen Titulos respectivos
2. Se borran titulos y aparece un objeto circulo
3. 
'''

from big_ol_pile_of_manim_imports import *
from threading import Thread



def nacimiento():
    pass
    
def muerte():
    pass
    
def tiempo():                                   #Definimos un segundo de espera, tomando en cuenta un parte del tiempo en el que duran en ejecutarse las instrucciones
    self.wait()


class Markov(Scene):
    def construct(self):
        #Archivo para cadenas de Markov
        
        #Variables para el calculo de las probabilidades
        N = 10                      #Numero de Clientes
        lam = 6/60                  #Clientes que llegan por segundo
        nu = 10/60                   #Clientes que son servidos cada segundo
        t = 0.0                               #Tiempo que debe transcurrir
        
        #Definimos las Variables Objeto a Utilizar
        title1 = TextMobject("Cadenas de Markov")
        title2 = TextMobject("Procesos de Nacimiento y Muerte")
        
        #Definimos algunas figuras
        circles = np.full([N], None)
        for i in range(0, len(circles)):
            circles[i] = Circle(radius = 0.5, color = BLUE)
            circles[i].set_fill(BLUE, opacity = 1)
        
        
        
        
        
        
        
        
        
        #Animaciones del Video
        self.play(ShowCreation(title1))
        self.wait(2)
        self.play(FadeOut(title1), ShowCreation(title2))
        self.wait(2)
        self.play(ShowCreation(circles[0]))
        self.wait(3)