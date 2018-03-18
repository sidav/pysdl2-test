import sdl2_wrapper as draw
from space2d import Renderer
from space2d.space_objects.ObjectWithModel import ObjectWithModel
from space2d.space_objects.Planet import Planet
import debug
import time

draw.init()

debug.do()
time.sleep(10.0)

shp = ObjectWithModel(0, 0)
planet = Planet(10.0, 50.0)
draw.set_color(128, 0, 200)
x = 0
y = 0

while not draw.is_window_closed() and not draw.read_key():
    draw.clear_screen(0, 0, 16)
    Renderer.render_object_with_model(shp)
    Renderer.set_viewpoint(x, y)
    x -= 1
    y -= 1
    # Renderer.render_planet(planet)
    # Renderer.zoom_factor *= 0.9
    draw.flush_screen()
    time.sleep(0.1)
    shp.rotate(0.2)