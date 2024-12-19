from manim import *

class Shapes(Scene):
    def construct(self):
        ######Code######
        #Making shapes
        circle = Circle()
        square = Square()
        triangle=Polygon(np.array([0,0,0]),np.array([1,1,0]),np.array([1,-1,0])) # create a triangle

        #Showing shapes
        self.play(Create(circle))
        self.play(FadeOut(circle))
        self.play(GrowFromCenter(square))
        self.play(Transform(square,triangle))
        self.wait(1)


class CircleToRectangle(Scene):
    def construct(self):
        circle_1 = Circle(radius=1, color=BLUE)
        circle_2 = Circle(radius=0.5, color=WHITE)
        ellipsis  = Ellipse(width=5, height=4, color=PURPLE)

        square = Square(side_length=3, color=GREEN)
        rectangle = Rectangle(width=5, color=WHITE)

        self.play(Create(circle_1))
        self.play(Create(square))

        self.play(square.animate.set_stroke(YELLOW, width=2)) # animer le changement de couleur

        self.play(
            Transform(square, rectangle),
            circle_1.animate.set_fill(BLUE, opacity=1)
        ) # animer la transformation du rectangle

        self.play(
            GrowFromCenter(circle_2),
            circle_2.animate.set_fill(WHITE, opacity=1),
            run_time = 2
        )

        self.wait(1)
        # add line inside the circle 1
        parts = 4
        for i in range(0, parts):
            angle = i * PI / parts
            radius = circle_1.get_width() / 2

            a = radius * np.array([np.cos(angle), np.sin(angle), 0])
            a_opp = radius * np.array([np.cos(angle + PI), np.sin(angle + PI), 0])
            self.add(Line(start=a, end=a_opp, color=YELLOW))


        self.play(
            FadeOut(square),
            GrowFromCenter(ellipsis)
        )

        self.wait(1)