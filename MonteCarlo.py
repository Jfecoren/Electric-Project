#!/usr/bin/env python

import numpy as np
import random
from big_ol_pile_of_manim_imports import *

#from manimlib.imports import *




class MonteCarlo(Scene):   

    def construct(self):
    
        #Definimos las variables que vamos a utilizar para la animacion
        
        
        
        #Para contar la cantidad de veces que el punto estara dentro del circulo o cuadrado
        countCircle = 0
        countSquare = 0
        
        #titulos
        title1 = TextMobject("Metodo de MonteCarlo")
        #Ecuaciones
        eq1 = TexMobject(r"\frac{A_c}{A_s}", r" = ", r"\frac{\pi r^2}{l^2}" , r" = ", r"\frac{\pi}{4}")
        eq1.move_to(LEFT*4)                             #Definimos la posicion inicial
        eq2 = TexMobject(r"4 \frac{P_c}{P_s}", " = ", r"\pi")
        eq2.move_to(LEFT*4)
        eq3 = TexMobject("r = 1", "l = 2")
        eq3[0].move_to(LEFT*3 +UP*2)                             #Definimos la posicion inicial
        eq3[1].move_to(LEFT*3 - UP*2)
        eqAc = TexMobject(r"A_c = \pi r^2")
        eqAs = TexMobject(r"A_s = l^2")
        eqAc.move_to(LEFT*3 + UP)               #Definimos su posicion incial
        eqAs.move_to(LEFT*3 - UP)               #Definimos una posicion incial
        
        #figuras
        square1 = Square(color  = RED, side_length = 4)
        circle1 = Circle(color = BLUE, radius = 2)
        cantidadPuntos = 100
        dots = np.full([cantidadPuntos], None)                 #Definimos un vector de longitud 100 para los puntos aleatorios dentro del area
        for i in range(0, len(dots)):               #Cada posicion del vector sera una figura punto (Dot)
            dots[i] = Dot(radius = 0.05)
            dots[i].move_to(np.array([random.uniform(-1.9, 1.9) + 3, random.uniform(-1.9, 1.9), 0]))                #Los puntos aleatorios estan dentro del cuadrado/circulo
        
        
        #Definimos el comportamiento de esos objetos/variables durante la animacion
        self.play(Write(title1))
        self.wait(2)
        self.play(FadeOut(title1), ShowCreation(square1))
        self.wait(2)
        self.play(ShowCreation(circle1))
        self.play(circle1.move_to, RIGHT*3, square1.move_to, RIGHT*3)
        self.wait()
        self.play(FadeIn(eqAc), FadeIn(eqAs))               #Escribimos las ecuaciones de area
        
        self.play(Transform(eqAc[:], eq1[0]), Transform(eqAs[:], eq1[0]))
        self.wait(3)
        self.play(FadeOut(eqAc), FadeOut(eqAs))
        for i in range(0,len(eq1)):                         #Escribimos cada 0.5 segundos cada lugar del vector ecuacion 1
            self.play(Write(eq1[i]))
            if i == 2:
                self.play(Write(eq3))
            self.wait(0.5)
        
        for i in range(0, len(dots)):                       #Agregamos los puntos de manera aleatoria en el espacio elegido
            self.add(dots[i])
            self.wait(0.1)
        
        self.play(FadeOut(eq1), FadeOut(eq3), Write(eq2))
        
        #Funcion para saber cuantos son los puntos dots que estan dentro del circulo
        for i in range(0, len(dots)):
            distance = np.linalg.norm(dots[i].get_center() - RIGHT*3)                   #Calculamos la magnitud del vector centro del objeto dot[i], del centro a su posicion
            if abs(distance) < 2:                                                                               #Definimos si los puntos cayeron dentro del circulo
                countCircle = countCircle + 1
                countSquare = countSquare + 1                   #La cantidad de veces que un punto cae en el cuadrado es la cantidad de puntos que hay
            else:
                countSquare = countSquare + 1
            
            
        self.wait(2)
        #Escribimos aparte estas ecuaciones que corresponden a la cantidad de veces que aparecieron los puntos en cada figura
        eqCC = TexMobject(r"P_c = ",str(countCircle))
        eqCS = TexMobject(r"P_s = ", str(countSquare))
        eqCC.move_to(LEFT*3 +UP*2)                             #Definimos la posicion inicial
        eqCS.move_to(LEFT*3 - UP*2)
        eqTotal = TexMobject(str(4*countCircle/countSquare))            #Definimos una ecuacion que proporsione el resultado entre los valores obtenidos
        eqTotal.move_to(LEFT*3)
        
        #Se puede observar el valor aproximado de pi
        self.play(Write(eqCC), Write(eqCS))
        self.wait(2)
        self.play(Transform(eq2[2], eqTotal))                                       #Transofmramos el valor de la ecuacion 2 eq2 donde se encuentra pi, en el valor aproximado encontrado en la operacion
        
        self.wait(5)
        
        #repetimos para un numero mayor de n
        ####### Se intento definir una funcion para generar estos puntos de manera automatica, pero python no reconoce esa funcino como existente
        
        
        
        self.play(FadeOut(eqCC),FadeOut(eqCS))
        for i in range(0, len(dots)):
            self.remove(dots[i])
        
        #Ahora lo haremos una cantidad de 500 puntos
        cantidadPuntos = 500
        
        cantidadN = TexMobject(r"n = "+str(cantidadPuntos))
        self.wait(5)
        self.play(Write(cantidadN))
        self.wait(2)
        dots = np.full([cantidadPuntos], None)                 #Definimos un vector de longitud 100 para los puntos aleatorios dentro del area
        for i in range(0, len(dots)):               #Cada posicion del vector sera una figura punto (Dot)
            dots[i] = Dot(radius = 0.05)
            dots[i].move_to(np.array([random.uniform(-1.9, 1.9) + 3, random.uniform(-1.9, 1.9), 0]))                #Los puntos aleatorios estan dentro del cuadrado/circulo
            
        for i in range(0, len(dots)):                       #Agregamos los puntos de manera aleatoria en el espacio elegido
            self.add(dots[i])
            self.wait(0.1)
            
        #Volvemos a incializar las variables de cuenta
        countCircle = 0
        countSquare = 0
        #Funcion para saber cuantos son los puntos dots que estan dentro del circulo
        for i in range(0, len(dots)):
            distance = np.linalg.norm(dots[i].get_center() - RIGHT*3)                   #Calculamos la magnitud del vector centro del objeto dot[i], del centro a su posicion
            if abs(distance) < 2:                                                                               #Definimos si los puntos cayeron dentro del circulo
                countCircle = countCircle + 1
                countSquare = countSquare + 1                   #La cantidad de veces que un punto cae en el cuadrado es la cantidad de puntos que hay
            else:
                countSquare = countSquare + 1
            
            
        self.wait(2)
        #Escribimos aparte estas ecuaciones que corresponden a la cantidad de veces que aparecieron los puntos en cada figura
        eqCC = TexMobject(r"P_c = ",str(countCircle))
        eqCS = TexMobject(r"P_s = ", str(countSquare))
        eqCC.move_to(LEFT*3 +UP*2)                             #Definimos la posicion inicial
        eqCS.move_to(LEFT*3 - UP*2)
        eqTotal = TexMobject(str(4*countCircle/countSquare))            #Definimos una ecuacion que proporsione el resultado entre los valores obtenidos
        eqTotal.move_to(LEFT*3)
        
        #Se puede observar el valor aproximado de pi
        self.play(Write(eqCC), Write(eqCS))
        self.wait(2)
        self.play(Transform(eq2[2], eqTotal))                                       #Transofmramos el valor de la ecuacion 2 eq2 donde se encuentra pi, en el valor aproximado encontrado en la operacion
        
        self.wait(10)