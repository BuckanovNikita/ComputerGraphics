from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

ctrlpoints_1 = [
    [
        [-2, -2, 0],
        [-3, -1, 0],
        [-3, 1, 0],
        [-2, 2, 0]
    ],

    [
        [-1, -3, 0],
        [-2, -3, 5],
        [-2, 3, 5],
        [-1, 3, 0]
    ],

    [
        [1, -3, 0],
        [2, -3, 5],
        [2, 3, 5],
        [1, 3, 0]
    ],

    [
        [2, -2, 0],
        [3, -1, 0],
        [3, 1, 0],
        [2, 2, 0]
    ],
]

ctrlpoints_2 = [
    [
        [2, -2, 0],
        [3, -1, 0],
        [3, 1, 0],
        [2, 2, 0]
    ],
    [
        [1, -3, 0],
        [2, -3, -5],
        [2, 3, -5],
        [1, 3, 0]
    ],
    [
        [-1, -3, 0],
        [-2, -3, -5],
        [-2, 3, -5],
        [-1, 3, 0]
    ],
    [
        [-2, -2, 0],
        [-3, -1, 0],
        [-3, 1, 0],
        [-2, 2, 0]
    ],
]


def display():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_AUTO_NORMAL)

    glColor(1, 0, 0, 0)
    glMap2f(GL_MAP2_VERTEX_3, 0, 1, 0, 1, ctrlpoints_1)
    glEnable(GL_MAP2_VERTEX_3)
    glMapGrid2f(20, 0.0, 1.0, 20, 0.0, 1.0)
    glEvalMesh2(GL_FILL, 0, 20, 0, 20)

    glMap2f(GL_MAP2_VERTEX_3, 0, 1, 0, 1, ctrlpoints_2)
    glEnable(GL_MAP2_VERTEX_3)
    glMapGrid2f(20, 0.0, 1.0, 20, 0.0, 1.0)
    glEvalMesh2(GL_FILL, 0, 20, 0, 20)

    glFlush()


def init():
    pass


def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-5.0 * w / h, 5.0 * w / h, -5.0, 5.0, -5.0, 5.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glRotatef(180.0, 1.0, 1.0, 1.0)


if __name__ == '__main__':
    glutInit(sys.argv)
    glutCreateWindow(b'lab6_2')
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()