import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
import the_cube as cube
import pointy as pointy
import extended_cube as xtcube
import the_basic_prism as prism
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from pointy import mod_space

# prism_figure = plt.axes(projection='3d')
# prism_figure.set_xlim(1, 9)
# prism_figure.set_ylim(-1, 7)
# prism_figure.set_zlim(3, 11)

free_points = prism.prism_filter(xtcube.extend_cube(pointy.the_point_of_it_all(pointy.all_opt_forms)))
connect_points = prism.prism_filter(xtcube.extend_cube(pointy.the_point_of_it_all(pointy.triads)))
only_rojavai = prism.prism_filter(xtcube.extend_cube(pointy.the_point_of_it_all(pointy.rojavai_forms)))


def plot_neighbors(form_list):
    connect_pool = []

    for form in form_list:
        for point in form:
            connect_pool.append(point)

    for point in connect_pool:
        # transpose by one step in a direction
        # if in transposed point in connect_pool, make a pair with point
        for transposer in [1, -1]:
            for i in range(0, 3):
                candidate_neighbor = point.copy()
                candidate_neighbor[i] = point[i] + transposer
                if candidate_neighbor in connect_pool:
                    neighbor_pair = [point, candidate_neighbor]
                    X, Y, Z = zip(*neighbor_pair)
                    cube.the_cube_plot.plot(X, Y, Z, color='black', linewidth = .5)


def plot_prism_walls():
    # bottom triangle, sum class 12 (5 mod-12)
    A = (8, 8, 8)
    B = (12, 0, 12)
    C = (4, 4, 16)#(17/3, 17/3, 38/3)
    # top triangle
    D = (8, 8, 20)
    E = (12, 12, 12)#(31/3, 31/3, 31/3)
    F = (16, 4, 16)
    faces = [[A, B, C], [D, E, F], [A, B, F, E], [C, A, E, D]]
    walls = Poly3DCollection(faces, edgecolors='black', linewidths=.2, alpha=.2)
    cube.the_cube_plot.add_collection3d(walls)


plot_prism_walls()
cube.the_cube_plot.set_axis_off()
cube.the_cube_plot.set_xlim(1, (mod_space + 2))
cube.the_cube_plot.set_ylim(-1, mod_space)
cube.the_cube_plot.set_zlim(3, (mod_space + 4))

plot_neighbors(connect_points)
cube.plot_it(connect_points)
cube.plot_transparent(free_points)
plt.show()