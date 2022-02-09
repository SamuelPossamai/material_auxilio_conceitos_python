
class Circle:

    def __init__(self, center, radius, stroke='black', stroke_width=1,
                 fill='transparent'):

        self.center = center
        self.radius = radius
        self.stroke = stroke
        self.stroke_width = stroke_width
        self.fill = fill

    def copy(self):

        return Circle(self.center, self.radius, stroke=self.stroke,
                      stroke_width=self.stroke_width, fill=self.fill)

    def toSVG(self):
        return (
            f'<circle cx="{self.center[0]}" cy="{self.center[1]}" r="{self.radius}" '
            f'stroke="{self.stroke}" stroke-width="{self.stroke_width}" fill="{self.fill}" />'
        )
