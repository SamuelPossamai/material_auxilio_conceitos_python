
class SVG:

    def __init__(self, elements=()):
        self.elements = list(elements)

    def add_element(self, element):
        self.elements.append(element)

        return True

    def toSVG(self):

        elements_to_svg = (el.toSVG() for el in self.elements)
        return f'<svg>{"".join(elements_to_svg)}</svg>'
