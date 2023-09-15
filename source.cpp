#ifdef __APPLE_CC__
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif

#include <math.h>
#include <stdlib.h>
#include <cstring>
#include <string>

double cosT;
double sinT;

int updateTimer = 1;
double LINE_LENGTH = .75;
double PIVOT_POS[2] = { .0, .5 };
double GRAVITY_CONST = 9.801;

double weightCenter[2];
double weightMass = 1.;

double gravity_val = GRAVITY_CONST * weightMass / 1000;
double tension_val;
double acceleration_val;
double velocity_val;

double gravity[2] = { .0, -gravity_val };
double tension[2];
double acceleration[2];
double velocity[2];

void text_out(int x, int y, float r, float g, float b, char* string)
{
    glColor3f(r, g, b);
    glRasterPos2f(x, y);
    int len, i;
    len = (int)strlen(string);
    for (i = 0; i < len; i++) {
        glutBitmapCharacter(GLUT_BITMAP_8_BY_13, string[i]);
    }
}

void updatePendulum()
{
    if (weightCenter[1] < -.251)
    {
        weightCenter[1] = -.25;
    }

    cosT = floor(weightCenter[0] / LINE_LENGTH * 100) / 100;
    sinT = floor((PIVOT_POS[1] - weightCenter[1]) / LINE_LENGTH * 100) / 100;

    tension_val = gravity_val;
    tension[0] = -(weightCenter[0]) * (tension_val / LINE_LENGTH);
    tension[1] = (PIVOT_POS[1] - weightCenter[1]) * (tension_val / LINE_LENGTH);

    acceleration_val = -gravity_val * (weightCenter[0] / LINE_LENGTH );
    acceleration[0] = sinT * acceleration_val;
    acceleration[1] = cosT * acceleration_val;

    velocity_val += acceleration_val;
    velocity[0] = sinT * velocity_val / 10000;
    velocity[1] = cosT * velocity_val / 10000;

    weightCenter[0] += velocity[0];
    weightCenter[1] += velocity[1];
}

void DrawCircle(double cx, double cy, double r, int num_segments)
{
    glBegin(GL_LINE_LOOP);
    glColor3d(1., 1., 1.);
    for (int ii = 0; ii < num_segments; ii++)
    {
        double theta = 2.0 * 3.1415926 * double(ii) / double(num_segments);//get the current angle

        double x = r * cos(theta);//calculate the x component
        double y = r * sin(theta);//calculate the y component

        glVertex2d(x + cx, y + cy);//output vertex
    }
    glEnd();
}

void display() {
    // Set every pixel in the frame buffer to the current clear color.
    glClear(GL_COLOR_BUFFER_BIT);

    if (updateTimer == 0 && weightCenter[1] > -.27)
    {
        updatePendulum();
        updateTimer = 1;
    }
    updateTimer--;

    glBegin(GL_LINES);
    glColor3d(1., 1., 1.);
    glVertex2d(weightCenter[0], weightCenter[1]);
    glVertex2d(PIVOT_POS[0], PIVOT_POS[1]);

    glColor3d(1., .0, .0);
    glVertex2d(weightCenter[0], weightCenter[1]);
    glVertex2d(weightCenter[0] + gravity[0] * 10., weightCenter[1] + gravity[1] * 10.);

    glColor3d(1., 1., .0);
    glVertex2d(weightCenter[0], weightCenter[1]);
    glVertex2d(weightCenter[0] + acceleration[0] * 10., weightCenter[1] + acceleration[1] * 10.);

    glColor3d(.0, 1., .0);
    glVertex2d(weightCenter[0], weightCenter[1]);
    glVertex2d(weightCenter[0] + tension[0] * 10., weightCenter[1] + tension[1] * 10.);

    glColor3d(.0, .0, 1.);
    glVertex2d(weightCenter[0], weightCenter[1]);
    glVertex2d(weightCenter[0] + velocity[0] * 10., weightCenter[1] + velocity[1] * 10.);
    
    glEnd();

    DrawCircle(weightCenter[0], weightCenter[1], .1, 100);
    
    std::string text = "Cos: ";
    text += std::to_string(cosT);
    text += "       Sin: ";
    text += std::to_string(sinT);
    text += "       X: ";
    text += std::to_string(weightCenter[0]);
    text += "       Y: ";
    text += std::to_string(weightCenter[1]);

    int text_len = text.length();
    char* char_array = new char[text_len + 1];
    strcpy(char_array, text.c_str());

    text_out(-1, -1, 1., 1., 1., char_array);

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
