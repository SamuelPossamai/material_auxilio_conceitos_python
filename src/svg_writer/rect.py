
class Rect:

    def __init__(self, position, size, stroke='black', stroke_width=1,
                 fill='transparent'):

        self.position = position
        self.size = size
        self.stroke = stroke
        self.stroke_width = stroke_width
        self.fill = fill

    def toSVG(self):
        return (
            f'<rect x="{self.position[0]}" y="{self.position[1]}" width="{self.size[0]}" '
            f'height="{self.size[1]}" stroke="{self.stroke}" '
            f'stroke-width="{self.stroke_width}" fill="{self.fill}" />'
        )
