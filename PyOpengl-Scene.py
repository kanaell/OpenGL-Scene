import Cube
import pygame
import os, sys

from pygame.locals import *

if not pygame.font: print("Warning, fonts disabled")
if not pygame.mixer: print("Warning, sound disabled")

from OpenGL.GL import *
from OpenGL.GLU import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600), DOUBLEBUF|OPENGL)
    pygame.display.set_caption('OpenGL Cube Exemple')

    gluPerspective(45, (800/600), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -10)

    glRotatef(25, 1, -1, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-0.5, 0, 0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(0.5, 0, 0)
                if event.key == pygame.K_UP:
                    glTranslatef(0, 0.5, 0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0, -0.5, 0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0, 0, 1.0)
                if event.button == 5:
                    glTranslatef(0, 0, -1.0)

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube.Cube()
        pygame.display.flip()

main()
