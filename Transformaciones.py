#!/usr/bin/env python

from big_ol_pile_of_manim_imports import *
import numpy as np

N = 20                  #Cantidad de Puntos
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
        "x_max": 30,
        "x_axis_width": 15,
        "x_axis_label": "$x$",
        
        "y_min": 0,
        "y_max": 6,
        "y_axis_height": 6,
        "y_axis_label": "$y$",
        
        "graph_origin": DOWN*3+ LEFT*6,
        "default_graph_colors": [YELLOW, GREEN, RED],
        "default_derivative_color": BLUE,
        "area_opacity": 1,
        "num_rects": 10,
    
    
    }
    
    #Definimos la funcion

    
    
    def get_points(self, coords):
        return [
            self.coords_to_point(px, py)
            for px,py in coords
        ]
    
    def get_dots(self,coords, radius = 0.1):
        points = self.get_points(coords)
        dots = VGroup(*[
            Dot(radius = radius).move_to([px,py,pz])
            for px,py,pz in points
            ]
        )
        return dots
    
    
    def show_function_graph_X(self):
        
        coords_y_x = np.full([N], 0.0)
        coords_x = np.full([N], 0)
        dots_x = np.full([N], None)
        for i in range(0, N):
            coords_x[i] = i
            coords_y_x[i] = np.sqrt(i)
            
        coords = [[px,py] for px,py in zip(coords_x, coords_y_x)]
        
        points = self.get_points(coords)
        graph = DiscreteGraphFromSetPoints(points, color = BLUE)
        dots = self.get_dots(coords)
        
        self.play(ShowCreation(graph), ShowCreation(dots), run_time = graphTime)
    
    def show_function_graph_Y(self):
        
        coords_y_x = np.full([N], 0.0)
        coords_x = np.full([N], 0)
        dots_x = np.full([N], None)
        for i in range(1, N):
            coords_x[i] = i
            coords_y_x[i] = 1/np.sqrt(i)
            
        coords = [[px,py] for px,py in zip(coords_x, coords_y_x)]
        
        points = self.get_points(coords)
        graph = DiscreteGraphFromSetPoints(points, color = BLUE)
        dots = self.get_dots(coords)
        
        self.play(ShowCreation(graph), ShowCreation(dots), run_time = graphTime)
    
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
        self.show_function_graph_X()
        self.wait(3)
        self.play(Transform(eq1, eq2), run_time = 1.5)
        self.show_function_graph_Y()
    
    
    