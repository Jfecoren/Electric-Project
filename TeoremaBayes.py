#!/usr/bin/env python


'''
1. Aparecen los titulos
2. Aparecen ecuaciones que describen la funcion
3. Las ecuaciones que se requieren para encontrar la ecuacion fundmental del  teorema de bayers se despejan/cambian de color
4. Se encuentra la ecuacion

'''

from big_ol_pile_of_manim_imports import *

#from manimlib.imports import *




class Bayes(Scene):   
    def construct(self):
        myTitle = TextMobject("Teorema de Bayes")
        self.play(Write(myTitle))
        self.wait(1.5)
        self.play(FadeOut(myTitle), runtime=2)
        self.wait()
        
        equation1 = TexMobject(r"P(A \mid B)",r"=","{",r" P(A \cap B)","\\over",r"P(B)","}")
        self.play(Write(equation1))
        self.play(equation1.move_to, np.array([-4,0,0]))
        self.wait()
        
        equation2 =  TexMobject(r"P(B \mid A)",r"=","{",r" P(A \cap B)","\\over",r"P(A)","}")
        equation2.move_to(np.array([4,0,0]))
        self.play(Write(equation2))
        self.wait()
        self.play(equation1[3].set_color, RED_E, equation2[3].set_color, RED_E)
        
        
        self.wait()
        
        equation3 = TexMobject(r"P(A \mid B)P(B) = P(B \mid A)P(A)")
        eq31 = TexMobject("P(B)", "=","\\frac{P(B \\mid A)P(A)}{P(A \\mid B)}")
        eq31.move_to(np.array([0,2,0]))
        
        self.play(equation1.move_to, np.array([0,0,0]), equation2.move_to, np.array([0,0,0]))
        temp1 = Transform(equation1, equation3)
        temp2 = Transform(equation2, equation3)
        self.play(temp1, temp2)
        
        self.wait()
        self.remove(equation2)
        self.play(equation1.move_to, np.array([0,2,0]))
        self.play(Transform(equation1, eq31))
        
        equation4 = TexMobject("P(B)", "=","P(B \\mid A)P(A)+P(B \\mid A' )P(A')")
        self.play(Write(equation4))
        self.wait()
        self.play(eq31[0].set_color, RED_E, equation4[0].set_color, RED_E)
        
        
        
        self.play(eq31[2].set_color, RED_E)
        eq32 = TexMobject("\\frac{P(B \\mid A)P(A)}{P(A \\mid B)}")
        eq32.next_to(equation4[0].get_center()+np.array([-3,0,0]))
        self.play(Transform(equation4[0], eq32[:]))
        self.wait(2)
        
        bayes = TexMobject("P(A \\mid B) = \\frac{P(B \\mid A)P(A)}{P(B \\mid A)P(A)+P(B \\mid A' )P(A')}")
        self.play(Transform(equation4, bayes), FadeOut(eq31), FadeOut(equation1))
        self.wait(10)
        self.play(FadeOutAndShiftDown(equation4), runtime = 5)
        self.wait(3)