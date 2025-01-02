from manim import *
from math import sin, cos

class ExampleFunctionGraph(Scene):
    def construct(self):
        # Axes creation
        axes = Axes((-10, 10), (-5, 5)).add_coordinates()
        axes.shift(LEFT).scale(1.25)
        labels = axes.get_axis_labels(Tex("x-axis").scale(1), Tex("y-axis").scale(1))

        # function to plot
        exp_func = lambda t: [t, np.exp(t), 0]
        ln_func  = lambda t: [t, np.log2(t), 0]

        exp_graph = axes.plot_parametric_curve(exp_func, color=BLUE, t_range=[-10, 10]) # Get the corresponding function graph
        ln_graph = axes.plot_parametric_curve(ln_func, color=GREEN, discontinuities=[0], dt=0.1, t_range=[0.01, 10])

        a = exp_graph.get_point_from_function(t=0)
        b = ln_graph.get_point_from_function(t=2)

        self.add(axes, labels)
        self.play(Create(exp_graph), run_time=3)
        self.play(Create(Dot(a)))
        self.wait(1)

        self.play(Transform(exp_graph,ln_graph), run_time=3)
        self.play(Transform(Dot(a),Dot(b)))

        self.play(Create(axes.get_vertical_line(b)))
        self.play(Create(axes.get_horizontal_line(b)))

        self.wait(5)


class PlotParametricFunction(Scene):
    def func(self, t):
        return (np.sin(2 * t), np.sin(3 * t), 0)

    def construct(self):
        func = ParametricFunction(self.func, t_range = (0, TAU), fill_opacity=0).set_color(RED)
        self.add(func.scale(3))


class ThreeDParametricSpring(ThreeDScene):
    def construct(self):
        curve1 = ParametricFunction(
            lambda u: (
                1.2 * np.cos(u),
                1.2 * np.sin(u),
                u * 0.05
            ), color=RED, t_range = (-3*TAU, 5*TAU, 0.01)
        ).set_shade_in_3d(True)
        axes = ThreeDAxes()
        self.add(axes, curve1)
        self.set_camera_orientation(phi=80 * DEGREES, theta=-60 * DEGREES)
        self.wait()