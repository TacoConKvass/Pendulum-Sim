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
double GRAVITY_CONST = 9.801;

double weightCenter[2] = { .0 , PIVOT_POS[1] - LINE_LENGTH };
double weightMass = 1.;
double gravity_val = GRAVITY_CONST * weightMass / 1000;

double gravity[2] = { .0, -gravity_val };
double tension[2];
double acceleration[2];
double velocity[2];

void updatePendulum()
{
    tension[0] = -(weightCenter[0]) * (gravity_val / LINE_LENGTH);
    tension[1] = (PIVOT_POS[1] - weightCenter[1]) * (gravity_val / LINE_LENGTH);

    acceleration[0] = tension[0] + gravity[0];
    acceleration[1] = tension[1] + gravity[1];

    velocity[0] += acceleration[0];
    velocity[1] += acceleration[1];

    weightCenter[0] += velocity[0];
    weightCenter[1] += velocity[1];
}

void DrawCircle(double cx, double cy, double r, int num_segments)
{
    glBegin(GL_LINE_LOOP);
    for (int ii = 0; ii < num_segments; ii++)
    {
        double theta = 2.0f * 3.1415926f * double(ii) / double(num_segments);//get the current angle

        double x = r * cosf(theta);//calculate the x component
        double y = r * sinf(theta);//calculate the y component

        glVertex2f(x + cx, y + cy);//output vertex

    }
    glEnd();
}

void display() {
    // Set every pixel in the frame buffer to the current clear color.
    glClear(GL_COLOR_BUFFER_BIT);

    if (updateTimer == 0)
    {
        updatePendulum();
        updateTimer = 30;
    }
    updateTimer--;

    glBegin(GL_LINES);
    glVertex2d(weightCenter[0], weightCenter[1]);
    glVertex2d(PIVOT_POS[0], PIVOT_POS[1]);
    glColor3d(1., 1., 1.);
    glEnd();

    DrawCircle(weightCenter[0], weightCenter[1], .1, 50);

    // Flush drawing command buffer to make drawing happen as soon as possible.
    glFlush();
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
    glutIdleFunc(display);
    glutKeyboardFunc(keyboard);

    // Tell GLUT to start reading and processing events.  This function
    // never returns; the program only exits when the user closes the main
    // window or kills the process.
    glutMainLoop();
}