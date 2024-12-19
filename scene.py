from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

        # Shift the circle
        self.wait(1)
        circle.shift(RIGHT)
        self.wait()


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle() # create a circle
        circle.set_fill(PINK, opacity=0.5)

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation


class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()       # create a circle
        circle.set_fill(PURPLE, opacity=0.5)

        square = Square()
        square.set_fill(BLUE, opacity=0.5)

        square.next_to(circle, LEFT, buff=0.5)
        self.play(Create(circle), Create(square))


class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle() # create a circle
        square = Square()

        square.next_to(circle, LEFT, buff=1)

        self.play(Create(square))
        self.play(square.animate.rotate(PI / 4)) # rotate the square

        self.play(Transform(square, circle))

        self.play(
            square.animate.set_fill(PINK, opacity=0.5)
        )

        self.play(Transform(circle, square))

        self.play(
            square.animate.shift(3 * LEFT)
        )


class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)

        self.play(
            left_square.animate.rotate(PI),
            Rotate(right_square, angle=PI),
            run_time = 2
        )

class WeirdSquare(Scene):
    def construct(self):
        square = Square()

        self.play(FadeIn(square))
        square.set_fill(PURE_GREEN)

        self.play(
            square.animate.set_fill(PURE_GREEN).shift(3 * UP).rotate(PI / 4)
        )
        self.wait(1)

        self.play(
            FadeOut(square)
        )

        self.wait(2)


class MobjectExample(Scene):
    def construct(self):
        p1 = [-1,-1, 0]
        p2 = [ 1,-1, 0]
        p3 = [ 1, 1, 0]
        p4 = [-1, 1, 0]
        a  = Line(p1,p2).append_points(Line(p2,p3).points)

        point_start  = a.get_start()
        point_end    = a.get_end()
        point_center = a.get_center()

        self.add(Text(f"a.get_start() = {np.round(point_start,2).tolist()}", font_size=24).to_edge(UR).set_color(YELLOW))
        self.add(Text(f"a.get_end() = {np.round(point_end,2).tolist()}", font_size=24).next_to(self.mobjects[-1],DOWN).set_color(RED))
        self.add(Text(f"a.get_center() = {np.round(point_center,2).tolist()}", font_size=24).next_to(self.mobjects[-1],DOWN).set_color(BLUE))

        self.add(Dot(a.get_start()).set_color(YELLOW).scale(2))
        self.add(Dot(a.get_end()).set_color(RED).scale(2))
        self.add(Dot(a.get_top()).set_color(GREEN_A).scale(2))
        self.add(Dot(a.get_bottom()).set_color(GREEN_D).scale(2))
        self.add(Dot(a.get_center()).set_color(BLUE).scale(2))
        self.add(Dot(a.point_from_proportion(0.5)).set_color(ORANGE).scale(2))
        self.add(*[Dot(x) for x in a.points])
        self.add(a)