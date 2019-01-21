from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np


LOOK_AT = np.array([1, 1, 10.0, 0.0, 0.0, 0.0, 0.0, 1, 0.0])
A = 1
B = 2
D = 5


def draw_table():
    glPushMatrix()
    glTranslate(0, -0.1, 0)
    glScalef(1, 0.1, 1)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslate(-0.45, -0.55, -0.45)
    glScalef(0.1, 1, 0.1)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.45, -0.55, -0.45)
    glScalef(0.1, 1, 0.1)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.45, -0.55, 0.45)
    glScalef(0.1, 1, 0.1)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslate(-0.45, -0.55, 0.45)
    glScalef(0.1, 1, 0.1)
    glutSolidCube(1)
    glPopMatrix()

    glFlush()


def draw_teapot():
    glPushMatrix()
    glutSolidTeapot(0.1)
    glPopMatrix()


def draw_pen():
    glPushMatrix()
    glTranslate(0, -0.02, 0)
    glutSolidCylinder(0.02, 0.1, 200, 200)
    glPopMatrix()


def draw_book():
    glPushMatrix()
    glScale(0.3, 0.1, 0.2)
    glutSolidCube(1)
    glPopMatrix()


def scene_1():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor(1, 1, 1)
    glLoadIdentity()
    draw_table()

    glPushMatrix()
    glColor(1, 0, 0)
    glTranslate(0.4, 0, 0.2)
    draw_teapot()
    glPopMatrix()

    glPushMatrix()
    glColor(0, 1, 0)
    glTranslate(-0.4, 0, -0.2)
    draw_book()
    glPopMatrix()

    glPushMatrix()
    glColor(0, 0, 1)
    draw_pen()
    glPopMatrix()

    glFlush()

def scene_2():
    np.random.seed(100)
    for i in range(3):
        for j in range(4):
            glPushMatrix()
            glTranslate(2*i, 0, 2*j)
            draw_table()

            glPushMatrix()
            glColor(1, 0, 0)
            r = np.random.rand(3)-0.5
            r[1] = 0
            glTranslate(*r)
            draw_book()
            glColor(1, 1, 1)
            glPopMatrix()

            glPushMatrix()
            glColor(0, 1, 0)
            r = np.random.rand(3) - 0.5
            r[1] = 0
            glTranslate(*r)
            draw_pen()
            glColor(1, 1, 1)
            glPopMatrix()

            glPushMatrix()
            glColor(0, 0, 1)
            r = np.random.rand(3) - 0.5
            r[1] = 0
            glTranslate(*r)
            draw_teapot()
            glColor(1, 1, 1)
            glPopMatrix()

            glPopMatrix()
    glFlush()


def scene_3():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    scene_2()

    phi = np.arctan2(B, A)

    glPushMatrix()
    glLoadIdentity()
    glTranslate(-D / A, 0, 0)
    glRotate(-phi*180/np.pi, 0, 1, 0)
    glScalef(0.1, 1, 40)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslate(0, 0, -2.5)
    glColor(1, 0, 0)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslate(-5, 0, 0)
    glColor(1, 0, 0)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glLoadIdentity()
    glColor(1, 1, 1)

    glTranslate(-D/A, 0, 0)

    glRotate(-phi*180/np.pi, 0, 1, 0)

    glScale(-1, 1, 1)

    glRotate(phi * 180 / np.pi, 0, 1, 0)

    glTranslate(D/A, 0, 0)

    scene_2()
    glPopMatrix()
    glFlush()
    glutSwapBuffers()


def display():
    pass


def reshape(w, h):
    glViewport(0, 0, GLsizei(w), GLsizei(h))
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glShadeModel(GL_FLAT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-2.0, 2.0, -2.0, 2.0, 0.5, 5)
    gluLookAt(1, 1, 3.0, 0.0, 0.0, 0.0, 0.0, 1, 0.0)
    glMatrixMode(GL_MODELVIEW)


def keyboard(key, _, __):
    print(key)
    if key == b'4':
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glFrustum(-1.0, 1.0, -1.0, 1.0, 0.5, 10)
        gluLookAt(*LOOK_AT)
        glMatrixMode(GL_MODELVIEW)
        glutPostRedisplay()

    if key == b'5':
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-1.0, 1.0, -1.0, 1.0, 0.5, 10)
        gluLookAt(*LOOK_AT)
        glMatrixMode(GL_MODELVIEW)
        glutPostRedisplay()

    if key == b'6':
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(120, 16 / 9, 0.5, 25)
        gluLookAt(*LOOK_AT)
        glMatrixMode(GL_MODELVIEW)
        glutPostRedisplay()

    if key == b'w':
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        LOOK_AT[2] -= 1
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(120, 16 / 9, 0.5, 25)
        gluLookAt(*LOOK_AT)
        glMatrixMode(GL_MODELVIEW)
        glutPostRedisplay()

    if key == b's':
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        LOOK_AT[2] += 1
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(120, 16 / 9, 0.5, 25)
        gluLookAt(*LOOK_AT)
        glMatrixMode(GL_MODELVIEW)
        glutPostRedisplay()

    if key == b'd':
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        LOOK_AT[0] += 1
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(120, 16 / 9, 0.5, 25)
        gluLookAt(*LOOK_AT)
        glMatrixMode(GL_MODELVIEW)
        glutPostRedisplay()

    if key == b'a':
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        LOOK_AT[0] -= 1
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(120, 16 / 9, 0.5, 25)
        gluLookAt(*LOOK_AT)
        glMatrixMode(GL_MODELVIEW)
        glutPostRedisplay()

    if key == b'1':
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glutDisplayFunc(scene_1)
        glutPostRedisplay()

    if key == b'2':
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glutDisplayFunc(scene_2)
        glutPostRedisplay()

    if key == b'3':
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glutDisplayFunc(scene_3)
        glutPostRedisplay()


if __name__ == '__main__':
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_DOUBLE |  GLUT_RGB)
    glutInitWindowSize(800, 450)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Cube")

    glClearColor(0.0, 0.0, 0.0, 0.0)
    glShadeModel(GL_FLAT)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(120, 16/9, 0.5, 25)
    gluLookAt(*LOOK_AT)
    glMatrixMode(GL_MODELVIEW)
    glutDisplayFunc(scene_3)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMainLoop()
