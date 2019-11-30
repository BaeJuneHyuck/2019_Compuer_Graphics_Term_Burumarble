from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

class Board():
    """ 게임이 이뤄질 보드 """
    def __init__(self, pos, type,  text):
        super().__init__()
        # 시작지점 0 부터 끝지점 25 까지 순서대로 pos 번호 부여
        self.pos = pos

        # type 0 일반적인 땅(건물 구입가능한)
        # type 1 특수한 지역,  따로 처리
        self.type = 0
        self.owner = -1

        # 건물이 지어질 경우
        self.building = 0

        # 설명용 텍스트 설정
        self.text = text

        # pos에 맞게 x,y 위치 설정 하기
        # x = pos
        # y = 5-pos....

    def draw(self):

        if(self.pos >= 0 and self.pos < 5) :
            # glBindTexture(GL_TEXTURE_2D, texArr[0])
            glBegin(GL_QUADS)
            glNormal3f(0, 0, 1)
            glTexCoord2f(0, 0)
            glVertex3f(self.pos*4, 0, 0) #1
            glTexCoord2f(0, 1)
            glVertex3f((self.pos+1)*4, 0, 0) #2
            glTexCoord2f(1, 1)
            glVertex3f((self.pos+1)*4, 4, 0) #3
            glTexCoord2f(1, 0)
            glVertex3f(self.pos*4, 4, 0) #4
            glEnd()

            #glBindTexture(GL_TEXTURE_2D, texArr[1])
            glBegin(GL_QUADS)
            glNormal3f(1, 0, 0)
            glTexCoord2f(0, 0)
            glVertex3f(self.pos*4, 0, 0)
            glTexCoord2f(0, 1)
            glVertex3f((self.pos+1)*4, 0, 0)
            glTexCoord2f(1, 1)
            glVertex3f((self.pos+1)*4, 0, 2)
            glTexCoord2f(1, 0)
            glVertex3f(self.pos*4, 0, 2)
            glEnd()

            #glBindTexture(GL_TEXTURE_2D, texArr[2])
            glBegin(GL_QUADS)
            glNormal3f(0, 0, -1)
            glTexCoord2f(0, 0)
            glVertex3f((self.pos+1)*4, 0, 0)
            glTexCoord2f(0, 1)
            glVertex3f((self.pos+1)*4, 4, 0)
            glTexCoord2f(1, 1)
            glVertex3f((self.pos + 1) * 4, 4, 2)
            glTexCoord2f(1, 0)
            glVertex3f((self.pos + 1) * 4, 0, 2)
            glEnd()

            #glBindTexture(GL_TEXTURE_2D, texArr[3])
            glBegin(GL_QUADS)
            glNormal3f(-1, 0, 0)
            glTexCoord2f(0, 0)
            glVertex3f((self.pos + 1) * 4, 4, 0)
            glTexCoord2f(0, 1)
            glVertex3f(self.pos*4, 4, 0)
            glTexCoord2f(1, 1)
            glVertex3f(self.pos * 4, 4, 2)
            glTexCoord2f(1, 0)
            glVertex3f((self.pos + 1) * 4, 4, 2)
            glEnd()

            #glBindTexture(GL_TEXTURE_2D, texArr[4])
            glBegin(GL_QUADS)
            glNormal3f(0, -1, 0)
            glTexCoord2f(0, 0)
            glVertex3f(self.pos*4, 4, 0)
            glTexCoord2f(0, 1)
            glVertex3f(self.pos*4, 0, 0)
            glTexCoord2f(1, 1)
            glVertex3f(self.pos*4, 0, 2)
            glTexCoord2f(1, 0)
            glVertex3f(self.pos*4, 4, 2)
            glEnd()

            #glBindTexture(GL_TEXTURE_2D, texArr[5])
            glBegin(GL_QUADS)
            glNormal3f(0, 1, 0)
            glTexCoord2f(0, 0)
            glVertex3f(self.pos*4, 0, 2)
            glTexCoord2f(0, 1)
            glVertex3f((self.pos+1)*4, 0, 2)
            glTexCoord2f(1, 1)
            glVertex3f((self.pos+1)*4, 4, 2)
            glTexCoord2f(1, 0)
            glVertex3f(self.pos*4, 4, 2)
            glEnd()

        if (self.pos >= 5 and self.pos < 9):
            # glBindTexture(GL_TEXTURE_2D, texArr[0])
            glBegin(GL_QUADS)
            glNormal3f(0, 0, 1)
            glTexCoord2f(0, 0)
            glVertex3f(16, (self.pos - 4)*4, 0)
            glTexCoord2f(0, 1)
            glVertex3f(20, (self.pos - 4)*4, 0)
            glTexCoord2f(1, 1)
            glVertex3f(20, (self.pos - 3)*4, 0)
            glTexCoord2f(1, 0)
            glVertex3f(16, (self.pos - 3)*4, 0)
            glEnd()

            # glBindTexture(GL_TEXTURE_2D, texArr[1])
            glBegin(GL_QUADS)
            glNormal3f(1, 0, 0)
            glTexCoord2f(0, 0)
            glVertex3f(16, (self.pos - 4)*4, 0)
            glTexCoord2f(0, 1)
            glVertex3f(20, (self.pos - 4)*4, 0)
            glTexCoord2f(1, 1)
            glVertex3f(20, (self.pos - 4)*4, 2)
            glTexCoord2f(1, 0)
            glVertex3f(16, (self.pos - 4)*4, 2)
            glEnd()

            # glBindTexture(GL_TEXTURE_2D, texArr[2])
            glBegin(GL_QUADS)
            glNormal3f(0, 0, -1)
            glTexCoord2f(0, 0)
            glVertex3f(20, (self.pos - 4)*4, 0)
            glTexCoord2f(0, 1)
            glVertex3f(20, (self.pos - 3)*4, 0)
            glTexCoord2f(1, 1)
            glVertex3f(20, (self.pos - 3)*4, 2)
            glTexCoord2f(1, 0)
            glVertex3f(20, (self.pos - 4)*4, 2)
            glEnd()

            # glBindTexture(GL_TEXTURE_2D, texArr[3])
            glBegin(GL_QUADS)
            glNormal3f(-1, 0, 0)
            glTexCoord2f(0, 0)
            glVertex3f(20, (self.pos - 3)*4, 0)
            glTexCoord2f(0, 1)
            glVertex3f(16, (self.pos - 3)*4, 0)
            glTexCoord2f(1, 1)
            glVertex3f(16, (self.pos - 3)*4, 2)
            glTexCoord2f(1, 0)
            glVertex3f(20, (self.pos - 3)*4, 2)
            glEnd()

            # glBindTexture(GL_TEXTURE_2D, texArr[4])
            glBegin(GL_QUADS)
            glNormal3f(0, -1, 0)
            glTexCoord2f(0, 0)
            glVertex3f(16, (self.pos - 3)*4, 0)
            glTexCoord2f(0, 1)
            glVertex3f(16, (self.pos - 4)*4, 0)
            glTexCoord2f(1, 1)
            glVertex3f(16, (self.pos - 4) * 4, 2)
            glTexCoord2f(1, 0)
            glVertex3f(16, (self.pos - 3)*4, 2)
            glEnd()

            # glBindTexture(GL_TEXTURE_2D, texArr[5])
            glBegin(GL_QUADS)
            glNormal3f(0, 0, 1)
            glTexCoord2f(0, 0)
            glVertex3f(16, (self.pos - 4) * 4, 2)
            glTexCoord2f(0, 1)
            glVertex3f(20, (self.pos - 4) * 4, 2)
            glTexCoord2f(1, 1)
            glVertex3f(20, (self.pos - 3) * 4, 2)
            glTexCoord2f(1, 0)
            glVertex3f(16, (self.pos - 3) * 4, 2)
            glEnd()

        if (self.pos >= 9 and self.pos < 13):
            # glBindTexture(GL_TEXTURE_2D, texArr[0])
            glBegin(GL_QUADS)
            glNormal3f(0, 0, 1)
            glTexCoord2f(0, 0)
            glVertex3f(20-4*(self.pos-8), 16, 0)  # 1
            glTexCoord2f(0, 1)
            glVertex3f(20-4*(self.pos-7), 16, 0)  # 2
            glTexCoord2f(1, 1)
            glVertex3f(20-4*(self.pos-7), 20, 0)  # 3
            glTexCoord2f(1, 0)
            glVertex3f(20-4*(self.pos-8), 20, 0)  # 4
            glEnd()

            # glBindTexture(GL_TEXTURE_2D, texArr[1])
            glBegin(GL_QUADS)
            glNormal3f(1, 0, 0)
            glTexCoord2f(0, 0)
            glVertex3f(20-4*(self.pos-8), 16, 0)
            glTexCoord2f(0, 1)
            glVertex3f(20-4*(self.pos-7), 16, 0)
            glTexCoord2f(1, 1)
            glVertex3f(20-4*(self.pos-7), 16, 2)
            glTexCoord2f(1, 0)
            glVertex3f(20-4*(self.pos-7), 16, 2)
            glEnd()

            # glBindTexture(GL_TEXTURE_2D, texArr[2])
            glBegin(GL_QUADS)
            glNormal3f(0, 0, -1)
            glTexCoord2f(0, 0)
            glVertex3f(20 - 4 * (self.pos - 7), 16, 0)
            glTexCoord2f(0, 1)
            glVertex3f(20-4*(self.pos-7), 20, 0)
            glTexCoord2f(1, 1)
            glVertex3f(20-4*(self.pos-7), 20, 2)
            glTexCoord2f(1, 0)
            glVertex3f(20 - 4 * (self.pos - 7), 16, 2)
            glEnd()

            # glBindTexture(GL_TEXTURE_2D, texArr[3])
            glBegin(GL_QUADS)
            glNormal3f(-1, 0, 0)
            glTexCoord2f(0, 0)
            glVertex3f(20 - 4 * (self.pos - 7), 20, 0)
            glTexCoord2f(0, 1)
            glVertex3f(20-4*(self.pos-8), 20, 0)
            glTexCoord2f(1, 1)
            glVertex3f(20-4*(self.pos-8), 20, 2)
            glTexCoord2f(1, 0)
            glVertex3f(20 - 4 * (self.pos - 7), 20, 2)
            glEnd()

            # glBindTexture(GL_TEXTURE_2D, texArr[4])
            glBegin(GL_QUADS)
            glNormal3f(0, -1, 0)
            glTexCoord2f(0, 0)
            glVertex3f(20-4*(self.pos-8), 20, 0)
            glTexCoord2f(0, 1)
            glVertex3f(20-4*(self.pos-8), 16, 0)
            glTexCoord2f(1, 1)
            glVertex3f(20-4*(self.pos-8), 16, 2)
            glTexCoord2f(1, 0)
            glVertex3f(20-4*(self.pos-8), 20, 2)
            glEnd()

            # glBindTexture(GL_TEXTURE_2D, texArr[5])
            glBegin(GL_QUADS)
            glNormal3f(0, 0, 1)
            glTexCoord2f(0, 0)
            glVertex3f(20 - 4 * (self.pos - 8), 16, 2)  # 1
            glTexCoord2f(0, 1)
            glVertex3f(20 - 4 * (self.pos - 7), 16, 2)  # 2
            glTexCoord2f(1, 1)
            glVertex3f(20 - 4 * (self.pos - 7), 20, 2)  # 3
            glTexCoord2f(1, 0)
            glVertex3f(20 - 4 * (self.pos - 8), 20, 2)  # 4
            glEnd()

        if (self.pos >= 13 and self.pos < 16):
            # glBindTexture(GL_TEXTURE_2D, texArr[0])
            glBegin(GL_QUADS)
            glNormal3f(0, 0, 1)
            glTexCoord2f(0, 0)
            glVertex3f(0, 20-4*(self.pos-11), 0)  # 1
            glTexCoord2f(0, 1)
            glVertex3f(4, 20-4*(self.pos-11), 0)  # 2
            glTexCoord2f(1, 1)
            glVertex3f(4, 20-4*(self.pos-12), 0)  # 3
            glTexCoord2f(1, 0)
            glVertex3f(0, 20-4*(self.pos-12), 0)   # 4
            glEnd()

            # glBindTexture(GL_TEXTURE_2D, texArr[1])
            glBegin(GL_QUADS)
            glNormal3f(1, 0, 0)
            glTexCoord2f(0, 0)
            glVertex3f(0, 20-4*(self.pos-11), 0)
            glTexCoord2f(0, 1)
            glVertex3f(4, 20-4*(self.pos-11), 0)
            glTexCoord2f(1, 1)
            glVertex3f(4, 20-4*(self.pos-11), 2)
            glTexCoord2f(1, 0)
            glVertex3f(4, 20-4*(self.pos-11), 2)
            glEnd()

            # glBindTexture(GL_TEXTURE_2D, texArr[2])
            glBegin(GL_QUADS)
            glNormal3f(0, 0, -1)
            glTexCoord2f(0, 0)
            glVertex3f(4, 20-4*(self.pos-11), 0)  # 2
            glTexCoord2f(0, 1)
            glVertex3f(4, 20-4*(self.pos-12), 0)
            glTexCoord2f(1, 1)
            glVertex3f(4, 20-4*(self.pos-12), 2)
            glTexCoord2f(1, 0)
            glVertex3f(4, 20-4*(self.pos-12), 2)
            glEnd()

            # glBindTexture(GL_TEXTURE_2D, texArr[3])
            glBegin(GL_QUADS)
            glNormal3f(-1, 0, 0)
            glTexCoord2f(0, 0)
            glVertex3f(4, 20-4*(self.pos-12), 0)
            glTexCoord2f(0, 1)
            glVertex3f(0, 20-4*(self.pos-12), 0)
            glTexCoord2f(1, 1)
            glVertex3f(0, 20-4*(self.pos-12), 2)
            glTexCoord2f(1, 0)
            glVertex3f(4, 20-4*(self.pos-12), 2)
            glEnd()

            # glBindTexture(GL_TEXTURE_2D, texArr[4])
            glBegin(GL_QUADS)
            glNormal3f(0, -1, 0)
            glTexCoord2f(0, 0)
            glVertex3f(0, 20-4*(self.pos-12), 0)
            glTexCoord2f(0, 1)
            glVertex3f(0, 20-4*(self.pos-11), 0)
            glTexCoord2f(1, 1)
            glVertex3f(0, 20-4*(self.pos-11), 2)
            glTexCoord2f(1, 0)
            glVertex3f(0, 20-4*(self.pos-12), 2)
            glEnd()

            # glBindTexture(GL_TEXTURE_2D, texArr[5])
            glBegin(GL_QUADS)
            glNormal3f(0, 1, 0)
            glTexCoord2f(0, 0)
            glVertex3f(0, 20 - 4 * (self.pos - 11), 2)  # 1
            glTexCoord2f(0, 1)
            glVertex3f(4, 20 - 4 * (self.pos - 11), 2)  # 2
            glTexCoord2f(1, 1)
            glVertex3f(4, 20 - 4 * (self.pos - 12), 2)  # 3
            glTexCoord2f(1, 0)
            glVertex3f(0, 20 - 4 * (self.pos - 12), 2)  # 4
            glEnd()

        glFlush()

