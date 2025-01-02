from manim import *
from numpy import *
from scipy.integrate import solve_ivp

""" For the camera :
- Theta : represents the rotation around Z axis
- Phi : represents the rotation on X axis
- Gamma : the rotation around the axis formed by the camera and the origin

Initially, the camera is stick to the Z axis
"""

class LorenzAttractorScene(ThreeDScene):
    pos = array([0.1, 0, 0])
    num_points = int(1e4)
    sim_time = 50
    constants = (10, 28, 8/3)

    def construct(self):
        self.set_camera_orientation(45, 60, 0)

        lorenz_curve = self.get_lorenz_curve()
        lorenz_curve.set_width(config.frame_width /2.5).center()
        lorenz_curve.set_color_by_gradient(DARK_BLUE, WHITE, GREEN)
        self.play(
            Create(lorenz_curve),
            run_time = self.sim_time
        )

    def get_lorenz_curve(self):
        pts = np.empty(self.num_points, 3)
        x, y, z = pts[0] = self.pos
        dt = self.sim_time / self.num_points

        for i in range(1, self.num_points):
            x_dot, y_dot, z_dot = self.update_curve(pos=(x, y, z))
            x += x_dot * dt
            y += y_dot * dt
            z += z_dot * dt

        curve = ParametricFunction(
            function= lambda i: pts[i],
            t_range=[0, self.num_points-1, 1]
        ).set_flat_stroke(False)

        return curve

    def update_curve(self, t=None ,pos=None):
        x, y, z = pos
        a, b, c = self.constants
        x_dot = a * (y - x)
        y_dot = x * (b - z) - y
        z_dot = x * y - c * z
        return array([x_dot, y_dot, z_dot])

class ImprovedLorenzAttractorScene(LorenzAttractorScene):
    def get_lorenz_curve(self):
        dt = self.sim_time / self.num_points

        solution = solve_ivp(
            fun=self.update_curve,
            t_span=(0.0, self.sim_time),
            y0=self.pos,
            dense_output=True
        )

        curve = ParametricFunction(
            function=lambda t: solution.sol(t),
            t_range=(0, self.sim_time, dt)
        ).set_flat_stroke(False)

        return curve


