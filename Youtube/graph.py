from manim import *
from math import sin, cos

class ParametricSinCurve(Scene):
    def construct(self):
        axes = NumberPlane()
        axes.add_coordinates()
        self.add(axes)

        sin_curve = ParametricFunction(
            function= lambda t: [
                t,
                sin(t),
                0
            ],
            t_range=[-5, 5, 0.1]
        )

        cos_curve = ParametricFunction(
            function= lambda t: [
                t,
                cos(t),
                0
            ],
            t_range=[-5, 5, 0.1]
        )

        sin_curve.set_color(YELLOW)

        p_cos_pi_4 = axes.c2p(PI/4, cos(PI/4), 0)
        p_sin_pi_6 = axes.c2p(PI/6, sin(PI/6), 0)

        self.play(Create(sin_curve))
        self.play(Create(cos_curve))

        self.add(Dot(p_cos_pi_4))
        self.add(Dot(p_sin_pi_6))
        self.wait(3)