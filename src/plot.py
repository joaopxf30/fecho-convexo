
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def plota_fecho_convexo(poligono, pontos):
    coords_x = [ponto.coord_x for ponto in pontos]
    coords_y = [ponto.coord_y for ponto in pontos]

    vertices_poligono = [(v.coord_x, v.coord_y) for v in poligono.vertices]

    fig = plt.figure(figsize=(5, 5))

    plot_width, plot_height = 4, 4
    fig_w, fig_h = fig.get_size_inches()
    ax_w = plot_width / fig_w
    ax_h = plot_height / fig_h

    left = (1 - ax_w) / 2
    bottom = (1 - ax_h) / 2

    ax = fig.add_axes((left, bottom, ax_w, ax_h))

    poligono_patch = Polygon(vertices_poligono, closed=True,edgecolor="black", facecolor="lightgray")
    ax.add_patch(poligono_patch)

    xs, ys = zip(*vertices_poligono)
    ax.scatter(xs, ys, color="black", s=20, zorder=3)
    ax.scatter(coords_x, coords_y, color="black", s=20, zorder=3)


    ax.set_title(fr"Polígono $\mathcal{{P}}_{{{len(poligono.vertices)}}}$", fontsize=12)
    ax.set_xlabel(r"$x$", fontsize=12)
    ax.set_ylabel(r"$y$", fontsize=12)

    ax.set_aspect("equal", adjustable="box")

    plt.show()
