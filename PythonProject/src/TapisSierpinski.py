import turtle


class SierpinskiCarpet:
    """
    A class to represent a Menger Sponge fractal.

    WIDTH_HEIGHT :  The width and height of the drawing area.
    ANGLE :         The angle used for turning the turtle.
    LENGTH :        The length of each side of the sponge.
    """

    WIDTH_HEIGHT = 750
    ANGLE = 90
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
            return 'F+F-F-F-UGD+F+F+F-F'
        if ch == 'G':
            return 'GGG'
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
        axiom = 'F'
        s = axiom
        for _ in range(self.iterations):
            s = self.process_string(s)
        return s

    def draw_fractal(self, s: str, length: int):
        """
        Draws the fractal using the turtle graphics module.

        s : The fractal string to draw.
        length : The length of each side of the sponge.
        """
        turtle.speed(0)
        for ch in s:
            match ch:
                case 'F':
                    turtle.forward(length)
                case 'G':
                    turtle.forward(length)
                case 'U':
                    turtle.up()
                case 'D':
                    turtle.down()
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
        turtle.goto(-self.WIDTH_HEIGHT / 4, 0)
        turtle.down()
        turtle.pensize(2)
        s = self.compute_fractal()
        self.draw_fractal(s, 15)

    def show_final_fractal(self):
        """
        Shows a final fractal bigger than the previous one.
        """
        self.draw_iteration_number()
        turtle.hideturtle()
        turtle.tracer(0, 0)
        turtle.up()
        turtle.goto(-self.WIDTH_HEIGHT / 1.6, 0)
        turtle.down()
        turtle.pensize(1)
        s = self.compute_fractal()
        self.draw_fractal(s, 3)
        turtle.update()
        turtle.showturtle()

if __name__ == '__main__':
    sierpinskiCarpetSmall = SierpinskiCarpet(3)
    #sierpinskiCarpetSmall.show_fractal_generation()

    sierpinskiCarpetLarge = SierpinskiCarpet(5)
    sierpinskiCarpetLarge.show_final_fractal()