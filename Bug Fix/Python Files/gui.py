from cubemesh import *
from face import *
import cubemesh

# from matplotlib.widgets import Button

#----------------------------------------------------------------------------------------------------------------------------------------------------

def poly_to_cart(length, degree):
    # Länge wird mit Cos von Grad zu Bogenmaß umgerechnet
    # Length is converted from degrees to radians using cos
    x = length * np.cos(np.deg2rad(degree))
    # Länge wird mit Sin von Grad zu Bogenmaß umgerechnet
    # Length is converted from degrees to radians using Sin
    y = length * np.sin(np.deg2rad(degree))
    return x, y

#----------------------------------------------------------------------------------------------------------------------------------------------------

# Legt die Länge des Würfels und dessen Kanten fes
# Specifies the length of the cube and its edges
length = 5

#----------------------------------------------------------------------------------------------------------------------------------------------------

def drawing():
    #--------------------------------------------------------------------------------------
    
    #cubemesh.up_counter()
    #cubemesh.debug()

    #--------------------------------------------------------------------------------------

    print(cubemesh.cube)
    
    #--------------------------------------------------------------------------------------

    # links farbe
    # left color
    faces = np.empty(shape=(3, 3, 3), dtype=face)

    for number in range(1, 4, 1):
        for number2 in range(1, 4, 1):
            faces[0, 3 - number, 3 - number2] = face(
                (poly_to_cart((number / 3) * length, 150)[0],
                 poly_to_cart((number / 3) * length, 150)[1] - (
                         (number2 - 1) / 3) * length),
                (poly_to_cart((number / 3) * length, 150)[0],
                 poly_to_cart((number / 3) * length, 150)[1] - (
                         number2 / 3) * length),
                (poly_to_cart(((number - 1) / 3) * length, 150)[0],
                 poly_to_cart(((number - 1) / 3) * length, 150)[1] - (
                         (number2 / 3) * length)),
                (poly_to_cart(((number - 1) / 3) * length, 150)[0],
                 poly_to_cart(((number - 1) / 3) * length, 150)[1]),
                "blue"
            )

    #--------------------------------------------------------------------------------------

    # rechts farbe
    # right color
    for number in range(1, 4, 1):
        for number2 in range(1, 4, 1):
            faces[1, number - 1, 3 - number2] = face(
                (poly_to_cart((number / 3) * length, 30)[0],
                 poly_to_cart((number / 3) * length, 30)[1] - (
                         (number2 - 1) / 3) * length),
                (poly_to_cart((number / 3) * length, 30)[0],
                 poly_to_cart((number / 3) * length, 30)[1] - (
                         number2 / 3) * length),
                (poly_to_cart(((number - 1) / 3) * length, 30)[0],
                 poly_to_cart(((number - 1) / 3) * length, 30)[1] - (
                         (number2 / 3) * length)),
                (poly_to_cart(((number - 1) / 3) * length, 30)[0],
                 poly_to_cart(((number - 1) / 3) * length, 30)[1]),
                "red"
            )

    #--------------------------------------------------------------------------------------

    # oben farbe
    # above color
    faces[2, 2, 0] = face(
        (0, 0),
        (poly_to_cart((1 / 3) * length, 30)[0],
         poly_to_cart((1 / 3) * length, 30)[1]),
        (0, 2 * poly_to_cart((1 / 3) * length, 30)[1]),
        (poly_to_cart((1 / 3) * length, 150)[0],
         poly_to_cart((1 / 3) * length, 150)[1]),
        "yellow")

    faces[2, 2, 1] = face(
        (poly_to_cart((1 / 3) * length, 30)[0], poly_to_cart((1 / 3) * length, 30)[1]),
        (poly_to_cart((2 / 3) * length, 30)[0],
         poly_to_cart((2 / 3) * length, 30)[1]),
        (poly_to_cart((1 / 3) * length, 30)[0], 3 * poly_to_cart((1 / 3) * length, 30)[1]),
        (0, 2 * poly_to_cart((1 / 3) * length, 30)[1]),
        "yellow")

    faces[2, 2, 2] = face(
        (poly_to_cart((2 / 3) * length, 30)[0], poly_to_cart((2 / 3) * length, 30)[1]),
        (poly_to_cart((3 / 3) * length, 30)[0],
         poly_to_cart((3 / 3) * length, 30)[1]),
        (poly_to_cart((2 / 3) * length, 30)[0], 4 * poly_to_cart((1 / 3) * length, 30)[1]),
        (poly_to_cart((1 / 3) * length, 30)[0], 3 * poly_to_cart((1 / 3) * length, 30)[1]),
        "yellow")

    faces[2, 1, 0] = face(
        (poly_to_cart((1 / 3) * length, 150)[0], poly_to_cart((1 / 3) * length, 150)[1]),
        (poly_to_cart((2 / 3) * length, 150)[0],
         poly_to_cart((2 / 3) * length, 150)[1]),
        (poly_to_cart((1 / 3) * length, 150)[0], 3 * poly_to_cart((1 / 3) * length, 150)[1]),
        (0, 2 * poly_to_cart((1 / 3) * length, 150)[1]),
        "yellow")

    faces[2, 0, 0] = face(
        (poly_to_cart((2 / 3) * length, 150)[0], poly_to_cart((2 / 3) * length, 150)[1]),
        (poly_to_cart((3 / 3) * length, 150)[0],
         poly_to_cart((3 / 3) * length, 150)[1]),
        (poly_to_cart((2 / 3) * length, 150)[0], 4 * poly_to_cart((1 / 3) * length, 150)[1]),
        (poly_to_cart((1 / 3) * length, 150)[0], 3 * poly_to_cart((1 / 3) * length, 150)[1]),
        "yellow")

    faces[2, 1, 1] = face(
        (0, 2 * poly_to_cart((1 / 3) * length, 30)[1]),
        (poly_to_cart((1 / 3) * length, 30)[0],
         3 * poly_to_cart((1 / 3) * length, 30)[1]),
        (0, 2 * poly_to_cart((2 / 3) * length, 30)[1]),
        (poly_to_cart((1 / 3) * length, 150)[0],
         3 * poly_to_cart((1 / 3) * length, 150)[1]),
        "yellow")

    faces[2, 1, 2] = face(
        (poly_to_cart((1 / 3) * length, 30)[0], poly_to_cart((3 / 3) * length, 30)[1]),
        (poly_to_cart((2 / 3) * length, 30)[0],
         poly_to_cart((4 / 3) * length, 30)[1]),
        (poly_to_cart((1 / 3) * length, 30)[0], 5 * poly_to_cart((1 / 3) * length, 30)[1]),
        (0, 4 * poly_to_cart((1 / 3) * length, 30)[1]),
        "yellow")

    faces[2, 0, 1] = face(
        (poly_to_cart((1 / 3) * length, 150)[0], poly_to_cart((3 / 3) * length, 150)[1]),
        (poly_to_cart((2 / 3) * length, 150)[0],
         poly_to_cart((4 / 3) * length, 150)[1]),
        (poly_to_cart((1 / 3) * length, 150)[0], 5 * poly_to_cart((1 / 3) * length, 150)[1]),
        (0, 4 * poly_to_cart((1 / 3) * length, 30)[1]),
        "yellow")

    faces[2, 0, 2] = face(
        (0, 4 * poly_to_cart((1 / 3) * length, 30)[1]),
        (poly_to_cart((1 / 3) * length, 30)[0],
         5 * poly_to_cart((1 / 3) * length, 30)[1]),
        (0, 3 * poly_to_cart((2 / 3) * length, 30)[1]),
        (poly_to_cart((1 / 3) * length, 150)[0],
         5 * poly_to_cart((1 / 3) * length, 150)[1]),
        "yellow")
    
    #--------------------------------------------------------------------------------------

    for i in range(3):
        for j in range(3):
            faces[0, i, j].update_color(cube[2, i, j])

    for i in range(3):
        for j in range(3):
            faces[1, i, j].update_color(cube[5, i, j])

    for i in range(3):
        for j in range(3):
            faces[2, i, j].update_color(cube[1, i, j])

    #--------------------------------------------------------------------------------------

    # Innere Linien
    # Inner Lines
    inner1 = plt.Line2D([0, 0], [-length, 0])
    inner2 = plt.Line2D([0, poly_to_cart(length, 30)[0]], [0, poly_to_cart(length, 30)[1]])
    inner3 = plt.Line2D([0, poly_to_cart(length, 150)[0]], [0, poly_to_cart(length, 150)[1]])
    plt.gca().add_line(inner1)
    plt.gca().add_line(inner2)
    plt.gca().add_line(inner3)

    #--------------------------------------------------------------------------------------

    # Obere Linien
    # top lines
    top1 = plt.Line2D([poly_to_cart(
        length, 150)[0], 0], [poly_to_cart(length, 150)[1], 2 * poly_to_cart(length, 150)[1]])
    top2 = plt.Line2D([poly_to_cart(length, 30)[0], 0], [poly_to_cart(length, 30)[1], 2 * poly_to_cart(length, 30)[1]])
    top3 = plt.Line2D(
        [poly_to_cart(length / 3, 30)[0], poly_to_cart(length, 150)[0] - poly_to_cart(length / 3, 150)[0]],
        [poly_to_cart(length / 3, 30)[1], poly_to_cart(length, 150)[1] + poly_to_cart(length / 3, 30)[1]])
    top4 = plt.Line2D(
        [poly_to_cart((length / 3) * 2, 30)[0], poly_to_cart(length, 150)[0] - poly_to_cart((length / 3) * 2, 150)[0]],
        [poly_to_cart((length / 3) * 2, 30)[1], poly_to_cart(length, 150)[1] + poly_to_cart((length / 3) * 2, 30)[1]])

    top5 = plt.Line2D(
        [poly_to_cart(length / 3, 150)[0], poly_to_cart(length, 30)[0] - poly_to_cart(length / 3, 30)[0]],
        [poly_to_cart(length / 3, 150)[1], poly_to_cart(length, 30)[1] + poly_to_cart(length / 3, 30)[1]])

    top6 = plt.Line2D(
        [poly_to_cart((length / 3) * 2, 150)[0], poly_to_cart(length, 30)[0] - poly_to_cart((length / 3) * 2, 30)[0]],
        [poly_to_cart((length / 3) * 2, 150)[1], poly_to_cart(length, 150)[1] + poly_to_cart((length / 3) * 2, 30)[1]])

    plt.gca().add_line(top1)
    plt.gca().add_line(top2)
    plt.gca().add_line(top3)
    plt.gca().add_line(top4)
    plt.gca().add_line(top5)
    plt.gca().add_line(top6)

    #--------------------------------------------------------------------------------------

    # Unten
    # Below
    bot1 = plt.Line2D([0, poly_to_cart(length, 30)[0]], [-length, poly_to_cart(-length, 30)[1]])

    bot2 = plt.Line2D([0, poly_to_cart(length, 150)[0]], [-length, poly_to_cart(-length, 150)[1]])
    plt.gca().add_line(bot1)
    plt.gca().add_line(bot2)

    #--------------------------------------------------------------------------------------

    # Rechts
    # Right
    right = plt.Line2D([poly_to_cart(length, 30)[0], poly_to_cart(length, 30)[0]],
                       [poly_to_cart(length, 30)[1], poly_to_cart(-length, 30)[1]])
    plt.gca().add_line(right)

    rightvertical1 = plt.Line2D([poly_to_cart(length / 3, 30)[0], poly_to_cart(length / 3, 30)[0]],
                                [poly_to_cart(length / 3, 30)[1], poly_to_cart(length / 3, 30)[1] - length])
    plt.gca().add_line(rightvertical1)

    rightvertical2 = plt.Line2D([poly_to_cart((length / 3) * 2, 30)[0], poly_to_cart((length / 3) * 2, 30)[0]],
                                [poly_to_cart((length / 3) * 2, 30)[1], poly_to_cart((length / 3) * 2, 30)[1] - length])
    plt.gca().add_line(rightvertical2)

    righthorizontal1 = plt.Line2D([poly_to_cart(length, 30)[0], poly_to_cart(0, 30)[0]],
                                  [poly_to_cart(length / 3, 30)[1], - length / 3])
    plt.gca().add_line(righthorizontal1)

    righthorizontal2 = plt.Line2D([poly_to_cart(length, 30)[0], poly_to_cart(0, 30)[0]],
                                  [poly_to_cart(length, 30)[1] - (length / 3) * 2, (- length / 3) * 2])
    plt.gca().add_line(righthorizontal2)

    #--------------------------------------------------------------------------------------

    # Links
    # left
    left = plt.Line2D([poly_to_cart(length, 150)[0], poly_to_cart(length, 150)[0]],
                      [poly_to_cart(length, 150)[1], poly_to_cart(-length, 150)[1]])
    plt.gca().add_line(left)

    leftvertical1 = plt.Line2D([poly_to_cart(length / 3, 150)[0], poly_to_cart(length / 3, 150)[0]],
                               [poly_to_cart(length / 3, 150)[1], poly_to_cart(length / 3, 150)[1] - length])
    plt.gca().add_line(leftvertical1)

    leftvertical2 = plt.Line2D([poly_to_cart((length / 3) * 2, 150)[0], poly_to_cart((length / 3) * 2, 150)[0]],
                               [poly_to_cart((length / 3) * 2, 150)[1],
                                poly_to_cart((length / 3) * 2, 150)[1] - length])
    plt.gca().add_line(leftvertical2)

    righthorizontal1 = plt.Line2D([poly_to_cart(length, 150)[0], poly_to_cart(0, 150)[0]],
                                  [poly_to_cart(length / 3, 150)[1], - length / 3])
    plt.gca().add_line(righthorizontal1)

    righthorizontal2 = plt.Line2D([poly_to_cart(length, 150)[0], poly_to_cart(0, 150)[0]],
                                  [poly_to_cart(length, 150)[1] - (length / 3) * 2, (- length / 3) * 2])
    plt.gca().add_line(righthorizontal2)

    #--------------------------------------------------------------------------------------

    # Macht Fenster zu einem Quadrat
    # Makes windows into a square
    plt.axis("square")

    #--------------------------------------------------------------------------------------

    # Setzt min und max Koordinaten für x und y
    # Set min and max coordinates for x and y
    plt.xlim([-10, 10])
    plt.ylim([-10, 10])

    #--------------------------------------------------------------------------------------

    # Entfernt beschriftung für x und y Achse
    # Removed labeling for x and y axis
    plt.xticks([])
    plt.yticks([])

    plt.title(r'$RubiksCubeGUI$')

    #--------------------------------------------------------------------------------------

    # Generiert das Fenster
    # Generates the window
    plt.show()
