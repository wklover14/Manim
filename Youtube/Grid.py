from manim import *

# Source of the code, this youtube video : https://www.youtube.com/watch?v=jFqYq9quBds&list=PLWOlLjdyZm2NQD1YZmEPB0dwbd0yKINAT&index=2

class FittingObjects(Scene):
    def construct(self):
        # Afficher le plan
        c = NumberPlane().add_coordinates()
        self.add(c)

        # afficher des axes secondaires
        axes = Axes(x_range=[-3, 3, 1], y_range=[-3, 3, 1], x_length=6, y_length=6)
        axes.to_edge(LEFT, buff=0.5)

        # Création d'un cercle
        circle = Circle(stroke_width = 6, stroke_color = YELLOW, fill_color = RED_C, fill_opacity = 0.8)
        circle.set_width(2).to_edge(DR, buff=0)

        # Création d'un triangle
        triangle = Triangle(stroke_color=ORANGE, stroke_width=10, fill_color= GREY).set_height(2).shift(DOWN*3 + RIGHT*3)

        # Changement du cercle en triangle
        self.play(Write(axes))
        self.play(DrawBorderThenFill(circle))
        self.play(circle.animate.set_stroke(1))
        self.play(Transform(circle, triangle), run_time=3)


class Updaters(Scene):
    def construct(self):
        rectangle = RoundedRectangle(stroke_width = 8, stroke_color = WHITE,
                                     fill_color = BLUE_B, width = 4.5,
                                     height = 2).shift(UP*3 + LEFT*5)

        mathtext = MathTex("\\frac{3}{4} = 0.75").set_color_by_gradient(GREEN, PINK).set_height(1.5)
        mathtext.add_updater(lambda x : x.move_to(rectangle.get_center()))

        self.play(FadeIn(rectangle))
        self.play(Write(mathtext))
        self.play(rectangle.animate.shift(RIGHT*1.5 + DOWN*5), run_time=6)
        self.wait()

        mathtext.clear_updaters()
        self.play(rectangle.animate.shift(LEFT*2 + UP*1), run_time=6)
