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


def h_line(x1, x2, y):
    renderer.draw_line([int(x1), int(y), int(x2), int(y)], current_color)


def filled_triangle(x1, y1, x2, y2, x3, y3):
    # highest_y = y1
    # if y2 < highest_y:
    #     highest_y = y2
    # if y3 < highest_y:
    #     highest_y = y3
    # lowest_y = y1
    # if y2 > lowest_y:
    #     lowest_y = y2
    # if y3 > lowest_y:
    #     lowest_y = y3
    highest_y = min(y1, y2, y3)
    lowest_y = max(y1, y2, y3)
    mid_y = y1 + y2 + y3 - highest_y - lowest_y
    max_x = max(x1, x2, x3)
    min_x = min(x1, x2, x3)
    mid_x = x1 + x2 + x3 - max_x - min_x
    # shit begins here
    left_dx = (x3-x1) / (y3 - y1)
    right_dx = (x2-x1) / (y2 - y1)
    cur_x1 = float(mid_x)
    cur_x2 = float(mid_x)
    for y in range(highest_y, lowest_y):
        h_line(cur_x1, cur_x2, y)
        x1 += left_dx
        x2 += right_dx
    # TODO: do this
    # Draws filled triangle


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
