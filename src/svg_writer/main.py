
import os
from pathlib import Path

from circle import Circle
from rect import Rect
from svg import SVG

#circle = Circle((50, 50), 50, fill='white')
rect = Rect((0, 0), (300, 100), fill='blue', stroke='green', stroke_width=10)

a = Circle((50, 50), 50, fill='white')
b = a.copy()

b.center = (150, 50)

c = b.copy()

c.center = (250, 50)

svg = SVG([
    rect,
    a,
    b
])

#svg.add_element(c)

content = svg.toSVG()

print(content.replace('><', '>\n<'))

filepath = Path.home().joinpath('exemplo.svg')

with open(filepath, 'w') as file:
    file.write(content)

os.system(f'gwenview {filepath}')

filepath.unlink()
