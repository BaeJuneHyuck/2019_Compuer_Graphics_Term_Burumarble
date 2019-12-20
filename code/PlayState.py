from tkinter import DISABLED

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import PIL as Image
import numpy as np

class PlayState():

    def __init__(self, _camera, w, h, textures):
        self.camera = _camera;
        self.width = w
        self.height = h
        self.texArr = textures


    def setWidthHeight(self, w, h):
        self.width = w
        self.height = h

    def nameSpace(self):
        glDisable(GL_TEXTURE_2D)
        glBegin(GL_QUADS)
        # glColor3f(0, 0, 0.5)
        glNormal3f(0, 0, 1)
        glTexCoord2f(0, 0)
        glVertex3f(-6.5, 8.5, 0.5)
        glTexCoord2f(0, 1)
        glVertex3f(16, 8.5, 0.5)
        glTexCoord2f(1, 1)
        glVertex3f(16, 15.5, 0.5)
        glTexCoord2f(1, 0)
        glVertex3f(-6.5, 15.5, 0.5)
        glEnd()
        glEnable(GL_TEXTURE_2D)


    def pictureSpace(self):
        glBindTexture(GL_TEXTURE_2D, self.texArr[17])
        glBegin(GL_QUADS)
        #glColor3f(0, 0, 0.5)
        glNormal3f(0, 0, 1)
        glTexCoord2f(0, 0)
        glVertex3f(-15.5, -15.5, 0.5)
        glTexCoord2f(0, 1)
        glVertex3f(-6.5, -15.5, 0.5)
        glTexCoord2f(1, 1)
        glVertex3f(-6.5, 15.5, 0.5)
        glTexCoord2f(1, 0)
        glVertex3f(-15.5, 15.5, 0.5)
        glEnd()

    def goldTextureSpace(self):
        glBindTexture(GL_TEXTURE_2D, self.texArr[26])
        #glBindTexture(GL_TEXTURE_2D, self.texArr[25])
        glBegin(GL_QUADS)
        #glColor3f(0.5, 0, 0.5)
        glNormal3f(0, 0, 1)
        glTexCoord2f(0, 0)
        #glColor3f(0.5, 0, 0.5)
        glVertex3f(-6.7, -16, 0)
        glTexCoord2f(0, 1)
        glVertex3f(0, -16, 0)
        glTexCoord2f(1, 1)
        glVertex3f(0, 9, 0)
        glTexCoord2f(1, 0)
        glVertex3f(-6.7, 9, 0)
        glEnd()

    def goldNumSpace(self):
        glColor3f(1, 1, 1)
        glDisable(GL_TEXTURE_2D)
        glBegin(GL_QUADS)
        # glColor3f(0.5, 0, 0.5)
        glNormal3f(0, 0, 1)
        glTexCoord2f(0, 0)
        # glColor3f(0.5, 0, 0.5)
        glVertex3f(-0, -15.7, 0.5)
        glTexCoord2f(0, 1)
        glVertex3f(16, -15.7, 0.5)
        glTexCoord2f(1, 1)
        glVertex3f(16, 9, 0.5)
        glTexCoord2f(1, 0)
        glVertex3f(-0, 9, 0.5)
        glEnd()
        glEnable(GL_TEXTURE_2D)


    # 플레이어 스테이터스 화면 그리기
    def draw(self):

        #왼쪽 하단 스테이터스
        glViewport(0, 0, 200, 100)
        glPushMatrix()
        gluLookAt(0, 0, 28, 0, 0, 0, 0, 1, 0)
        self.goldTextureSpace()
        self.pictureSpace()
        glColor3f(153/255, 153/255, 51/255)
        self.nameSpace()
        self.goldNumSpace()


        playerName = "Play2"
        self.drawPlayName(playerName)
        self.drawGoldName()
        glodNum = "100,000,000"
        self.drawGoldNum(glodNum)

        glPopMatrix()

        #왼쪽 상단 스테이터스
        glViewport(0, 700, 200, 100)
        glPushMatrix()
        gluLookAt(0, 0, 28, 0, 0, 0, 0, 1, 0)
        self.goldTextureSpace()
        self.pictureSpace()
        glColor3f(102/255, 102/255, 1)
        self.nameSpace()
        self.goldNumSpace()


        playerName = "Play1"
        self.drawPlayName(playerName)
        self.drawGoldName()
        glodNum = "100,000,000"
        self.drawGoldNum(glodNum)

        glPopMatrix()

        #오른쪽 하단 스테이터스
        glViewport(600, 0, 200, 100)
        glPushMatrix()
        gluLookAt(0, 0, 28, 0, 0, 0, 0, 1, 0)
        self.goldTextureSpace()
        self.pictureSpace()
        glColor3f(0, 153/255, 0)
        self.nameSpace()
        self.goldNumSpace()

        playerName = "Play4"
        self.drawPlayName(playerName)
        self.drawGoldName()
        glodNum = "100,000,000"
        self.drawGoldNum(glodNum)

        glPopMatrix()

        #오른쪽 상단 스테이터스
        glViewport(600, 700, 200, 100)
        glPushMatrix()
        gluLookAt(0, 0, 28, 0, 0, 0, 0, 1, 0)
        self.goldTextureSpace()
        self.pictureSpace()
        glColor3f(1, 102/255, 102/255)
        self.nameSpace()
        self.goldNumSpace()

        playerName = "Play3"
        self.drawPlayName(playerName)
        self.drawGoldName()
        glodNum = "100,000,000"
        self.drawGoldNum(glodNum)
        glColor3f(1, 1, 1)
        glPopMatrix()




        # 버튼
        glViewport(350, 0, 100, 100)
        glPushMatrix()
        gluLookAt(-8, -8, 15, -8, -8, 0.5, 0, 1, 0)


        glBindTexture(GL_TEXTURE_2D, self.texArr[17])
        glBegin(GL_QUADS)
        glNormal3f(0, 0, 1)
        glTexCoord2f(0, 1)
        glVertex3f(-16, -16, 0.5)
        glTexCoord2f(1, 1)
        glVertex3f(0, -16, 0.5)
        glTexCoord2f(1, 0)
        glVertex3f(0, 0, 0.5)
        glTexCoord2f(0, 0)
        glVertex3f(-16, 0, 0.5)
        glEnd()
        glPopMatrix()

    def drawGoldNum(self, glodNum):
        glRasterPos3f(0, -5, 0.7)
        for string in glodNum:
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ctypes.c_int(ord(string)))

    def drawPlayName(self, playerName):
        glRasterPos3f(-5, 10, 0.7)
        for string in playerName:
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ctypes.c_int(ord(string)))

    def drawGoldName(self):
        glodName = "GOLD"
        glRasterPos3f(0, 4, 0.7)
        for string in glodName:
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ctypes.c_int(ord(string)))


