#ifdef __APPLE_CC__
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif

#include <math.h>
#include <stdlib.h>

int updateTimer = 60;
double LINE_LENGTH = .75;
double PIVOT_POS[2] = { .0, .5 };
double GRAVITY = 9.801;

double weightCenter[2] = { .0 , PIVOT_POS[1] - LINE_LENGTH };
double weightMass = 1.;

void updatePendulum() 
{

}


void display() {
    // Set every pixel in the frame buffer to the current clear color.
    glClear(GL_COLOR_BUFFER_BIT);

    if (updateTimer == 0)
    {
        updatePendulum();
        updateTimer = 60;
    }
    updateTimer--;

    glBegin(GL_QUADS);
    glVertex2d(weightCenter[0] + .05, weightCenter[1] + .05);
    glVertex2d(weightCenter[0] + .05, weightCenter[1] - .05);
    glVertex2d(weightCenter[0] - .05, weightCenter[1] - .05);
    glVertex2d(weightCenter[0] - .05, weightCenter[1] + .05);
    glColor3d(1., 1., 1.);
    glEnd();

    glBegin(GL_LINES);
    glVertex2d(weightCenter[0], weightCenter[1]);
    glVertex2d(PIVOT_POS[0], PIVOT_POS[1]);
    glColor3d(1., 1., 1.);
    glEnd();

    // Flush drawing command buffer to make drawing happen as soon as possible.
    glFlush();
    glutPostRedisplay();
}

void keyboard(unsigned char key, int x, int y)
{
    switch (key) {
        case 27:  // escape key
            exit(0);
            break;
        default:
            break;
    }
}

int main(int argc, char** argv)
{
    weightCenter[0] = .74;
    weightCenter[1] = .378;

    // Use a single buffered window in RGB mode (as opposed to a double-buffered
    // window or color-index mode).
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

    glutInitWindowPosition(400, 50);
    glutInitWindowSize(700, 700);
    glutCreateWindow("Pendulum Simulation");

    // Tell GLUT that whenever the main window needs to be repainted that it
    // should call the function display().
    glutDisplayFunc(display);
    glutKeyboardFunc(keyboard);

    // Tell GLUT to start reading and processing events.  This function
    // never returns; the program only exits when the user closes the main
    // window or kills the process.
    glutMainLoop();
}