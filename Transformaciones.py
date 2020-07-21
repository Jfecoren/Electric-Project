#!/usr/bin/env python

from big_ol_pile_of_manim_imports import *
import numpy as np
import math

N = 10                  #Cantidad de Puntos
graphTime = 10  #Tiempo en que dura creando la grafica

class SmoothGraphFromSetPoints(VMobject):
    def __init__(self, set_of_points, **kwargs):
        super().__init__(**kwargs)
        self.set_points_smoothly(set_of_points)

class DiscreteGraphFromSetPoints(VMobject):
    def __init__(self, set_of_points, **kwargs):
        super().__init__(**kwargs)
        self.set_points_as_corners(set_of_points)
    
class vTransform(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 10,
        "x_axis_width": 10,
        "x_axis_label": "$f_x(X)$",
        
        "y_min": 0,
        "y_max": 5,
        "y_axis_height": 5,
        "y_axis_label": "$f_y(X)$",
        
        "graph_origin": DOWN*3+ LEFT*5,
        "default_graph_colors": [YELLOW, GREEN, RED],
        "default_derivative_color": BLUE,
        "area_opacity": 1,
        "num_rects": 10,
    
    
    }
    
    #Definimos la funcion

    
    #Convierte las coordenadas de la pantalla, a coordenadas en la grafica
    def get_points_from_coords(self, coords):
        return [
            self.coords_to_point(px, py)
            for px,py in coords
        ]
    
    def get_dots(self,coords, radius = 0.1):
        points = self.get_points_from_coords(coords)
        dots = VGroup(*[
            Dot(radius = radius).move_to([px,py,pz])
            for px,py,pz in points
            ]
        )
        return dots
    
    
    def show_function_graph_X(self):
        
        coords_y_x = np.full([N], 0.0)
        coords_x = np.full([N], 0)
        for i in range(0, N):
            coords_x[i] = i
            coords_y_x[i] = math.exp(-0.25*(i-5)**2)
            
        coords = [[px,py] for px,py in zip(coords_x, coords_y_x)]
        
        points = self.get_points_from_coords(coords)
        graph = SmoothGraphFromSetPoints(points, color = BLUE)
        dots = self.get_dots(coords)
        self.play(ShowCreation(dots), run_time = graphTime)
        
    
    def function_graph_X1(self):
        ancho = 0.01
        graph_X1 = self.get_graph(lambda x: np.sqrt(x), x_min = 0, x_max = 10)
        self.play(ShowCreation(graph_X1), run_time = 10)
        rectan = np.full([10],None)
        for i in range(0, 10):
            rectan[i] = self.get_riemann_rectangles(graph_X1, x_min = i-ancho/2.0, x_max = i+ancho/2.0, dx = ancho)
            rectan[i].set_color(RED)
            self.play(ShowCreation(rectan[i]), run_time = 2)
        
        lines = np.full([10], None)        
        for i in range(0, 10):
            lines[i] = Line(start = np.array([-5,-2+(np.sqrt(i)-1),0]), end = np.array([math.exp(-0.25*(i-5)**2) - 5.0,-2+(np.sqrt(i)-1),0]))
            self.play(Write(lines[i]), run_time = 0.5)
        self.wait(2)
        
    def function_graph_X2(self):
        graph_X2 = self.get_graph(lambda x: 0.1*x**2, x_min = 0, x_max = 10)
        self.play(ShowCreation(graph_X2), run_time = 10)
    
    
    def discrete_rectangles(self):
        ancho = 0.04
        def func(x):
            return math.exp(-0.25*(x-5)**2)
        graph_01 = self.get_graph(func, x_min = 0, x_max = 9)
        rectan = np.full([10],None)
        for i in range(1, 10):
            rectan[i] = self.get_riemann_rectangles(graph_01, x_min = i-ancho/2.0, x_max = i+ancho/2.0, dx = ancho)
            rectan[i].set_color(WHITE)
            self.play(ShowCreation(rectan[i]), run_time = 2)
        
    
    def construct(self):
    
    
        #Definimos slos titulos que deseamos poner
        title1 = TextMobject("Transformacion de una variable aleatoria")
        
        #Definimos las ecuaciones que deseamos agregar
        eq1 = TexMobject(r"X")
        eq2 = TexMobject(r"Y = g(X)")
        eq1.move_to(UP*2)
        eq2.move_to(UP*2)
        
        
        #Definimos las figuras que deseamos agregar
        
        
        

        
        #Definimos el progreso de las animaciones
        #Mostramos una grafica antes para aumentar el drama
        self.setup_axes(animate = True)
        #Aparicion de Titulo
        self.play(Write(title1))
        self.wait(2)
        self.play(FadeOut(title1))
    
        self.play(Write(eq1), run_time = 1.5)
        self.discrete_rectangles()
        self.wait(2)
        self.play(Transform(eq1, eq2), run_time = 1.5)
        self.wait(3)
        self.function_graph_X1()
        #self.function_graph_X2()
    
        
    
        self.wait(5)
    