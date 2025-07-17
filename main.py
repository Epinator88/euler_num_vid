from manim import *

class IntroToE(Scene):

    def construct(self):
        epin = Text("ep1n", t2c={'1':YELLOW}, font_size=48)
        self.play(Write(epin))
        self.play(Unwrite(epin))
        alg = Text("y = mx + b", font_size=48)
        self.play(Write(alg))
        self.play(FadeOut(alg))
        self.remove(epin, alg)
        poly = MathTex("(a+b)^2 = a^2 + 2ab + b^2", color = BLUE, font_size=48)
        rad = MathTex("\\sqrt{a^2 + b^2}", color = RED, font_size=48)
        imag = MathTex("i = \\sqrt{-1}", color = GREEN, font_size=48)
        loga = MathTex("\\log_a{b} = \\frac{\\log{b}}{\\log{a}}", color = YELLOW, font_size=48)
        self.play(Write(poly))
        self.play(poly.animate.shift(UP * 2 + LEFT * 2), Succession(Wait(0.5),Write(rad)))
        self.play(rad.animate.shift(UP * 2 + RIGHT * 2), Succession(Wait(0.5),Write(imag)))
        self.play(imag.animate.shift(DOWN * 2 + LEFT * 2), Succession(Wait(0.5),Write(loga)))
        self.play(loga.animate.shift(DOWN * 2 + RIGHT * 2))
        self.play(FadeOut(poly, shift=LEFT * 5), FadeOut(rad, shift=UP * 5), FadeOut(imag, shift=DOWN * 5), FadeOut(loga, shift=RIGHT * 5))

        # start to do the units and then the lesson w/ e

        title = Text("Algebra Curriculum", font_size=72, ).shift(UP * 3) #this should be at the top of the screen
        self.play(Write(title))
        under = Underline(title)
        self.play(Write(under))
        boxes = VGroup()

        boxes.add(*[Square(color = BLUE).shift(RIGHT * (i % 3 - 1) * 3 + DOWN * (i // 3 - 0.5) * 3).shift(DOWN) for i in range(6)])
        self.play(Create(boxes))
        nubox = boxes[1].copy().set_color(YELLOW)
        self.play(FadeIn(nubox))
        self.play(FadeOut(boxes))
        self.play(FadeOut(title), FadeOut(under), nubox.animate.shift(DOWN * 0.5))







        self.wait(2) #so that i can actually see the end of the animation oh my god