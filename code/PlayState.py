from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import PIL as Image
import numpy as np

class PlayState():

    def __init__(self, _camera, w, h):
        self.camera = _camera;
        self.width = w
        self.height = h
#        self.texArr = textures


    def setWidthHeight(self, w, h):
        self.width = w
        self.height = h

    def pictureSpace(self):
        glBegin(GL_QUADS)
        #glColor3f(0, 0, 0.5)
        glNormal3f(0, 0, 1)
        glTexCoord2f(0, 0)
        glVertex3f(-16, -16, 0.5)
        glTexCoord2f(0, 1)
        glVertex3f(0, -16, 0.5)
        glTexCoord2f(1, 1)
        glVertex3f(0, 0, 0.5)
        glTexCoord2f(1, 0)
        glVertex3f(-16, 0, 0.5)
        glEnd()

    def drawBackground(self):
        glBegin(GL_QUADS)
        #glColor3f(0.5, 0, 0.5)
        glNormal3f(0, 0, 1)
        glTexCoord2f(0, 0)
        glVertex3f(-16, -16, 0)
        glTexCoord2f(0, 1)
        glVertex3f(16, -16, 0)
        glTexCoord2f(1, 1)
        glVertex3f(16, 16, 0)
        glTexCoord2f(1, 0)
        glVertex3f(-16, 16, 0)
        glEnd()

    # 플레이어 스테이터스 화면 그리기
    def draw(self):
        #오른쪽 상단 스테이터스
        glViewport(0, 0, 200, 100)
        glPushMatrix()
        gluLookAt(0, 0, 1, 0, 0, 0, 0, 1, 0)
        self.drawBackground()
        self.pictureSpace()
        glPopMatrix()

        #오른쪽 하단 스테이터스
        glViewport(0, 700, 200, 100)
        glPushMatrix()
        gluLookAt(0, 0, 50, 0, 0, 0, 0, 1, 0)
        self.drawBackground()
        self.pictureSpace()
        glPopMatrix()

        #왼쪽 하단 스테이터스
        glViewport(600, 0, 200, 100)
        glPushMatrix()
        gluLookAt(0, 0, 1, 0, 0, 0, 0, 1, 0)
        self.drawBackground()
        self.pictureSpace()
        glPopMatrix()

        #왼쪽 상단 스테이터스
        glViewport(600, 700, 200, 100)
        glPushMatrix()
        gluLookAt(0, 0, 1, 0, 0, 0, 0, 1, 0)
        self.drawBackground()
        self.pictureSpace()
        glPopMatrix()

        # 버튼
        glViewport(340, 0, 120, 80)
        glPushMatrix()
        gluLookAt(0, 0, 1, 0, 0, 0, 0, 1, 0)
        glBegin(GL_QUADS)

        glNormal3f(0, 0, 1)
        glTexCoord2f(0, 0)
        glVertex3f(-16, -16, 0.5)
        glTexCoord2f(0, 1)
        glVertex3f(0, -16, 0.5)
        glTexCoord2f(1, 1)
        glVertex3f(0, 0, 0.5)
        glTexCoord2f(1, 0)
        glVertex3f(-16, 0, 0.5)
        glEnd()

        glPopMatrix()

