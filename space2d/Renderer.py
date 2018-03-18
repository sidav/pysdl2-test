import sdl2_wrapper as draw
from .Ship import Ship
from .Model2d import Model2d

viewpoint = (160, 100)

def set_viewpoint(x, y):
    viewpoint = (x, y)


def render_ship(ship):
    model2d = ship.get_model()
    verts = model2d.get_rotated_vertices()
    verts = model2d.get_vertices()
    edges = model2d.get_edges()
    for edge in edges:
        for curr in range(len(edge) - 1): # well fuck
            curr_vert = edge[curr]
            next_vert = edge[curr+1]
            x0 = viewpoint[0] + int(verts[curr_vert][0])
            y0 = viewpoint[1] + int(verts[curr_vert][1])
            x1 = viewpoint[0] + int(verts[next_vert][0])
            y1 = viewpoint[1] + int(verts[next_vert][1])
            draw.line(x0, y0, x1, y1)
