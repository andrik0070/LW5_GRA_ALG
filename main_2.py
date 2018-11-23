from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import sys
from pprint import pprint

first_letter_points = []
first_letter_faces = []
second_letter_points = []
second_letter_faces = []
xAngle = 0
yAngle = 0


def load_points_faces(file_name, points, faces):
    with open(file_name) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        point_number = int(content.pop(0))

        for point in content[:point_number]:
            points.append(tuple([int(coordinate) for coordinate in point.split(' ')]))
        del content[:point_number]

        content.pop(0)

        for face in content:
            faces.append([int(el) for el in face.split(' ')])


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)

    glutInitWindowSize(800, 600)
    glutCreateWindow("OpenGL lesson 7")

    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutKeyboardFunc(processNormalKeys)
    glutSpecialFunc(processSpecialKeys)
    glutMouseFunc(mouseClilc)

    glutMainLoop()

    return 0


def reshape(w, h):
    glViewport(0, 0, w, h)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-500, 500, -500, 500, -500, 500)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def processNormalKeys(key, x, y):
    if (key == 27):
        return 0
    elif (key == 65):
        glMatrixMode(GL_MODELVIEW)
        glTranslated(2, 2, 0)
        display()
    elif (key == b'+'):
        glMatrixMode(GL_MODELVIEW)
        glScalef(1.1, 1.1, 1.1)
        display()
    elif (key == b'-'):
        glMatrixMode(GL_MODELVIEW)
        glScalef(0.9, 0.9, 0.9)
        display()


def processSpecialKeys(key, x, y):
    if key == GLUT_KEY_UP:
        glMatrixMode(GL_MODELVIEW)
        glRotated(10, 0, 1, 0)
        display()
    elif key == GLUT_KEY_DOWN:
        glMatrixMode(GL_MODELVIEW)
        glRotated(-10, 0, 1, 0)
        display()
    elif key == GLUT_KEY_LEFT:
        glMatrixMode(GL_MODELVIEW)
        glTranslated(-10, 0, 0)
        display()
    elif key == GLUT_KEY_RIGHT:
        glMatrixMode(GL_MODELVIEW)
        glTranslated(10, 0, 0)
        display()
    elif key == GLUT_KEY_HOME:
        glMatrixMode(GL_MODELVIEW)
        glRotatef(-10, 1, 0, 0)
        display()
    elif key == GLUT_KEY_END:
        glMatrixMode(GL_MODELVIEW)
        glRotatef(-10, 0, 1, 0)
        display()
    elif key == GLUT_KEY_DELETE:
        glMatrixMode(GL_MODELVIEW)
        glRotatef(-10, 0, 0, 1)
        display()
    elif key == GLUT_KEY_PAGE_UP:
        glMatrixMode(GL_MODELVIEW)
        glRotatef(10, 1, 1, 1)
        display()
    elif key == GLUT_KEY_PAGE_DOWN:
        glMatrixMode(GL_MODELVIEW)
        glRotatef(-10, 1, 1, 1)
        display()


def display():
    global first_letter_points
    global first_letter_faces

    global second_letter_points
    global second_letter_faces

    glLineWidth(5)
    glClearColor(1, 1, 1, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)

    for face in first_letter_faces:
        glBegin(GL_LINE_LOOP)
        for point_number in face:
            glVertex3f(first_letter_points[point_number][0], first_letter_points[point_number][1],
                       first_letter_points[point_number][2])
        glEnd()

    for face in second_letter_faces:
        glBegin(GL_LINE_LOOP)
        for point_number in face:
            glVertex3f(second_letter_points[point_number][0], second_letter_points[point_number][1],
                       second_letter_points[point_number][2])
        glEnd()
    glutSwapBuffers()


def mouseClilc(button, state, x, y):
    pprint(x)
    pprint(y)
    pprint('\n')


load_points_faces('./data_2_G.txt', first_letter_points, first_letter_faces)
load_points_faces('./data_2.txt', second_letter_points, second_letter_faces)
main()
