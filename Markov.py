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
tiempoTranscurso = 2 #Tiempo entre cada aparicion/desaparicion de objeto (llegada/muerte)

def nacimiento(self, objetoC, time=1, i=0):
        self.play(ShowCreation(objetoC), run_time = time/4)
        self.play(objetoC.next_to, LEFT*(i+1)*0.5)
        self.wait(time/2)
        
    
def muerte(self, objetoC, time=1, i=0):                     #muerte dell objeto
    if i>0:
        self.play(objetoC.set_color, BLUE)
        self.play(objetoC.shift, RIGHT*3)

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
        
        
        
class MarkovSecuencia(Scene):
    def construct(self):
        #Archivo para cadenas de Markov
        N = 10
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
        
        
        ###Iniciamos una secuencia no aleatoria para demostrar la aleatoriedad
        self.play(Write(cantidad))
        #Cada dos segundos debe llegar un objeto y cada 3 segundos un objeto sera servido
        self.play(ShowCreation(circles[0]), run_time = 0.5)   #Llega el objeto 0
        self.play(circles[0].move_to, RIGHT*2.5, run_time = 0.5)
        self.wait()
        
        
        self.play(ShowCreation(circles[1]), run_time = 0.5)   #Pasados dos segundos llega el objeto 1
        self.play(circles[1].next_to, circles[0].get_center()+LEFT, run_time = 0.5)
        self.play(circles[0].set_color, WHITE, run_time = 0.5)     ## 3 segundos despues el objeto 0 fue servido
        self.wait(0.5)
        
        
        self.play(ShowCreation(circles[2]), run_time = 0.5)   #A los 4 segundos llega el objeto 2
        self.play(circles[2].next_to, circles[1].get_center()+LEFT, run_time = 0.5)
        self.wait()
        
        self.play(circles[1].set_color, WHITE, ShowCreation(circles[3]), run_time = 0.5)              #A los 6 segundos el objeto 1 es servido #Tambien el objeto 3 llega  
        self.play(circles[3].next_to, circles[2].get_center()+LEFT, run_time = 0.5)
        self.wait()
        
        self.play(ShowCreation(circles[4]), run_time = 0.5)   #A los 8 segundos llega el objeto 4
        self.play(circles[4].next_to, circles[3].get_center()+LEFT, run_time = 0.5)
        self.play(circles[2].set_color, WHITE, run_time = 0.5)     ## 9 segundos despues el objeto 2 fue servido
        self.wait(0.5)
        
        self.play(ShowCreation(circles[5]), run_time = 0.5)   #A los 10segundos llega el objeto 5
        self.play(circles[5].next_to, circles[4].get_center()+LEFT, run_time = 0.5)
        self.wait()
        
        self.play(ShowCreation(circles[6]), circles[3].set_color, WHITE, run_time = 0.5)   #A los 12 segundos llega el objeto 6 y el objeto 3 es servido
        self.play(circles[6].next_to, circles[5].get_center()+LEFT, run_time = 0.5)
        self.wait()
        
        self.play(ShowCreation(circles[7]), run_time = 0.5)   #A los 14 segundos llega el objeto 7
        self.play(circles[7].next_to, circles[6].get_center()+LEFT, run_time = 0.5)
        self.play(circles[4].set_color, WHITE, run_time = 0.5)     ## a los 15 segundos el objeto 4 fue servido
        self.wait(0.5)
        
        self.play(ShowCreation(circles[8]), run_time = 0.5)   #A los 16 segundos llega el objeto 8
        self.play(circles[8].next_to, circles[7].get_center()+LEFT, run_time = 0.5)
        self.wait()
        
        self.play(ShowCreation(circles[9]), circles[5].set_color, WHITE, run_time = 0.5)   #A los 18 segundos llega el objeto 9 y el objeto 5 es servido
        self.play(circles[9].next_to, circles[8].get_center()+LEFT, run_time = 0.5)
        self.wait()
        
        
        
        
        