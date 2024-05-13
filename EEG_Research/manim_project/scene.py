import numpy as np
from manim import *

class FourierVisualization(Scene): 
    def construct(self):
        e = ValueTracker(0.01)

        equation_sin = lambda amplitude, frequency, shift, displacement, x: amplitude * \
                                                                np.sin(2 * np.pi / frequency * (x - shift)) + \
                                                                displacement
        equation_exp = lambda amplitude, frequency, shift, displacement, x: amplitude * \
                                                                complex(np.cos(2 * np.pi / frequency * (x - shift)), \
                                                                    np.sin(2 * np.pi / frequency * (x - shift))) + \
                                                                1j * displacement
        
        plane = ComplexPlane(x_length=5, x_range=[-2, 2], y_length=5, y_range=[-2, 2]).add_coordinates()
        plane.shift(LEFT*4)

        graph1 = always_redraw(lambda : 
                    ParametricFunction(lambda t : 
                        plane.polar_to_point(
                            equation_exp(1, 1, np.pi, 0, t), 
                            t), 
                        t_range = [0, e.get_value()], 
                        color = GREEN)
        )

        dot1 = always_redraw(lambda : 
                    Dot(fill_color = GREEN, 
                    fill_opacity = 0.8)
                    .scale(0.5)
                    .move_to(graph1.get_end())
        )

        planeTitle = MathTex(r'ae^{\frac{2i\pi}{f}(x - \phi)} + id', font_size=30, color=GREEN)
        planeTitle.next_to(plane, DOWN)

        axes = Axes(x_length=5, x_range=[0, 8], y_length=5, y_range=[-1.5, 1.5]).add_coordinates()
        axes.shift(RIGHT*4)

        graph2 = always_redraw(lambda : 
                        axes.plot(lambda x : 
                            equation_sin(1, 1, np.pi, 0, x), 
                            x_range = [0, e.get_value()], 
                            color = RED)
        )

        dot2 = always_redraw(lambda : 
                    Dot(fill_color = RED,
                    fill_opacity = 0.8)
                    .scale(0.5)
                    .move_to(graph2.get_end())
        )

        axesTitle = MathTex(r'a\sin(\frac{2\pi}{f}(x - \phi)) + d', font_size=30, color=RED)
        axesTitle.next_to(axes, DOWN)

        title = Text("Pure Sine Waves As Rotating Vectors", font_size=40, color=YELLOW)
        title.to_edge(UP)

        self.play(LaggedStart(
            Write(plane), Create(axes), Write(title), Write(planeTitle), Write(axesTitle),
            run_time=3, lag_ratio=0.5)
        )
        self.add(graph1, dot1, graph2, dot2)
        self.play(e.animate.set_value(2 * PI), run_time=10, rate_func=linear)
        self.wait()
