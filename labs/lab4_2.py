from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
from numpy import sin, cos, pi
from lab4 import read_texture
from lab3 import mouse

mat_emission = GLfloat_3(0.5, 0.5, 0.5)


def scene_3(n=100, m=100, r=2):
    glEnable(GL_TEXTURE_2D)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    read_texture('tex/brick.bmp')
    for j in range(n):
        phi1 = j * (2 * pi) / n
        phi2 = (j + 1) * (2 * pi) / n
        glBegin(GL_QUAD_STRIP)
        for i in range(m + 1):
            theta = i * pi / n
            ex = sin(theta) * cos(phi2)
            ey = sin(theta) * sin(phi2)
            ez = cos(theta)
            s = phi2 / (2 * pi)
            t = 1 - theta / pi
            glTexCoord2f(4*s, 4*t)
            glVertex3f(r*ex, r*ey, r*ez)
            ex = sin(theta) * cos(phi1)
            ey = sin(theta) * sin(phi1)
            ez = cos(theta)
            s = phi1 / (2 * pi)
            t = 1 - theta / pi
            glTexCoord2f(4*s, 4*t)
            glVertex3f(r * ex, r * ey, r * ez)
        glEnd()
    glDisable(GL_TEXTURE_2D)
    glFlush()
    glutSwapBuffers()


def reshape(w, h):
    glViewport(0, 0, GLsizei(w), GLsizei(h))
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(120.0, 16.0 / 9.0, 1.0, 10.0)
    glMatrixMode(GL_MODELVIEW)


def display():
    pass


LOOK_AT = np.array([0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 1, 0.0])


def keyboard(key, _, __):
    print(key)
    if key == b'w':
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        LOOK_AT[2] -= 0.1
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(120, 16 / 9, 0.5, 25)
        gluLookAt(*LOOK_AT)
        glMatrixMode(GL_MODELVIEW)
        glutPostRedisplay()

    if key == b's':
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        LOOK_AT[2] += 0.1
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(120, 16 / 9, 0.5, 25)
        gluLookAt(*LOOK_AT)
        glMatrixMode(GL_MODELVIEW)
        glutPostRedisplay()

    if key == b'd':
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        LOOK_AT[0] += 0.1
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(120, 16 / 9, 0.5, 25)
        gluLookAt(*LOOK_AT)
        glMatrixMode(GL_MODELVIEW)
        glutPostRedisplay()

    if key == b'a':
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        LOOK_AT[0] -= 0.1
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(120, 16 / 9, 0.5, 25)
        gluLookAt(*LOOK_AT)
        glMatrixMode(GL_MODELVIEW)
        glutPostRedisplay()


if __name__ == '__main__':
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_DOUBLE |  GLUT_RGB)
    glutInitWindowSize(800, 450)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"lab4")

    glClearColor(0.0, 0.0, 0.0, 0.0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glMaterialfv(GL_FRONT, GL_EMISSION, mat_emission)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(120.0, 16.0 / 9.0, 1.0, 10.0)
    glMatrixMode(GL_MODELVIEW)
    glutDisplayFunc(scene_3)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutPassiveMotionFunc(mouse)
    glutMainLoop()
