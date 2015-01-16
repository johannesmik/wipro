__author__ = 'johannes'

"""
Plot the Mandelbrot set using OpenGL and GLUT

Based on:
Shaders in PyOpenGL: http://pyopengl.sourceforge.net/context/tutorials/shader_1.html
Mandelbrot Fragment Shader: http://nuclear.mutantstargoat.com/articles/sdr_fract/
Tourist Guide: http://www.nahee.com/Derbyshire/manguide.html
"""

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import shaders
from OpenGL.arrays import vbo

width, height = 800, 600                               # window size

scale_x = 1.0
scale = 4.0



def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex2f(-1, -1)
    glTexCoord2f(1, 0)
    glVertex2f(1, -1)
    glTexCoord2f(1, 1)
    glVertex2f(1, 1)
    glTexCoord2f(0, 1)
    glVertex2f(-1, 1)
    glEnd()

    glutSwapBuffers()                                  # important for double buffering

def zoomin():
    global scale
    global scale_x
    scale /= scale_x
    scale_x += 0.00001
    scale_loc = glGetUniformLocation(shader, 'scale')
    glUniform1f(scale_loc, scale)
    glutPostRedisplay()



glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)
glutInitWindowPosition(0, 0)
window = glutCreateWindow("Mandelbrot")

# Read in shader
fragment_shader_source = ""
with open("mandelbrot.fs") as f:
    fragment_shader_source = f.read()

fragment_shader = shaders.compileShader(fragment_shader_source, GL_FRAGMENT_SHADER)
shader = shaders.compileProgram(fragment_shader)



shaders.glUseProgram(shader)

# Set Uniform variables

iter_loc = glGetUniformLocation(shader, 'iter')
glUniform1i(iter_loc, 200)

center_loc = glGetUniformLocation(shader, 'center')
glUniform2f(center_loc, -0.275, 0)

scale_loc = glGetUniformLocation(shader, 'scale')
glUniform1f(scale_loc, scale)

glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(zoomin)                                     # draw all the time
glutMainLoop()
