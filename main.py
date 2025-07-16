from manim import *

class MainScene(Scene):
    def construct(self):
        taylor = MathTex(r"e^{x} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots")
        self.play(Write(taylor), run_time=3)
        self.play(taylor.animate.shift(UP * 2), run_time = 1)
        self.play(Circumscribe(taylor, color=BLUE, run_time=2))
        self.play(taylor.animate.shift(DOWN * 2), run_time = 1)
        euler = MathTex(r"e \approx 2.71828")
        self.play(ReplacementTransform(taylor, euler), run_time = 1)
        self.wait(1)