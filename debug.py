from space2d.Math import *
from space2d import SystemController
from space2d.space_objects.Model2d import Model2d
import sdl2_wrapper as draw
import random, time

def do():

    points = [(-100, -100), (45, 45), (-45, 45)]

    # draw.filled_circle(320, 200, 50)
    # draw.flush_screen()
    # time.sleep(5)
    #
    # for i in range(360):
    #     draw.set_color(255, 0, 255)
    #     draw.multiline([points[0][0]+200, points[0][1]+200, points[1][0]+200, points[1][1]+200,
    #                          points[2][0]+200, points[2][1]+200, points[0][0]+200, points[0][1]+200])
    #     draw.set_color(255, 255, 255)
    #     draw.filled_triangle(points[0][0]+200, points[0][1]+200, points[1][0]+200, points[1][1]+200,
    #                          points[2][0]+200, points[2][1]+200)
    #     draw.flush_screen()
    #     # print(points)
    #     time.sleep(0.1)
    #     for j in range(len(points)):
    #         points[j] = rotate_vector(points[j], 3.14159/180.0)
    #     draw.clear_screen()

    count_exec_time(draw_n_triangles, '100 triangles')
    count_exec_time(draw_n_circles, '100 circles')
    count_exec_time(draw.flush_screen, 'buffer output')
    # SystemController.control()

def render_triangle(mdl):
    model2d = mdl
    verts = model2d.get_vertices()
    edges = model2d.get_edges()
    cx, cy = 0, 0
    for edge in edges:
        for curr in range(len(edge) - 1): # well fuck
            curr_vert = edge[curr]
            next_vert = edge[curr+1]
            x0 = (cx + verts[curr_vert][0]) + 200
            y0 = (cy + verts[curr_vert][1]) + 200
            x1 = (cx + verts[next_vert][0]) + 200
            y1 = (cy + verts[next_vert][1]) + 200
            draw.line(x0, y0, x1, y1)


def draw_n_triangles():
    for i in range(100):
        draw.set_color(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
        draw.filled_triangle(random.randint(0, 640),random.randint(0, 400),random.randint(0, 640),random.randint(0, 400),
                             random.randint(0, 640),random.randint(0, 400))


def draw_n_circles():
    for i in range(100):
        draw.set_color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw.filled_circle(random.randint(0, 640), random.randint(0, 400), random.randint(0, 100))


def count_exec_time(func, text):
    start_time = time.time()
    func()
    elapsed_time = time.time() - start_time
    print('Time for {}: {}'.format(text, elapsed_time))
