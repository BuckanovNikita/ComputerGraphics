from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

m_x = -0.5
m_y = 0.0
m_z = 3.0

angle_x = 0
angle_y = 0
angle_z = 0


def scene():
    glPushMatrix()
    glTranslatef(2.5, 0.0, 0.0)
    glColor3f(1.0, 0.0, 0.0)
    glutSolidCube(1.0)
    glPopMatrix()


def mirror(type_):
    glLineWidth(10)
    glBegin(type_)
    glVertex3f(m_x, m_y - 1, m_z - 2.0)
    glVertex3f(m_x, m_y - 1, m_z + 2.0)
    glVertex3f(m_x, m_y + 1, m_z + 2.0)
    glVertex3f(m_x, m_y + 1, m_z - 2.0)
    glEnd()


def display():
    glClearColor(1, 1, 1, 0.0)
    glEnable(GL_STENCIL_TEST)
    glEnable(GL_DEPTH_TEST)

    glClearStencil(0)
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glTranslatef(0.0, 0.0, -9.0)
    glRotatef(angle_x, 1.0, 0.0, 0.0)
    glRotatef(angle_y, 0.0, 1.0, 0.0)
    glRotatef(angle_z, 0.0, 0.0, 1.0)

    glClear(GL_STENCIL_BUFFER_BIT)
    glStencilFunc(GL_ALWAYS, 1, 1)
    glStencilOp(GL_REPLACE, GL_REPLACE, GL_REPLACE)
    mirror(GL_QUADS)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glColor3f(0.7, 0.7, 0.7)
    mirror(GL_LINE_LOOP)

    glStencilOp(GL_KEEP, GL_KEEP, GL_KEEP)
    glStencilFunc(GL_NOTEQUAL, 1, 1)
    scene()

    glStencilFunc(GL_EQUAL, 1, 1)
    glTranslatef(m_x, m_y, m_z)
    glScalef(-1.0, 1.0, 1.0)
    glTranslatef(-m_x, -m_y, -m_z)
    scene()

    glutSwapBuffers()


def keyboard(key, x, y):
    global angle_x
    global angle_y
    global angle_z

    if key == b'z':
        angle_x = (angle_x + 3) % 360

    if key == b'a':
        angle_x = (angle_x - 3) % 360

    if key == b'x':
        angle_y = (angle_y + 3) % 360

    if key == b's':
        angle_y = (angle_y - 3) % 360

    if key == b'c':
        angle_z = (angle_z + 3) % 360

    if key == b'd':
        angle_z = (angle_z - 3) % 360

    if key == b'r':
        angle_x = 0
        angle_y = 0
        angle_z = 0

    if key == b'q':
        exit(0)

    glutPostRedisplay()


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
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_STENCIL | GLUT_DEPTH)
    glutCreateWindow(b'lab 5_1')
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutReshapeFunc(reshape)
    glutMainLoop()
