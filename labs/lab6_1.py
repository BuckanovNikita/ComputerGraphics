from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

c = 0.55191502449

ctrlpoints_1 = [
    [-1, 0, 0],
    [-1, c, 0],
    [-c, 1, 0],
    [0, 1, 0],

    [0, 1, 0],
    [c, 1, 0],
    [1, c, 0],
    [1, 0, 0]]

ctrlpoints_2 = [
    [1, 0, 0],
    [1, -c, 0],
    [c, -1, 0],
    [0, -1, 0],

    [0, -1, 0],
    [-c, -1, 0],
    [-1, -c, 0],
    [-1, 0, 0]]


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glShadeModel(GL_FLAT)


def display():
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glMap1f(GL_MAP1_VERTEX_3, 0.0, 1.0, ctrlpoints_1)
    glEnable(GL_MAP1_VERTEX_3)
    glColor(0, 0, 0, 0)
    glBegin(GL_LINE_STRIP)
    glColor(0, 0, 0, 0)
    for i in range(30):
        glEvalCoord1f(i / 30.0)
    glEnd()

    glMap1f(GL_MAP1_VERTEX_3, 0.0, 1.0, ctrlpoints_2)
    glEnable(GL_MAP1_VERTEX_3)
    glColor(0, 0, 0, 0)
    glBegin(GL_LINE_STRIP)

    for i in range(30):
        glEvalCoord1f(i / 30.0)
    glEnd()

    glPointSize(5.0)
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_POINTS)
    for i in range(8):
        glVertex3fv(ctrlpoints_1[i])
    for i in range(8):
        glVertex3fv(ctrlpoints_2[i])
    glEnd()
    glFlush()


def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, w / h, 1.0, 30.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -5.0)


if __name__ == '__main__':
    glutInit(sys.argv)
    glutCreateWindow(b'lab6_1')
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()
