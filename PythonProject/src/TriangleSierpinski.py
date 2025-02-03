import turtle
import math

class SierpinskiTriangle:
    """
    A class to represent a Sierpinski Triangle fractal.

    WIDTH_HEIGHT :  The width and height of the drawing area.
    ANGLE :         The angle used for turning the turtle.
    LENGTH :        The length of each side of the triangle.
    """

    WIDTH_HEIGHT = 750
    ANGLE = 120
    LENGTH = 10

    def __init__(self, iterations : int) -> None:
        """
        Initializes the SierpinskiTriangle with the number of iterations.

        iterations : The number of iterations to generate the fractal.
        """
        self.iterations = iterations

    def apply_rules(self, ch: str) -> str:
        """
        Applies the L-system rules to a character.

        ch : The character to apply the rules to.

        Returns: The resulting string after applying the rules.
        """
        if ch == 'F':
            return 'F-G+F+G-F'
        if ch == 'G':
            return 'GG'
        return ch

    def process_string(self, s: str) -> str:
        """
        Processes a string by applying the L-system rules to each character.

        s : The string to process.

        Returns: The resulting string after processing.
        """
        new_str = ''
        for ch in s:
            new_str += self.apply_rules(ch)
        return new_str

    def compute_fractal(self) -> str:
        """
        Computes the fractal string after the given number of iterations.

        Returns: The final fractal string.
        """
        axiom = 'F-G-G'
        s = axiom
        for _ in range(self.iterations):
            s = self.process_string(s)
        return s

    def draw_fractal(self, s: str, length: int):
        """
        Draws the fractal using the turtle graphics module.

        s : The fractal string to draw.
        length : The length of each side of the triangle.
        """
        turtle.speed(0)
        turtle.up()
        turtle.down()
        for ch in s:
            match ch:
                case 'F' | 'G':
                    turtle.forward(length)
                case '+':
                    turtle.right(self.ANGLE)
                case '-':
                    turtle.left(self.ANGLE)
        turtle.done()

    def draw_iteration_number(self):
        """
        Draws the number of iterations on the screen.
        """
        turtle.up()
        turtle.goto(-self.WIDTH_HEIGHT / 2, self.WIDTH_HEIGHT / 2)
        turtle.down()
        turtle.write("ITERATIONS : " + str(self.iterations), align="center", font=("Times", 16, "normal"))

    def show_fractal_generation(self):
        """
        Shows the fractal generation process.
        """
        self.draw_iteration_number()
        turtle.up()
        turtle.goto(-self.WIDTH_HEIGHT / 4, -self.WIDTH_HEIGHT / 4)
        turtle.down()
        turtle.pensize(3)
        s = self.compute_fractal()
        self.draw_fractal(s, 30)

    def show_final_fractal(self):
        """
        Shows a final fractal bigger than the previous one.
        """
        self.draw_iteration_number()
        turtle.hideturtle()
        turtle.tracer(0, 0)
        turtle.up()
        turtle.goto(-self.WIDTH_HEIGHT / 1.7, -self.WIDTH_HEIGHT / 2)
        turtle.down()
        turtle.pensize(1)
        s = self.compute_fractal()
        self.draw_fractal(s, 7)
        turtle.update()
        turtle.showturtle()

if __name__ == '__main__':
    sierpinskiCourt = SierpinskiTriangle(4)
    sierpinskiCourt.show_fractal_generation()

    sierpinskiLong = SierpinskiTriangle(7)
    #sierpinskiLong.show_final_fractal()