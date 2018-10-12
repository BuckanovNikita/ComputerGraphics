#include <GL/glut.h>
#include <iostream>
GLdouble n[6][3] = {
        {-1.0, 0.0, 0.0}, {0.0, 1.0, 0.0}, {1.0, 0.0, 0.0},
        {0.0, -1.0, 0.0}, {0.0, 0.0, 1.0}, {0.0, 0.0, -1.0} };

GLint faces[6][4] = {
        {0, 1, 2, 3}, {3, 2, 6, 7}, {7, 6, 5, 4},
        {4, 5, 1, 0}, {5, 6, 2, 1}, {7, 4, 0, 3} };

GLdouble v[8][3];

GLfloat light_position[] = {0.0,1.0,-5.0, 0.0};

GLfloat SpecularLight[] = {0.6f, 0.0f, 0.4f};
GLfloat DiffLight[] = {0.6f, 0.0f, 0.4f};
GLfloat matSpec[] = {0.2f, 0.6f, 0.6f};
GLfloat matDiff[] = {0.2f, 0.6f, 0.6f};
GLfloat matZero[] = {0,0,0};
void drawBox(void)
{
    for (int i = 0; i < 6; i++) {
        glBegin(GL_QUADS);
        glNormal3dv(&n[i][0]);
        glVertex3dv(&v[faces[i][0]][0]);
        glNormal3dv(&n[i][0]);
        glVertex3dv(&v[faces[i][1]][0]);
        glNormal3dv(&n[i][0]);
        glVertex3dv(&v[faces[i][2]][0]);
        glNormal3dv(&n[i][0]);
        glVertex3dv(&v[faces[i][3]][0]);
        glEnd();
    }

    glBegin(GL_QUADS);
    glNormal3d(-0.5, -0.5, -0.5);
    glVertex3d(3.0, 0.0, 0.0);

    glNormal3d(0.5, -0.5, -0.5);
    glVertex3d(4.0, 0.0, 0.0);

    glNormal3d(0.5, -0.5, -0.5);
    glVertex3d(4.0, 0.0, 0.0);

    glNormal3d(0.5, 0.5, -0.5);
    glVertex3d(4.0, 1.0, 0.0);

    glNormal3d(-0.5, 0.5, -0.5);
    glVertex3d(3.0, 1.0, 0.0);
    glEnd();

    glBegin(GL_QUADS);
    glNormal3d(-0.5, -0.5, -0.5);
    glVertex3d(3.0, 0.0, 0.0);

    glNormal3d(-0.5, 0.5, -0.5);
    glVertex3d(3.0, 1.0, 0.0);

    glNormal3d(-0.5, 0.5, 0.5);
    glVertex3d(3.0, 1.0, 1.0);

    glNormal3d(-0.5, -0.5, 0.5);
    glVertex3d(3.0, 0.0, 1.0);
    glEnd();

    glBegin(GL_QUADS);
    glNormal3d(-0.5, -0.5, 0.5);
    glVertex3d(3.0, 0.0, 1.0);

    glNormal3d(-0.5, 0.5, 0.5);
    glVertex3d(3.0, 1.0, 1.0);

    glNormal3d(0.5, 0.5, 0.5);
    glVertex3d(4.0, 1.0, 1.0);

    glNormal3d(0.5, -0.5, 0.5);
    glVertex3d(4.0, 0.0, 1.0);
    glEnd();

    glBegin(GL_QUADS);

    glNormal3d(0.5, -0.5, 0.5);
    glVertex3d(4.0, 0.0, 1.0);

    glNormal3d(0.5, 0.5, 0.5);
    glVertex3d(4.0, 1.0, 1.0);

    glNormal3d(0.5, 0.5, -0.5);
    glVertex3d(4.0, 1.0, 0.0);

    glNormal3d(0.5, -0.5, -0.5);
    glVertex3d(4.0, 0.0, 0.0);

    glEnd();

    glBegin(GL_QUADS);

    glNormal3d(-0.5, -0.5, -0.5);
    glVertex3d(3.0, 0.0, 0.0);

    glNormal3d(0.5, -0.5, -0.5);
    glVertex3d(4.0, 0.0, 0.0);

    glNormal3d(0.5, -0.5, 0.5);
    glVertex3d(4.0, 0.0, 1.0);

    glNormal3d(-0.5, -0.5, 0.5);
    glVertex3d(3.0, 0.0, 1.0);

    glEnd();

    glBegin(GL_QUADS);

    glNormal3d(-0.5, 0.5, -0.5);
    glVertex3d(3.0, 1.0, 0.0);

    glNormal3d(0.5, 0.5, -0.5);
    glVertex3d(4.0, 1.0, 0.0);

    glNormal3d(0.5, 0.5, 0.5);
    glVertex3d(4.0, 1.0, 1.0);

    glNormal3d(-0.5, 0.5, 0.5);
    glVertex3d(4.0, 0.0, 1.0);

    glEnd();
}
void key(unsigned char key, int x, int y) {
    if (key == '1') {
        glDisable(GL_LIGHT1);
        glLightfv(GL_LIGHT0, GL_POSITION, light_position);
        glLightfv(GL_LIGHT0, GL_SPECULAR, SpecularLight);
        glMaterialfv(GL_FRONT, GL_DIFFUSE, matZero);
        glMaterialfv(GL_FRONT, GL_SPECULAR, matSpec);
        glEnable(GL_LIGHT0);
        glutPostRedisplay();
    }
    if (key == '2') {
        glDisable(GL_LIGHT0);
        glLightfv(GL_LIGHT1, GL_POSITION, light_position);
        glLightfv(GL_LIGHT1, GL_DIFFUSE, DiffLight);
        glEnable(GL_LIGHT1);

        glMaterialfv(GL_FRONT, GL_DIFFUSE, matZero);
        glMaterialfv(GL_FRONT, GL_SPECULAR, matSpec);
        glutPostRedisplay();
    }

    if (key == '3') {
        glDisable(GL_LIGHT1);
        glLightfv(GL_LIGHT0, GL_POSITION, light_position);
        glLightfv(GL_LIGHT0, GL_SPECULAR, SpecularLight);
        glLightfv(GL_LIGHT0, GL_DIFFUSE, matZero);
        glEnable(GL_LIGHT0);
        GLfloat matZero1[] = {0,0,0};
        glMaterialfv(GL_FRONT, GL_SPECULAR, matZero1);
        glMaterialfv(GL_FRONT, GL_DIFFUSE, matDiff);
        glutPostRedisplay();
    }

    if (key == '4') {
        glDisable(GL_LIGHT0);
        glLightfv(GL_LIGHT1, GL_POSITION, light_position);
        glLightfv(GL_LIGHT1, GL_DIFFUSE, DiffLight);
        glLightfv(GL_LIGHT1, GL_SPECULAR, matZero);
        glEnable(GL_LIGHT1);
        glMaterialfv(GL_FRONT, GL_SPECULAR, matZero);
        glMaterialfv(GL_FRONT, GL_DIFFUSE, matDiff);
        glutPostRedisplay();
    }
    if(key == '5')
    {
        glEnable(GL_LIGHT_MODEL_AMBIENT);
        glutPostRedisplay();
    }else{
        glEnable(GL_LIGHT_MODEL_AMBIENT);
        glutPostRedisplay();
    }

    if(key =='6')
    {
        GLfloat matEmission[] = {0.1,0,0};
        glMaterialfv(GL_FRONT, GL_EMISSION, matEmission);
        glutPostRedisplay();
    }
    else
    {
        glMaterialfv(GL_FRONT, GL_EMISSION, matZero);
        glutPostRedisplay();
    }
    if(key == '7')
    {
        glShadeModel(GL_FLAT);
        glutPostRedisplay();
    } else
    {
        glShadeModel(GL_SMOOTH);
        glutPostRedisplay();
    }
}


void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    drawBox();
    glutSwapBuffers();
}

void init(void)
{
    v[0][0] = v[1][0] = v[2][0] = v[3][0] = -1;
    v[4][0] = v[5][0] = v[6][0] = v[7][0] = 1;
    v[0][1] = v[1][1] = v[4][1] = v[5][1] = -1;
    v[2][1] = v[3][1] = v[6][1] = v[7][1] = 1;
    v[0][2] = v[3][2] = v[4][2] = v[7][2] = 1;
    v[1][2] = v[2][2] = v[5][2] = v[6][2] = -1;

    glEnable(GL_LIGHT0);
    glEnable(GL_LIGHTING);
    glEnable(GL_DEPTH_TEST);

    glMatrixMode(GL_PROJECTION);
    gluPerspective(90.0, 16.0/9.0, 1.0, 10.0);
    glMatrixMode(GL_MODELVIEW);
    gluLookAt(0.0, 0.0, 5.0,  /* eye is at (0,0,5) */
              0.0, 0.0, 0.0,      /* center is at (0,0,0) */
              0.0, 1.0, 0.);      /* up is in positive Y direction */

    /* Adjust cube position to be asthetic angle. */
    glTranslated(0.0, 0.0, -1.0);
    glRotated(60, 1.0, 0.0, 0.0);
    glRotated(-20, 0.0, 0.0, 1.0);
}

int main(int argc, char **argv)
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutCreateWindow("lab2");
    glEnable(GL_NORMALIZE);
    glutDisplayFunc(display);
    glutKeyboardFunc(key);
    init();
    glutMainLoop();
    return 0;
}