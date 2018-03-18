import sdl2.ext as sdl

renderer = None
window = None
current_color = sdl.Color(255, 255, 255)


def init(windowname='ZOMG FORGOT TO NAME IT', width=320, height=200):
    global renderer, window
    sdl.init()
    window = sdl.Window(windowname, size=(width, height))
    window.show()
    renderer = sdl.Renderer(window)


def proc_fuck():
    processor = sdl.TestEventProcessor()
    processor.run(window)


def flush_screen():
    renderer.present()


def pixel(x, y):
    renderer.draw_point([x, y])


def line(x1, y1, x2, y2):
    renderer.draw_line([x1, y1, x2, y2])


def circle(x0, y0, radius):
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
