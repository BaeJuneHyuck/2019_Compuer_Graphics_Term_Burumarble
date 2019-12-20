from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time
import random

isTop = 0
isGround = 0

class Dice():
    """ 주사위 굴리기(stage 1)에서 보여질 주사위 """
    def __init__(self, textures):
        self.texArr = textures
        self.value = 1
        self.z = 2.0
        self.rotation_x = 0.0
        self.rotation_y = 0.0
        self.rotation_z = 0.0
        self.textures = []
        self.rolling = False

        # 주사위 텍스처 6장을 뽑아서 배열로 만듬
        # 주사위를 굴리면 값만큼 배열을 당김
        # 값 3이면 배열을 3칸씩 왼쪽으로 밀어서 3번이 윗면으로 가는구조로
        for i in range(0,6):
            self.textures.append(textures[i+18])

    def draw(self):
        glPushMatrix()
        glTranslatef(10, 10, self.z)
        glRotatef(self.rotation_x, 1.0, 0, 0)
        glRotatef(self.rotation_y, 0, 1.0, 0)
        glRotatef(self.rotation_z, 0, 0, 1.0)
        glTranslatef(-10, -10, -2)

        glBindTexture(GL_TEXTURE_2D, self.texArr[18])
        glBegin(GL_QUADS)
        glNormal3f(0, 0, 1)
        glTexCoord2f(0, 0)
        glVertex3f(8, 8, 0)
        glTexCoord2f(0, 1)
        glVertex3f(12, 8, 0)
        glTexCoord2f(1, 1)
        glVertex3f(12, 12, 0)
        glTexCoord2f(1, 0)
        glVertex3f(8, 12, 0)
        glEnd()

        glBindTexture(GL_TEXTURE_2D, self.texArr[19])
        glBegin(GL_QUADS)
        glNormal3f(1, 0, 0)
        glTexCoord2f(0, 0)
        glVertex3f(8, 8, 0)
        glTexCoord2f(0, 1)
        glVertex3f(12, 8, 0)
        glTexCoord2f(1, 1)
        glVertex3f(12, 8, 4)
        glTexCoord2f(1, 0)
        glVertex3f(8, 8, 4)
        glEnd()

        glBindTexture(GL_TEXTURE_2D, self.texArr[20])
        glBegin(GL_QUADS)
        glNormal3f(0, 0, -1)
        glTexCoord2f(0, 0)
        glVertex3f(12, 8, 0)
        glTexCoord2f(0, 1)
        glVertex3f(12, 12, 0)
        glTexCoord2f(1, 1)
        glVertex3f(12, 12, 4)
        glTexCoord2f(1, 0)
        glVertex3f(12, 8, 4)
        glEnd()

        glBindTexture(GL_TEXTURE_2D, self.texArr[21])
        glBegin(GL_QUADS)
        glNormal3f(-1, 0, 0)
        glTexCoord2f(0, 0)
        glVertex3f(12, 12, 0)
        glTexCoord2f(0, 1)
        glVertex3f(8, 12, 0)
        glTexCoord2f(1, 1)
        glVertex3f(8, 12, 4)
        glTexCoord2f(1, 0)
        glVertex3f(12, 12, 4)
        glEnd()

        glBindTexture(GL_TEXTURE_2D, self.texArr[22])
        glBegin(GL_QUADS)
        glNormal3f(0, -1, 0)
        glTexCoord2f(0, 0)
        glVertex3f(8, 12, 0)
        glTexCoord2f(0, 1)
        glVertex3f(8, 8, 0)
        glTexCoord2f(1, 1)
        glVertex3f(8, 8, 4)
        glTexCoord2f(1, 0)
        glVertex3f(8, 12, 4)
        glEnd()

        glBindTexture(GL_TEXTURE_2D, self.texArr[23])
        glBegin(GL_QUADS)
        glNormal3f(0, 0, 1)
        glTexCoord2f(0, 0)
        glVertex3f(8, 8, 4)
        glTexCoord2f(0, 1)
        glVertex3f(12, 8, 4)
        glTexCoord2f(1, 1)
        glVertex3f(12, 12, 4)
        glTexCoord2f(1, 0)
        glVertex3f(8, 12, 4)
        glEnd()
        glPopMatrix()

        glutPostRedisplay()
        # 높이 조절하는부분을 쓰레드로 따로 빼거나 타이머 적용해서 gutPostRedisplay 넣어서 바로바로 보이도록해야함

        global isTop
        global isGround
        if self.rolling == True:
            if self.z <= 14 and isTop == 0:
                self.z += 0.25
                self.rotation_x += 45
                self.rotation_y += 45
                self.rotation_z += 45
                if self.z >= 14:
                    isTop = 1
            if isTop == 1 and isGround == 0:
                self.z -= 0.25
                self.rotation_x -= 45
                self.rotation_y -= 45
                self.rotation_z -= 45
                if self.z == 2:
                    if self.value == 1:
                        self.rotation_x = 0
                        self.rotation_y = 180
                        self.rotation_z = 0
                    elif self.value == 2:
                        self.rotation_x = 270
                        self.rotation_y = 270
                        self.rotation_z = 0
                    elif self.value == 3:
                        self.rotation_x = 90
                        self.rotation_y = 90
                        self.rotation_z = 90
                    elif self.value == 4:
                        self.rotation_x = 90
                        self.rotation_y = 0
                        self.rotation_z = 0
                    elif self.value == 113:
                        self.rotation_x = 0
                        self.rotation_y = 90
                        self.rotation_z = 0
                    elif self.value == 6:
                        self.rotation_x = 0
                        self.rotation_y = 0
                        self.rotation_z = 0
                    isGround = 1
        if isGround == 1:
            self.rolling = False
            isTop = 0
            isGround = 0
        glutPostRedisplay()

    def roll(self):
        global isTop
        global isGround
        self.rolling = True
        self.value = random.randrange(1, 7)
        return self.value
