from manim import *

class IntroToE(Scene):

    def construct(self):
        epin = Text("ep1n", t2c={'1':YELLOW}, font_size=48)
        self.play(Write(epin))
        self.wait(2)
        self.play(Unwrite(epin))
        self.wait(3)
        alg = Text("y = mx + b", font_size=48)
        self.play(Write(alg))
        self.wait(2)
        self.play(FadeOut(alg))
        self.remove(epin, alg)
        poly = MathTex("(a+b)^2 = a^2 + 2ab + b^2", color = BLUE, font_size=48)
        rad = MathTex("\\sqrt{x^3} = x^\\frac{3}{2}", color = RED, font_size=48)
        imag = MathTex("i = \\sqrt{-1}", color = GREEN, font_size=48)
        loga = MathTex("\\log_a{b} = \\frac{\\log{b}}{\\log{a}}", color = YELLOW, font_size=48)
        self.play(Write(poly))
        self.play(poly.animate.shift(UP * 2 + LEFT * 2), Succession(Wait(0.5),Write(rad)))
        self.play(rad.animate.shift(UP * 2 + RIGHT * 2), Succession(Wait(0.5),Write(imag)))
        self.play(imag.animate.shift(DOWN * 2 + LEFT * 2), Succession(Wait(0.5),Write(loga)))
        self.play(loga.animate.shift(DOWN * 2 + RIGHT * 2))
        self.wait(2)
        self.play(FadeOut(poly, shift=LEFT * 5), FadeOut(rad, shift=UP * 5), FadeOut(imag, shift=DOWN * 5), FadeOut(loga, shift=RIGHT * 5))

        # start to do the units and then the lesson w/ e

        title = Text("Algebra Curriculum", font_size=72, ).shift(UP * 3) #this should be at the top of the screen
        under = Underline(title)
        boxes = VGroup()

        boxes.add(*[Square(color = BLUE).shift(RIGHT * (i % 3 - 1) * 3 + DOWN * (i // 3 - 0.5) * 3).shift(DOWN).rotate(i * PI / 2) for i in range(6)])
        self.play(Create(boxes), Write(title), Write(under), run_time = 2)
        nubox = boxes[1].copy().set_color(YELLOW)
        unit = VGroup()
        unit.add(nubox)
        unitName = Text("Exponential Functions", font_size=48, color=YELLOW).next_to(nubox, UP * 0.1)
        unit.add(unitName)
        self.play(FadeIn(nubox), FadeOut(boxes), FadeOut(title), FadeOut(under), nubox.animate.shift(DOWN * 0.5), boxes[1].animate.shift(DOWN * 0.5))
        lesson = Rectangle(height = .5, width = 1.6875, color = RED)
        lessonUp = lesson.copy().next_to(lesson, UP * 0.5)
        lessonDown = lesson.copy().next_to(lesson, DOWN * 0.5)
        unit.add(lesson)
        unit.add(lessonUp)
        unit.add(lessonDown)
        self.play(FadeIn(lesson), FadeIn(unitName), FadeIn(lessonUp), FadeIn(lessonDown), unit.animate.scale(1.5))
        self.add(lesson)
        unit.remove(lesson)
        self.wait(1)
        self.play(FadeOut(unit), lesson.animate.center())
        self.play(lesson.animate.stretch_to_fit_width(7))
        comp = Text("Compounding Interest", font_size=48, color=RED)
        self.play(Write(comp))
        self.wait(3)
        self.play(FadeOut(comp), FadeOut(lesson))
        self.clear()
        cash = Text("$$$", font_size=144, color=GREEN)
        self.play(Write(cash))
        self.wait(2)
        self.play(Unwrite(cash))
        yearly_pre = MathTex(r"A", r" = ", r"P", r"(1 + ", r"r", r")^", r"t", color=BLUE, font_size=48)
        monthly = MathTex(r"A = P(1 + ", "\\frac{r}{12}", r")^", r"{12t}", color=RED, font_size=48)
        continuous = MathTex(r"A = ", r"P", r"e", r"^", r"{rt}", color=GREEN, font_size=48)
        yearly_pre.next_to(monthly, UP)
        continuous.next_to(monthly, DOWN)
        self.play(Write(yearly_pre), Succession(Wait(0.5), Write(monthly)), Succession(Wait(1), Write(continuous)))
        self.wait(2)
        self.play(FadeOut(monthly, shift = DOWN * 3), FadeOut(continuous, shift = DOWN * 3), yearly_pre.animate.center())
        self.wait(2)
        yearly_simple = Text("Money = 1000(1.12)(1.12)(1.12)(1.12)(1.12)", color=BLUE, font_size=48)
        self.play(ReplacementTransform(yearly_pre, yearly_simple))
        self.wait(4)
        yearly = MathTex(r"A", r" = ", r"P", r"(1 + ", r"r", r")^", r"t", color=BLUE, font_size=48)
        self.play(ReplacementTransform(yearly_simple, yearly))
        self.play(yearly[2].animate.set_color(YELLOW))
        self.wait(0.5)
        self.play(yearly[4].animate.set_color(YELLOW))
        self.wait(0.5)
        self.play(yearly[6].animate.set_color(YELLOW))
        self.wait(1)
        monthly.center()
        self.wait(2)
        self.play(ReplacementTransform(yearly, monthly))
        self.play(monthly[3].animate.set_color(YELLOW))
        self.wait(0.5)
        self.play(monthly[1].animate.set_color(YELLOW))
        self.wait(1)
        compl = MathTex(r"1.12 < ", r"(1.01)^{12}", font_size = 48, color = RED)
        fin = MathTex(r"1.1268", font_size = 48, color = RED)
        self.wait(2)
        self.play(FadeOut(monthly, scale = 10), FadeIn(compl, scale = 0.1))
        self.wait(2)
        fin.move_to(compl[1])
        self.play(Transform(compl[1], fin))
        self.wait(0.5)
        self.play(FadeOut(compl, scale = 0.1), FadeIn(monthly, scale = 10))
        continuous.center()
        self.wait(2)
        self.play(ReplacementTransform(monthly, continuous))
        self.wait(2)
        tex1 = Text("Hourly?", font_size=48, color=YELLOW).shift(UP)
        tex2 = Text("Secondly?", font_size=48, color=YELLOW).next_to(tex1, DOWN * 1)
        tex3 = Text("Continuously?", font_size=48, color=YELLOW).next_to(tex2, DOWN * 1)
        self.play(FadeOut(continuous), FadeIn(tex1), FadeIn(tex2), FadeIn(tex3))
        self.play(FadeOut(tex1, scale = 0))
        self.play(FadeOut(tex2, scale = 0))
        self.play(tex3.animate.center())
        self.play(Circumscribe(tex3))
        self.wait(2)
        self.play(ReplacementTransform(tex3, continuous))
        self.play(continuous[1].animate.set_color(YELLOW))
        self.wait(0.5)
        self.play(continuous[2].animate.set_color(YELLOW))
        self.wait(0.5)
        self.play(continuous[4].animate.set_color(YELLOW))
        big_euler = MathTex("e", " = ", "2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945729725726", color=YELLOW, font_size=144)
        big_euler.next_to(continuous, RIGHT)
        big_euler.shift(LEFT * 2.2) #NIIIIIIIIIIIICHE GEOMETRY DASH REFERENCE
        self.play(FadeOut(continuous, scale = 0.1))
        self.play(Write(big_euler), run_time = 4)
        self.wait(5)
        self.play(big_euler.animate.shift(LEFT * 100), run_time = 6)


        # end first paragraph, segue into origin of e


        self.wait(2) #so that i can actually see the end of the animation oh my god

class EulerFoundations(Scene):

    def construct(self):
        euler = Text("e", font_size=720, color=WHITE)
        self.play(Write(euler))








        self.wait(2) #so that i can actually see the end of the animation oh my god 2: electric boogaloo