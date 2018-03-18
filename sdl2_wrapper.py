import sdl2.ext as sdl

renderer = None
window = None


def init(windowname='ZOMG FORGOT TO NAME IT', width=320, height=200):
    global renderer, window
    sdl.init()
    window = sdl.Window(windowname, size=(width, height))
    window.show()
    renderer = sdl.Renderer(window)
    # processor = sdl.TestEventProcessor()
    # processor.run(window)


def flush_screen():
    renderer.present()


def line(x1, y1, x2, y2):
    renderer.draw_line([x1, y1, x2, y2])
