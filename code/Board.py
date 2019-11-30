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

    def draw(self, index):

        if(index >= 0 and index < 5) :
            # glBindTexture(GL_TEXTURE_2D, texArr[0])
            glBegin(GL_QUADS)
            glNormal3f(0, 0, 1)
            glTexCoord2f(0, 0)
            glVertex3f(index*4, 0, 0)
            glTexCoord2f(0, 1)
            glVertex3f((index+1)*4, 0, 0)
            glTexCoord2f(1, 1)
            glVertex3f((index+1)*4, 4, 0)
            glTexCoord2f(1, 0)
            glVertex3f(index*4, 4, 0)
            glEnd()

            #glBindTexture(GL_TEXTURE_2D, texArr[1])
            glBegin(GL_QUADS)
            glNormal3f(1, 0, 0)
            glTexCoord2f(0, 0)
            glVertex3f(index*4, 0, 0)
            glTexCoord2f(0, 1)
            glVertex3f((index+1)*4, 0, 0)
            glTexCoord2f(1, 1)
            glVertex3f((index+1)*4, 0, 2)
            glTexCoord2f(1, 0)
            glVertex3f(index*4, 0, 2)
            glEnd()

            #glBindTexture(GL_TEXTURE_2D, texArr[2])
            glBegin(GL_QUADS)
            glNormal3f(0, 0, -1)
            glTexCoord2f(0, 0)
            glVertex3f((index+1)*4, 0, 0)
            glTexCoord2f(0, 1)
            glVertex3f((index+1)*4, 4, 0)
            glTexCoord2f(1, 1)
            glVertex3f((index + 1) * 4, 4, 2)
            glTexCoord2f(1, 0)
            glVertex3f((index + 1) * 4, 0, 2)
            glEnd()

            #glBindTexture(GL_TEXTURE_2D, texArr[3])
            glBegin(GL_QUADS)
            glNormal3f(-1, 0, 0)
            glTexCoord2f(0, 0)
            glVertex3f((index + 1) * 4, 4, 0)
            glTexCoord2f(0, 1)
            glVertex3f(index*4, 4, 0)
            glTexCoord2f(1, 1)
            glVertex3f(index * 4, 4, 2)
            glTexCoord2f(1, 0)
            glVertex3f((index + 1) * 4, 4, 2)
            glEnd()

            #glBindTexture(GL_TEXTURE_2D, texArr[4])
            glBegin(GL_QUADS)
            glNormal3f(0, -1, 0)
            glTexCoord2f(0, 0)
            glVertex3f(index*4, 4, 0)
            glTexCoord2f(0, 1)
            glVertex3f(index*4, 0, 0)
            glTexCoord2f(1, 1)
            glVertex3f(index*4, 0, 2)
            glTexCoord2f(1, 0)
            glVertex3f(index*4, 4, 2)
            glEnd()

            #glBindTexture(GL_TEXTURE_2D, texArr[5])
            glBegin(GL_QUADS)
            glNormal3f(0, 1, 0)
            glTexCoord2f(0, 0)
            glVertex3f(index*4, 0, 2)
            glTexCoord2f(0, 1)
            glVertex3f((index+1)*4, 0, 2)
            glTexCoord2f(1, 1)
            glVertex3f((index+1)*4, 4, 2)
            glTexCoord2f(1, 0)
            glVertex3f(index*4, 4, 2)
            glEnd()

        glFlush()

