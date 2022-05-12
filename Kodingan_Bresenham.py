# Nama  : Wahid amin samsudin
# NIM   : 20051397077
# Kelas : D4 Manajemen Informatika - 2020A

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-100.0, 100.0, -100.0, 100.0)
    glPointSize(5)


def plot(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def bresenham_circle_drawing(r):

    # tempat lingkaran hasil output
    x_position = 50
    y_position = -45

    x = 0
    y = r

    # parameter keputusan
    d = 3 - 2 * r

    # membuat titik koordinat
    plot(x + x_position, y + y_position)

    while y > x:

        if d < 0:
            x += 1
            d += 4 * x + 6
        else:
            x += 1
            y -= 1
            d += (4 * (x - y)) + 6

        # mencari nilai (x, y)
        # membalikkan nilai menjadi (y, x)

        #nilai (x, y)

        # kuadran 1
        plot(x + x_position, y + y_position)

        # kuadran 2
        plot(x + x_position, -y + y_position)

        # kuadran 3
        plot(-x + x_position, -y + y_position)

        # kuadran 4
        plot(-x + x_position, y + y_position)

        #nilai (y, x)

        # kuadran 1
        plot(y + x_position, x + y_position)

        # kuadran 2
        plot(-y + x_position, x + y_position)

        # kuadran 3
        plot(-y + x_position, -x + y_position)

        # kuadran 4
        plot(y + x_position, -x + y_position)


def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 1.0, 1.0)
    glBegin(GL_LINES)
    glVertex2f(-100, 0)
    glVertex2f(100, 0)
    glVertex2f(0, -100)
    glVertex2f(0, 100)
    glEnd()

    bresenham_circle_drawing(40)

    glFlush()

# menampilkan hasil output


def main():
    # menampilkan hasil output
    glutInit(sys.argv)
    # inisialisasi tipe display glut
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    # inisialisasi ukuran layar glut
    glutInitWindowSize(400, 400)
    # inisiasliasi posisi layar glut
    glutInitWindowPosition(200, 200)
    # inisialisasi pembuatan window
    glutCreateWindow("Bresenham Lingkaran")
    glutDisplayFunc(plotpoints)

    init()
    glutMainLoop()


main()
