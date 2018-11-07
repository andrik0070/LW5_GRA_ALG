from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import sys
from pprint import pprint


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)

    glutInitWindowSize(800, 600)
    glutCreateWindow("OpenGL lesson 7")

    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutKeyboardFunc(processNormalKeys)
    glutSpecialFunc(processSpecialKeys)

    glutMainLoop()

    return 0


def reshape(w, h):
    glViewport(0, 0, w, h)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 10, 0, 10, -10, 10)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def processNormalKeys(key, x, y):
    if (key == 27):
        return 0
    elif (key == 65):
        glMatrixMode(GL_MODELVIEW)
        glTranslated(2, 2, 0)
        display()

def processSpecialKeys(key, x, y):
    if key == GLUT_KEY_UP:
        glMatrixMode(GL_MODELVIEW)
        glTranslated(0, 2, 0)
        display()
    elif key == GLUT_KEY_DOWN:
       glMatrixMode(GL_MODELVIEW)
       glRotated(5, 1, 1, 1)
       display()


