import sdl2_wrapper as draw
from space2d import Renderer
from space2d.Ship import Ship
draw.init()

# renderer.
# draw.line(1, 1, 100, 200)
# draw.circle(0, 0, 250)
shp = Ship()
draw.set_color(128, 0, 200)
while not draw.is_window_closed():
    Renderer.render_ship(shp)
    Renderer.zoom_factor *= 1.00001
    draw.flush_screen()
    draw.clear_screen()