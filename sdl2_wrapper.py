import ctypes
import sdl2.ext as sdl
import sdl2

window_width = window_height = 0
renderer = None
window = None
current_color = sdl.Color(255, 255, 255)
evh = None


def init(windowname='ZOMG FORGOT TO NAME IT', width=640, height=400):
    global renderer, window, window_width, window_height
    window_width = width
    window_height = height
    sdl.init()
    window = sdl.Window(windowname, size=(window_width, window_height))
    window.show()
    renderer = sdl.Renderer(window)
    # renderer = sdl2.SDL_CreateRenderer(
    #     window,
    #     -1,
    #     sdl2.SDL_RENDERER_ACCELERATED | sdl2.SDL_RENDERER_PRESENTVSYNC
    #     )
    # sdl.

def is_window_closed():
    event = sdl2.SDL_Event()
    if sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
        if event.type == sdl2.SDL_QUIT:
            return True
    return False


def clear_screen(r=0, g=0, b=0):
    color = sdl.Color(r, g, b)
    renderer.clear(color)


def read_key():
    event = sdl2.SDL_Event()
    if sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
        if event.type == sdl2.SDL_KeyboardEvent:
            return True


def flush_screen():
    renderer.present()


def set_color(r, g, b):
    global current_color
    current_color = sdl.Color(r, g, b)


def pixel(x, y):
    renderer.draw_point([x, y], current_color)


def line(x1, y1, x2=-1, y2=-1):
    if x2 == y2 == -1:
        renderer.draw_line([int(x1[0]), int(x1[1]), int(y1[0]), int(y1[1])], current_color) # what a shame...
    else:
        renderer.draw_line([int(x1), int(y1), int(x2), int(y2)], current_color)

def multiline(arr_of_verts):
    fuck = []
    for v in arr_of_verts:
        fuck.append(int(v))
    renderer.draw_line(fuck, current_color)


def h_line(x1, x2, y):
    renderer.draw_line([int(x1), int(y), int(x2), int(y)], current_color)


def filled_triangle(x1, y1, x2, y2, x3, y3):
    vertices = [(int(x1), int(y1)), (int(x2), int(y2)), (int(x3), int(y3))]
    high_vert = 0
    low_vert = 0
    for i in [1, 2]:
        if vertices[high_vert][1] > vertices[i][1]:
            high_vert = i
        if vertices[low_vert][1] <= vertices[i][1]:
            low_vert = i
    mid_vert = 3 - high_vert - low_vert

    x_hl = x_hm = vertices[high_vert][0]
    if vertices[high_vert][1] == vertices[mid_vert][1]:
        x_hm = vertices[mid_vert][0]
    dx_hl = (vertices[high_vert][0] - vertices[low_vert][0]) / (vertices[high_vert][1] - vertices[low_vert][1])
    if vertices[high_vert][1] - vertices[mid_vert][1] == 0:
        dx_hm = 0
    else:
        dx_hm = (vertices[high_vert][0] - vertices[mid_vert][0]) / (vertices[high_vert][1] - vertices[mid_vert][1])
    for y in range(vertices[high_vert][1], vertices[mid_vert][1]):
        h_line(x_hl, x_hm, y)
        x_hl += dx_hl
        x_hm += dx_hm
    x_ml = x_hm
    if vertices[mid_vert][1] - vertices[low_vert][1] == 0:
        dx_ml = 0
    else:
        dx_ml = (vertices[mid_vert][0] - vertices[low_vert][0]) / (vertices[mid_vert][1] - vertices[low_vert][1])
    for y in range(vertices[mid_vert][1], vertices[low_vert][1]):
        h_line(x_hl, x_ml, y)
        x_hl += dx_hl
        x_ml += dx_ml


def circle(x0, y0, radius):
    x0 = int(x0)
    y0 = int(y0)
    radius = int(radius)
    x = radius
    y = 0
    dx = 1
    dy = 1
    err = dx - (radius * 2)
    while x >= y:
        pixel(x0 + x, y0 + y)
        pixel(x0 + y, y0 + x)
        pixel(x0 - y, y0 + x)
        pixel(x0 - x, y0 + y)
        pixel(x0 - x, y0 - y)
        pixel(x0 - y, y0 - x)
        pixel(x0 + y, y0 - x)
        pixel(x0 + x, y0 - y)

        if err <= 0:
            y += 1
            err += dy
            dy += 2
        if err > 0:
            x -= 1
            dx += 2
            err += dx - (radius * 2)

########## EXPERIMENTAL #####
