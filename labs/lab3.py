from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np


LOOK_AT = np.array([2, 2, 0.0, 0.0, 0.0, 0.0, 0.0, 1, 0.0])

n = [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [-1.0, 0.0, 0.0],
     [0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [0.0, 0.0, -1.0]]

v = np.zeros((8, 3))
v[0][0] = v[1][0] = v[2][0] = v[3][0] = -1
v[4][0] = v[5][0] = v[6][0] = v[7][0] = 1
v[0][1] = v[1][1] = v[4][1] = v[5][1] = -1
v[2][1] = v[3][1] = v[6][1] = v[7][1] = 1
v[0][2] = v[3][2] = v[4][2] = v[7][2] = 1
v[1][2] = v[2][2] = v[5][2] = v[6][2] = -1

faces = [[0, 1, 2, 3], [3, 2, 6, 7], [7, 6, 5, 4],
         [4, 5, 1, 0], [5, 6, 2, 1], [7, 4, 0, 3]]

light_position = GLdouble_4(5.0, -5.0, 0.0, 0.0)

SpecularLight = GLdouble_3(0.6, 0.0, 0.4)
DiffLight = GLdouble_3(1, 1, 1)
matSpec = GLdouble_3(0.2, 0.6, 0.6)
matDiff = GLdouble_3(0.2, 0.6, 0.6)
matZero = GLdouble_3(0, 0, 0)


def draw_cube():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBegin(GL_QUADS)
    glNormal3d(0, -1, 0)
    glVertex3d(0, 1, 0)
    glVertex3d(1.0, 1.0, 0.0)
    glVertex3d(1.0, 1.0, 1.0)
    glVertex3d(0.0, 1.0, 1.0)
    glEnd()

    glBegin(GL_QUADS)
    glNormal3d(0, 1, 0)
    glVertex3d(0, 0, 0)
    glVertex3d(1.0, 0.0, 0.0)
    glVertex3d(1.0, 0.0, 1.0)
    glVertex3d(0.0, 0.0, 1.0)
    glEnd()

    glBegin(GL_QUADS)
    glNormal3d(1, 0, 0)
    glVertex3d(0, 0, 0)
    glVertex3d(0.0, 1.0, 0.0)
    glVertex3d(0.0, 1.0, 1.0)
    glVertex3d(0.0, 0.0, 1.0)
    glEnd()

    glBegin(GL_QUADS)
    glNormal3d(-1, 0, 0)
    glVertex3d(1, 0, 0)
    glVertex3d(1.0, 1.0, 0.0)
    glVertex3d(1.0, 1.0, 1.0)
    glVertex3d(1.0, 0.0, 1.0)
    glEnd()

    glBegin(GL_QUADS)
    glNormal3d(0, -1, 0)
    glVertex3d(0, 0, 0)
    glVertex3d(1.0, 0.0, 0.0)
    glVertex3d(1.0, 1.0, 0.0)
    glVertex3d(0.0, 1.0, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glNormal3d(0, 0, -1)
    glVertex3d(0, 0, 1)
    glVertex3d(1.0, 0.0, 1.0)
    glVertex3d(1.0, 1.0, 1.0)
    glVertex3d(0.0, 1.0, 1.0)
    glEnd()

    #cube2
    glPushMatrix()
    glTranslate(0.5, 0.5, 0.5)
    glutWireCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.5, 0.5, 2.5)
    glutWireCube(1)
    glPopMatrix()

    y = np.array([0, 0, 2])
    glBegin(GL_QUADS)
    center = y + np.array([0.5, 0.5, 0.5])
    v1 = np.array([0, 0, 0])
    glNormal3d(*(-abs(center - (v1+y))))
    glVertex3d(*(v1+y))
    v1 = np.array([1, 0, 0])
    glNormal3d(*(-abs(center - (v1+y))))
    glVertex3d(*(v1+y))
    v1 = np.array([1, 0, 1])
    glNormal3d(*(-abs(center - (v1+y))))
    glVertex3d(*(v1+y))
    v1 = np.array([0.0, 0.0, 1.0])
    glNormal3d(*(-abs(center - (v1+y))))
    glVertex3d(*(v1+y))
    glEnd()

    y = np.array([0, 0, 2])
    glBegin(GL_QUADS)
    center = y + np.array([0.5, 0.5, 0.5])
    v1 = np.array([0, 1, 0])
    glNormal3d(*(-abs(center - (v1 + y))))
    glVertex3d(*(v1+y))
    v1 = np.array([1, 1, 0])
    glNormal3d(*(-abs(center - (v1 + y))))
    glVertex3d(*(v1+y))
    v1 = np.array([1, 1, 1])
    glNormal3d(*(-abs(center - (v1 + y))))
    glVertex3d(*(v1+y))
    v1 = np.array([0.0, 1.0, 1.0])
    glNormal3d(*(-abs(center - (v1 + y))))
    glVertex3d(*(v1+y))
    glEnd()

    y = np.array([0, 0, 2])
    glBegin(GL_QUADS)
    center = y + np.array([0.5, 0.5, 0.5])
    v1 = np.array([0, 0, 0])
    glNormal3d(*(-abs(center - (v1 + y))))
    glVertex3d(*(v1+y))
    v1 = np.array([0, 1, 0])
    glNormal3d(*(-abs(center - (v1 + y))))
    glVertex3d(*(v1+y))
    v1 = np.array([0, 1, 1])
    glNormal3d(*(-abs(center - (v1 + y))))
    glVertex3d(*(v1+y))
    v1 = np.array([0.0, 0.0, 1.0])
    glNormal3d(*(-abs(center - (v1 + y))))
    glVertex3d(*(v1+y))
    glEnd()

    y = np.array([0, 0, 2])
    glBegin(GL_QUADS)
    center = y + np.array([0.5, 0.5, 0.5])
    v1 = np.array([1, 0, 0])
    glNormal3d(*(-abs(center - (v1 + y))))
    glVertex3d(*(v1 + y))
    v1 = np.array([1, 1, 0])
    glNormal3d(*(-abs(center - (v1 + y))))
    glVertex3d(*(v1 + y))
    v1 = np.array([1, 1, 1])
    glNormal3d(*(-abs(center - (v1 + y))))
    glVertex3d(*(v1 + y))
    v1 = np.array([1.0, 0.0, 1.0])
    glNormal3d(*(-abs(center - (v1 + y))))
    glVertex3d(*(v1 + y))
    glEnd()

    y = np.array([0, 0, 2])
    glBegin(GL_QUADS)
    center = y + np.array([0.5, 0.5, 0.5])
    v1 = np.array([0, 0, 0])
    glNormal3d(*(-abs(center - (v1 + y))))
    glVertex3d(*(v1 + y))
    v1 = np.array([0, 1, 0])
    glNormal3d(*(-abs(center - (v1 + y))))
    glVertex3d(*(v1 + y))
    v1 = np.array([1, 1, 0])
    glNormal3d(*(-abs(center - (v1 + y))))
    glVertex3d(*(v1 + y))
    v1 = np.array([1.0, 0.0, 0.0])
    glNormal3d(*(-abs(center - (v1 + y))))
    glVertex3d(*(v1 + y))
    glEnd()

    y = np.array([0, 0, 2])
    glBegin(GL_QUADS)
    center = y + np.array([0.5, 0.5, 0.5])
    v1 = np.array([0, 0, 1])
    glNormal3d(*(-abs(center - (v1 + y))))
    glVertex3d(*(v1 + y))
    v1 = np.array([0, 1, 1])
    glNormal3d(*(-abs(center - (v1 + y))))
    glVertex3d(*(v1 + y))
    v1 = np.array([1, 1, 1])
    glNormal3d(*(-abs(center - (v1 + y))))
    glVertex3d(*(v1 + y))
    v1 = np.array([1.0, 0.0, 1.0])
    glNormal3d(*(-abs(center - (v1 + y))))
    glVertex3d(*(v1 + y))
    glEnd()


def special(key, x, y):
    print(key)
    if key == 101:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        LOOK_AT[1] += 1
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(120, 16 / 9, 0.5, 25)
        gluLookAt(*LOOK_AT)
        glMatrixMode(GL_MODELVIEW)
        glutPostRedisplay()

    if key == 103:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        LOOK_AT[1] -= 1
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(120, 16 / 9, 0.5, 25)
        gluLookAt(*LOOK_AT)
        glMatrixMode(GL_MODELVIEW)
        glutPostRedisplay()
    pass


lmodel_ambient_enabled = GLfloat_4( 1.0, 1.0, 1.0, 1.0)
lmodel_ambient_disabled = GLfloat_4( 0.0, 0.0, 0.0, 0.0 )
local_view = [1.0]


def keyboard(key, x, y):
    mat_emission = GLfloat_3(0.1, 0, 0)

    if key == b'1':
        glDisable(GL_LIGHT1)
        glLightfv(GL_LIGHT0, GL_POSITION, light_position)
        glLightfv(GL_LIGHT0, GL_SPECULAR, SpecularLight)
        glMaterialfv(GL_FRONT, GL_DIFFUSE, matZero)
        glMaterialfv(GL_FRONT, GL_SPECULAR, matSpec)
        glEnable(GL_LIGHT0)
        glutPostRedisplay()

    if key == b'2':
        glDisable(GL_LIGHT0)
        glLightfv(GL_LIGHT1, GL_POSITION, light_position)
        glLightfv(GL_LIGHT1, GL_DIFFUSE, DiffLight)
        glMaterialfv(GL_FRONT, GL_DIFFUSE, matZero)
        glMaterialfv(GL_FRONT, GL_SPECULAR, matSpec)
        glEnable(GL_LIGHT1)
        glutPostRedisplay()

    if key == b'3':
        glDisable(GL_LIGHT1)
        glLightfv(GL_LIGHT0, GL_POSITION, light_position)
        glLightfv(GL_LIGHT0, GL_SPECULAR, SpecularLight)
        glMaterialfv(GL_FRONT, GL_SPECULAR, matZero)
        glMaterialfv(GL_FRONT, GL_DIFFUSE, matDiff)
        glEnable(GL_LIGHT0)
        glutPostRedisplay()

    if key == b'4':
        glDisable(GL_LIGHT0)
        glLightfv(GL_LIGHT1, GL_POSITION, light_position)
        glLightfv(GL_LIGHT1, GL_DIFFUSE, DiffLight)
        glMaterialfv(GL_FRONT, GL_SPECULAR, matZero)
        glMaterialfv(GL_FRONT, GL_DIFFUSE, matDiff)
        glEnable(GL_LIGHT1)
        glutPostRedisplay()

    if key == b'6':
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, 1)
        glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER, GL_FALSE)
        glutPostRedisplay()

    if key == b'7':
        glLightModelfv(GL_LIGHT_MODEL_LOCAL_VIEWER, local_view)
        glutPostRedisplay()

    if key == b'9':
        glMaterialfv(GL_FRONT, GL_EMISSION, mat_emission)
        glutPostRedisplay()

    if key == b'0':
        glShadeModel(GL_FLAT)
        glutPostRedisplay()

    if key == b'q':
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMaterialfv(GL_FRONT, GL_EMISSION, matZero)
        glShadeModel(GL_SMOOTH)
        glutPostRedisplay()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_cube()
    glutSwapBuffers()


def init():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1, 1, 1])
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [1, 1, 1])
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(120.0, 16.0/9.0, 1.0, 10.0)
    gluLookAt(*LOOK_AT)
    glMatrixMode(GL_MODELVIEW)


if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 450)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"lab2")
    glEnable(GL_NORMALIZE)
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(special)

    glutMainLoop()
