from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np
from PIL import Image

mat_emission = GLfloat_3(0.5, 0.5, 0.5)


def read_texture(filename):
    try:
        image = Image.open(filename)
    except IOError as ex:
        return
    image_data = np.array(list(image.getdata()), np.uint8)

    texture_id = glGenTextures(1)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 4)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.size[0], image.size[1],
                 0, GL_RGB, GL_UNSIGNED_BYTE, image_data)
    image.close()
    return texture_id


def scene_3():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    x = read_texture('tex/texture.jpg')
    glEnable(GL_TEXTURE_2D)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-0.5, -0.5, 0.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-0.5, 0.5, 0.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(0.5, 0.5, 0.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(0.5, -0.5, 0.0)
    glEnd()
    glDisable(GL_TEXTURE_2D)
    glFlush()
    glutSwapBuffers()


def reshape(w, h):
    glViewport(0, 0, GLsizei(w), GLsizei(h))
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)


def display():
    pass


def keyboard(key, _, __):
    pass


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
    glFrustum(-4, 4, -4, 4, 0.1, 100)
    glMatrixMode(GL_MODELVIEW)
    glutDisplayFunc(scene_3)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMainLoop()
