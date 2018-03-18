import sdl2_wrapper as draw

viewpoint = (320.0, 200.0)
zoom_factor = 0.01

def clear():
    draw.clear_screen()

def set_viewpoint(x, y):
    WIDTH = draw.window_width
    HEIGHT = draw.window_height
    global viewpoint
    viewpoint = (x * zoom_factor - WIDTH // 2, y * zoom_factor - HEIGHT // 2)


def render_planet(planet):
    rad = planet.get_radius()
    cx, cy = planet.get_coords()
    # TODO: clip planet off screen
    sx = cx * zoom_factor - viewpoint[0]
    sy = cy * zoom_factor - viewpoint[1]
    zoomed_radius = rad * zoom_factor
    draw.circle(sx, sy, zoomed_radius)


def render_object_with_model(obj):
    model2d = obj.get_model()
    verts = obj.get_rotated_vertices()
    edges = model2d.get_edges()
    cx, cy = obj.get_coords()
    for edge in edges:
        for curr in range(len(edge) - 1): # well fuck
            curr_vert = edge[curr]
            next_vert = edge[curr+1]
            x0 = (cx + verts[curr_vert][0]) * zoom_factor - viewpoint[0]
            y0 = (cy + verts[curr_vert][1]) * zoom_factor - viewpoint[1]
            x1 = (cx + verts[next_vert][0]) * zoom_factor - viewpoint[0]
            y1 = (cy + verts[next_vert][1]) * zoom_factor - viewpoint[1]
            draw.line(x0, y0, x1, y1)
