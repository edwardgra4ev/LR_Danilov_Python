import pylab
import matplotlib.patches
import matplotlib.lines
import matplotlib.path
import matplotlib.pyplot



def drawCircles (axes):
    """
    Рисование окружностей
    """
    circle1 = matplotlib.patches.Circle((0, 0), radius=0.02, fill=True)
    axes.add_patch (circle1)

    circle2 = matplotlib.patches.Circle((0, 0),
                                        radius=1,
                                        fill=False,
                                        color="r")
    axes.add_patch (circle2)
    pylab.text (0, 1.55, "Окружность", horizontalalignment="center")


def drawlines (axes):
    """
    Рисование линий
    """
    axes.hlines(0, -1.5, 1.5)
    axes.hlines(0.8, -1.5, 1.5)


def shooting_range(axes, x, y):
    if ((-1 <= x <= 1) and (0 <= y <= 0.8)) and 1 >= x**2+y**2:
        #if x<=2 and y <= x and 2<=x*x+y*y:
        circle = matplotlib.patches.Circle((x, y), radius=0.02, fill=True)
        axes.add_patch(circle)
        pylab.text(x-0.2, y-0.2, "Попал", horizontalalignment="center")
    else:
        circle = matplotlib.patches.Circle((x, y), radius=0.02, fill=True)
        axes.add_patch(circle)
        pylab.text(x - 0.2, y - 0.2, "Не попал", horizontalalignment="center")

if __name__ == "__main__":
    pylab.xlim(-1.5, 1.5)
    pylab.ylim(-1.5, 1.5)
    pylab.grid()

    x, y = 0, 0.3

    # Получим текущие оси
    axes = pylab.gca()
    axes.set_aspect("equal")

    drawlines (axes)
    drawCircles (axes)
    shooting_range(axes, x, y)
    pylab.show()