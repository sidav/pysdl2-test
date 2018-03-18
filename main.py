import sdl2_wrapper as draw
from space2d import Renderer
from space2d.Ship import Ship
draw.init()

# renderer.
# draw.line(1, 1, 100, 200)
# draw.circle(0, 0, 250)
shp = Ship()
Renderer.render_ship(shp)
draw.flush_screen()
draw.proc_fuck()