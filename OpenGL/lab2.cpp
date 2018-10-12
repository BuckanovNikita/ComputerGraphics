// project.cpp: определяет точку входа для консольного приложения.
//
#include <time.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <glut/glut.h>

void draw_table() {
    glColor3f(1, 0, 0);
    glPushMatrix();
    glTranslatef(+2, 0, +1);
    glScalef(0.2, 2, 0.2);
    glutSolidCube(1);
    glPopMatrix();

    glPushMatrix();
    glTranslatef(+2, 0, -1);
    glScalef(0.2, 2, 0.2);
    glutSolidCube(1);
    glPopMatrix();

    glPushMatrix();
    glTranslatef(-2, 0, +1);
    glScalef(0.2, 2, 0.2);
    glutSolidCube(1);
    glPopMatrix();

    glPushMatrix();
    glTranslatef(-2, 0, -1);
    glScalef(0.2, 2, 0.2);
    glutSolidCube(1);
    glPopMatrix();

    glPushMatrix();
    glTranslatef(0, 1, 0);
    glScalef(5.0, 0.2, 2.5);
    glutSolidCube(1);
    glPopMatrix();
}

void draw_book() {
    glColor3f(1, 0, 0);
    glPushMatrix();
    glScalef(0.5, 0.1, 0.7);
    glutSolidCube(1);
    glPopMatrix();
}

void draw_pen() {
    glColor3f(1, 0, 0);
    glPushMatrix();
    glScalef(0.1, 0.1, 1.0);
    glutSolidSphere(0.2, 50, 50);
    glPopMatrix();
}

void draw_teapot() {
    glutSolidTeapot(0.25);
}

void draw_set() {

    draw_table();

    std::vector<double> x;
    std::vector<double> y;

    for (int i = -1; i < 1; ++i) y.push_back(0.25 + i + (rand() % 10) / 20.0);
    for (int i = -2; i < 2; ++i) x.push_back(0.25 + i + (rand() % 10) / 20.0);

    std::random_shuffle(x.begin(), x.end());
    std::random_shuffle(y.begin(), y.end());

    glPushMatrix();
    glTranslatef(x[0], 1.2, y[0]);
    glRotatef(rand() % 360, 0, 1, 0);
    draw_book();
    glPopMatrix();

    glPushMatrix();
    glTranslatef(x[1], 1.2, y[1]);
    glRotatef(rand() % 360, 0, 1, 0);
    draw_book();
    glPopMatrix();

    glPushMatrix();
    glTranslatef(x[2], 1.2, y[2]);
    glRotatef(rand() % 360, 0, 1, 0);
    draw_pen();
    glPopMatrix();


    glPushMatrix();
    glTranslatef(x[3], 1.325, y[3]);
    glRotatef(rand() % 360, 0, 1, 0);
    draw_teapot();
    glPopMatrix();

    //draw_pen();
    //draw_teapot();
}

void draw_class(time_t seed) {
    srand(seed);
    for (int i = -1; i < 2; i++) {
        for (int j = 0; j < 5; j++) {
            glPushMatrix();
            glTranslatef(8*i, 0, 5 + 4*j);
            draw_set();
            glPopMatrix();
        }
    }
}

void draw_wall() {
    glColor3f(1, 0, 0);
    glPushMatrix();
    glScalef(20, 2, 0.1);
    glutSolidCube(1);
    glPopMatrix();
}

double a = 3;

void key(unsigned char key, int x, int y) {
    GLfloat matEmission[] = { 0.1,0,0 };
    switch (key)
    {
        case '1':
            glLoadIdentity();
            gluLookAt(
                    0.0, 3.0, -3.0,
                    0.0, 0.0, 0.0,
                    0.0, 1.0, 0.0
            );

            glMatrixMode(GL_PROJECTION);
            glOrtho(-5, 5, -5, 5, 1.0, 20.0);
            glMatrixMode(GL_MODELVIEW);

            glutPostRedisplay();
            break;
        case '2':
            glLoadIdentity();
            gluLookAt(
                    0.0, 3.0, -3.0,
                    0.0, 0.0, 0.0,
                    0.0, 1.0, 0.0
            );

            glMatrixMode(GL_PROJECTION);
            gluPerspective(120.0, 16.0 / 9.0, 1.0, 20.0);
            glMatrixMode(GL_MODELVIEW);

            glutPostRedisplay();
            break;
        case '3':
            glLoadIdentity();
            gluLookAt(
                    0.0, 3.0, -3.0,
                    0.0, 0.0, 0.0,
                    0.0, 1.0, 0.0
            );

            glMatrixMode(GL_PROJECTION);
            glFrustum(-5, 5, -5, 5, 1.0, 20.0);
            glMatrixMode(GL_MODELVIEW);

            glutPostRedisplay();
            break;
        case '9':
            a = a + 1;
            glLoadIdentity();
            //gluPerspective(120.0, 16.0 / 9.0, 1.0, 20.0);
            gluLookAt(
                    0.0, a, -a,
                    0.0, 0.0, 0.0,
                    0.0, 1.0, 0.0
            );
            glRotated(90, 0.0, 1.0, 0.0);
            glutPostRedisplay();
            break;
        case '0':
            a = a - 1;
            glLoadIdentity();
            //gluPerspective(120.0, 16.0 / 9.0, 1.0, 20.0);
            gluLookAt(
                    0.0, a, -a,
                    0.0, 0.0, 0.0,
                    0.0, 1.0, 0.0
            );
            glRotated(90, 0.0, 1.0, 0.0);
            glutPostRedisplay();
            break;
    }
}

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    time_t seed = time(NULL);

    draw_class(seed);

    glPushMatrix();
    glScalef(-1, 1, 1);
    glRotatef(180, 0, 1, 0);
    draw_class(seed);
    glPopMatrix();

    draw_wall();

    glutSwapBuffers();
}

void init(void)
{
    glEnable(GL_LIGHT0);
    glEnable(GL_LIGHTING);
    glEnable(GL_DEPTH_TEST);


    /*
    glMatrixMode(GL_PROJECTION);
    gluPerspective(130.0, 16.0 / 9.0, 1.0, 10.0);
    glMatrixMode(GL_MODELVIEW);
    */

    glRotated(90, 0.0, 0.0, 1.0);
}

int main(int argc, char **argv)
{
    glutInit(&argc, argv);

    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutCreateWindow("");
    glEnable(GL_NORMALIZE);
    glutDisplayFunc(display);
    glutKeyboardFunc(key);

    init();
    glutMainLoop();
    return 0;
}