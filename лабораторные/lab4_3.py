from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
from PIL import Image

angle_x = 0
angle_y = 0
angle_z = 0


def init():
    glClearColor(0.9, 0.9, 0.8, 0.0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_AUTO_NORMAL)
    light_ambient = [0.1, 0.1, 0.1, 1.0]
    light_diffuse = [0.9, 0.8, 0.9, 1.0]
    light_position = [1.0, 1.0, 1.0, 0.0]

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_LIGHT0)
    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glEnable(GL_TEXTURE_GEN_S)
    glEnable(GL_TEXTURE_GEN_T)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glEnable(GL_TEXTURE_2D)


def rotate():
    glRotatef(angle_x, 1.0, 0.0, 0.0)
    glRotatef(angle_y, 0.0, 1.0, 0.0)
    glRotatef(angle_z, 0.0, 0.0, 1.0)


def draw_scene():
    glDisable(GL_LIGHTING)
    glPushMatrix()
    glTranslatef(2, 0.5, 0.5)
    glRotatef(45, 1, 1, 1)

    image = Image.open('tex/brick.bmp')
    image_data = np.array(list(image.getdata()), np.uint8)

    glGenTextures(2)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 4)
    glBindTexture(GL_TEXTURE_2D, 2)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.size[0], image.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, image_data)
    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_OBJECT_LINEAR)
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_OBJECT_LINEAR)
    glEnable(GL_TEXTURE_GEN_S)
    glEnable(GL_TEXTURE_GEN_T)
    image.close()

    glutSolidCube(0.2)
    glPopMatrix()

    glBindTexture(GL_TEXTURE_2D, 1)
    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glEnable(GL_TEXTURE_GEN_S)
    glEnable(GL_TEXTURE_GEN_T)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glEnable(GL_LIGHTING)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0, 0, 0, 5, 0, 0, 0, 0, 1)
    glScalef(1, -1, 1)
    rotate()
    draw_scene()
    glCopyTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, 0, 0, 500, 500, 0)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(5, 0, 0, 0, 0, 0, 0, 0, 1)
    rotate()
    draw_scene()
    glutSolidSphere(1.0, 20, 20)
    glFlush()
    glutSwapBuffers()


def keyboard(key, _, __):
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

    if key == b'27':
        exit(0)
    glutPostRedisplay()


def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, float(w / h), 1.0, 30.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -5.0)


if __name__ == '__main__':
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b'lab4_3')
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMainLoop()
