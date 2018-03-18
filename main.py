import sdl2_wrapper as draw
from space2d import Renderer
from space2d.Ship import Ship
import debug
import time

debug.do()


draw.init()
shp = Ship()
draw.set_color(128, 0, 200)
while not draw.is_window_closed():
    draw.clear_screen(0, 0, 16)
    Renderer.render_ship(shp)
    Renderer.zoom_factor *= 0.99
    draw.flush_screen()
    time.sleep(0.5)
    shp.rotate(0.2)