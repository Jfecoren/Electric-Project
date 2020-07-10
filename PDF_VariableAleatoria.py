#!/usr/bin/env python


from big_ol_pile_of_manim_imports import *

def Range(in_val, end_val, step = 1):
        return list(np.arange(in_val, end_val+step, step))

class PDFVar(GraphScene):
    CONFIG = {
        "y_max" : 2,
        "y_min" : 0,
        "y_axis_height" : 3,
        "x_max" : 3,
        "x_min" : -3,
        "y_tick_frequency" : 1,
        "x_tick_frequency" : 1,
        "axes_color" : BLUE,
        "graph_origin" : np.array([0,-2,0]),
        }



    def construct(self):
        #Presentacion en pantalla
        
        #Variables a Presentar
        title1 = TextMobject("{\\Large Funcion de Densidad de Probabilidad}")
        title2 = TextMobject("Area Bajo la Curva")
        eq1 = TexMobject(r"f(x)")
        eq2 = TexMobject(r"\int_{a}^{b}", r"f(x)", "dx")
        eq3 = TexMobject(r"P(a \leq x \leq b) =")
        eq4 = TexMobject(r"f(x)", r"= \frac{1}{\sigma \sqrt(2\pi)} e^{-0.5(\frac{x-\mu}{\sigma})^2}")
        eq4.move_to(UP*3)
        
        eq5 = TexMobject(r"f(x) \geq 0")
        eq6 = TexMobject(r"\int_{-\infty}^{\infty}", r"f(x)", "dx", "=", "1")
        
        
        
        #Animaciones de Presentacion
        #Titulos
        self.play(Write(title1))
        self.wait(2)
        self.play(FadeOut(title1), FadeIn(title2))
        self.wait()
        self.play(FadeOutAndShiftDown(title2))
        
        #Ecuaciones
        self.play(Write(eq1))
        self.play(eq1.move_to, UP*2)
        self.wait()
        self.play(Write(eq2[0]), Write(eq2[2]))
        self.wait(2)
        self.play(eq1.move_to, eq2[1].get_center())
        self.play(Write(eq2[1]))
        self.remove(eq1)
        self.wait()
        self.play(eq2.shift, RIGHT*0.7)
        eq3.next_to(eq2, LEFT)
        self.play(Write(eq3))
        self.wait(2)
        self.play(eq2.move_to, eq2.get_center()+UP*3+RIGHT, eq3.move_to, eq3.get_center()+UP*3+RIGHT)
        self.wait(3)
        self.play(Write(eq5))
        self.wait(2)
        self.play(Transform(eq5, eq6))
        self.wait(3)
        self.play(FadeOut(eq5))
        self.wait()
        
        
        
        
        
        #Graficas
        self.setup_axes()
        graph = self.get_graph(lambda x : np.exp(-x**2), color = GREEN)
        self.play(ShowCreation(graph), run_time = 2)
        self.wait()
        
        #Funcion de Distribucion
        
        self.play(Transform(eq2, eq4), FadeOut(eq3))
        self.wait(3)
        #Agregar area bajo la curva
        area = self.get_riemann_rectangles(graph, x_min = -2, x_max = 2, dx=0.01)
        self.play(FadeInFromDown(area))
        self.wait(2)
        
        
        
        
        self.play(FadeOutAndShiftDown(eq2))
        self.wait(2)
    
        ##Definicion de algunas configuraciones de la grafica
    def setup_axes(self):
        GraphScene.setup_axes(self)
        self.x_axis.label_direction = UP
        init_val_x = -3
        step_x = 1
        end_val_x = 3
        
        values_dec_x = Range(init_val_x, end_val_x, step_x)
        
        list_x = [*["%.1f"%i for i in values_dec_x]]
        
        
        values_x = [
            (i,j)
            for i,j in zip(values_dec_x, list_x)
        ]
        
        self.x_axis_labels = VGroup()
        for x_val, x_tex in values_x:
            tex = TexMobject(x_tex)
            tex.scale(0.5)
            tex.next_to(self.coords_to_point(x_val, 0), DOWN)
            self.x_axis_labels.add(tex)
       
        self.play(
            Write(self.x_axis_labels),
            Write(self.x_axis),
            Write(self.y_axis)
        )
        
        