from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np


class ShadowObj:
    vertex = np.array([-14, -11, -350, 15, 0, -345, 0, 10, -355])
    normal = np.array([1, 1, 1])
    n = 0


shadow = ShadowObj()
light_pos = [0, 100, -340, 1]
sphere_mat = [1, 1, 1, 1]
obj_mat = [1, 1, 1, 1]


def extend(light, vertex, t):
    return light[:3] + (vertex - light[:3])*t


def make_shadow(obj, light, t, list_ind):

    glNewList(list_ind, GL_COMPILE)
    glDisable(GL_LIGHTING)
    glBegin(GL_QUADS)
    for i in range(obj.n):
        glVertex3fv(obj.vertex[i * 3:(i + 1) * 3])
        glVertex3fv(extend(light, obj.vertex[i * 3: (i + 1) * 3], t))
        glVertex3fv(extend(light, obj.vertex[((i + 1) % obj.n) * 3:((i + 1) % obj.n) * 3 + 3], t))
        glVertex3fv(obj.vertex[((i + 1) % obj.n) * 3: ((i + 1) % obj.n) * 3 + 3])
    glEnd()
    glEnable(GL_LIGHTING)
    glEndList()


def torus():
    global sphere_mat
    glPushMatrix()
    glTranslatef(0, -80, -360)
    glRotate(45, 0, 1, 0)
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, sphere_mat)
    glutSolidTorus(10, 20, 200, 200)
    glPopMatrix()


def render(obj):
    global obj_mat
    torus()
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, obj_mat)
    glBegin(GL_POLYGON)
    glNormal3fv(obj.normal)

    for i in range(obj.n):
        glVertex3fv(obj.vertex[3*i:3*(i+1)])
    glEnd()


def redraw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT | GL_STENCIL_BUFFER_BIT)
    glColorMask(GL_FALSE, GL_FALSE, GL_FALSE, GL_FALSE)
    render(shadow)

    glEnable(GL_STENCIL_TEST)
    glDepthMask(GL_FALSE)
    glStencilFunc(GL_ALWAYS, 0, 0)

    glStencilOp(GL_KEEP, GL_KEEP, GL_INCR)
    glCullFace(GL_BACK)
    glCallList(1)

    glStencilOp(GL_KEEP, GL_KEEP, GL_DECR)
    glCullFace(GL_FRONT)
    glCallList(1)

    glDepthMask(GL_TRUE)
    glColorMask(GL_TRUE, GL_TRUE, GL_TRUE, GL_TRUE)
    glCullFace(GL_BACK)
    glDepthFunc(GL_LEQUAL)
    glStencilOp(GL_KEEP, GL_KEEP, GL_KEEP)

    glStencilFunc(GL_EQUAL, 1, 1)
    glDisable(GL_LIGHT0)
    render(shadow)

    glStencilFunc(GL_EQUAL, 0, 1)
    glEnable(GL_LIGHT0)
    render(shadow)

    glDepthFunc(GL_LESS)
    glDisable(GL_STENCIL_TEST)

    glutSwapBuffers()


def keyboard(key, _, __):
    if key == b'q':
        exit(0)


if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH | GLUT_STENCIL | GLUT_DOUBLE)
    glutCreateWindow(b'lab5_2')
    glutDisplayFunc(redraw)
    glutKeyboardFunc(keyboard)

    glMatrixMode(GL_PROJECTION)
    glFrustum(-100, 100, -100, 100, 320, 640)
    glMatrixMode(GL_MODELVIEW)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_CULL_FACE)

    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)

    shadow.n = len(shadow.vertex)//3

    make_shadow(shadow, light_pos, 10, 1)

    glutMainLoop()
