import sdl2_wrapper as draw
from .ObjectWithModel import ObjectWithModel
from .Model2d import Model2d
from .Planet import Planet

viewpoint = (320.0, 200.0)
zoom_factor = 1.0


def set_viewpoint(x, y):
    viewpoint = (x, y)


def render_planet(planet):
    rad = planet.get_radius()
    cx, cy = planet.get_coords()
    # TODO: clip planet off screen
    sx = viewpoint[0] + cx * zoom_factor
    sy = viewpoint[1] + cy * zoom_factor
    zoomed_radius = rad * zoom_factor
    draw.circle(sx, sy, zoomed_radius)

def render_ship(ship):
    model2d = ship.get_model()
    verts = ship.get_rotated_vertices()
    edges = model2d.get_edges()
    for edge in edges:
        for curr in range(len(edge) - 1): # well fuck
            curr_vert = edge[curr]
            next_vert = edge[curr+1]
            x0 = viewpoint[0] + verts[curr_vert][0] * zoom_factor
            y0 = viewpoint[1] + verts[curr_vert][1] * zoom_factor
            x1 = viewpoint[0] + verts[next_vert][0] * zoom_factor
            y1 = viewpoint[1] + verts[next_vert][1] * zoom_factor
            draw.line(x0, y0, x1, y1)
