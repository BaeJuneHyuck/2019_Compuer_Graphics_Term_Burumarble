from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

class Building() :
    vertexQuadArray = [(4.0, 4.0, 4.0), (4, -4, 4), (-4, -4, 4), (-4, 4, 4), (4, 4, -4), (4, -4, -4), (-4, -4, -4),
                       (-4, 4, -4)]
    vertexTraArray = [(5, 5, 5), (-5, 5, 5), (-5, 5, -5), (5, 5, -5), (0, 5, 0)]
    def __init__(self, color, texArr):
        self.color = color
        self.texArr = texArr

    # 1번 땅이 6,2,2.5 이다.
    # moveZ 에 2.5를 넣으면 딱 땅바닥에 안착
    # moveX 엥 +4 씩 하면 됨
    # moveY 도 + 4 씩 하면 됨
    def firstBuilding(self, moveX, moveY, moveZ):
        # 정면 왼쪽 삼각형
        glBegin(GL_TRIANGLES)
        glColor3f(1, 1, 1)
        glVertex3f(-1 + moveX, -1 + moveY, 0.5 + moveZ)
        glVertex3f(-1 + moveX, 1 + moveY, 0.5 + moveZ)
        glVertex3f(moveX, moveY, 2 + moveZ)
        glEnd()

        # 정면 삼각형
        glBegin(GL_TRIANGLES)
        glColor3f(1, 1, 1)
        glVertex3f(1 + moveX, -1 + moveY, 0.5 + moveZ)
        glVertex3f(-1 + moveX, -1 + moveY, 0.5 + moveZ)
        glVertex3f(moveX, moveY, 2 + moveZ)
        glEnd()

        # 정면 오른쪽 삼각형
        glBegin(GL_TRIANGLES)
        glColor3f(1, 1, 1)
        glVertex3f(1 + moveX, 1 + moveY, 0.5 + moveZ)
        glVertex3f(1 + moveX, -1 + moveY, 0.5 + moveZ)
        glVertex3f(moveX, moveY, 2 + moveZ)
        glEnd()

        # 정면 맞은편 삼각형
        glBegin(GL_TRIANGLES)
        glColor3f(1, 1, 1)
        glVertex3f(-1 + moveX, 1 + moveY, 0.5 + moveZ)
        glVertex3f(1 + moveX, 1 + moveY, 0.5 + moveZ)
        glVertex3f(moveX, moveY, 2 + moveZ)
        glEnd()

        # 건물 윗면
        glBegin(GL_QUADS)
        glNormal3f(0.0, 0.0, 1)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-1 + moveX, 1 + moveY, 0.5 + moveZ)
        glTexCoord2f(0.0, 1)
        glVertex3f(-1 + moveX, -1 + moveY, 0.5 + moveZ)
        glTexCoord2f(1, 1)
        glVertex3f(1 + moveX, -1 + moveY, 0.5 + moveZ)
        glTexCoord2f(1, 0.0)
        glVertex3f(1 + moveX, 1 + moveY, 0.5 + moveZ)
        glEnd()

        # 건물 앞면 오른쪽 면
        glBindTexture(GL_TEXTURE_2D, self.texArr[27])
        glBegin(GL_QUADS)
        glNormal3f(1, 0.0, 0.0)
        glTexCoord2f(1, 0.0)
        glVertex3f(0.75 + moveX, 0.75 + moveY, 0.5 + moveZ)
        glTexCoord2f(0, 0)
        glVertex3f(0.75 + moveX, -0.75 + moveY, 0.5 + moveZ)
        glTexCoord2f(0, 1)
        glVertex3f(0.75 + moveX, -0.75 + moveY, -0.5 + moveZ)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(0.75 + moveX, 0.75 + moveY, -0.5 + moveZ)
        glEnd()


        # 건물 앞면 왼쪽
        glBindTexture(GL_TEXTURE_2D, self.texArr[27])
        glBegin(GL_QUADS)
        glNormal3f(-0.5, 0.0, 0.0)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-0.75 + moveX, 0.75 + moveY, -0.5 + moveZ)
        glTexCoord2f(0.0, 1)
        glVertex3f(-0.75 + moveX, -0.75 + moveY, -0.5 + moveZ)
        glTexCoord2f(1, 1)
        glVertex3f(-0.75 + moveX, -0.75 + moveY, 0.5 + moveZ)
        glTexCoord2f(1, 0.0)
        glVertex3f(-0.75 + moveX, 0.75 + moveY, 0.5 + moveZ)
        glEnd()

        # 건물 앞면
        glBindTexture(GL_TEXTURE_2D, self.texArr[27])
        glBegin(GL_QUADS)
        glNormal3f(0.0, -1, 0.0)
        glTexCoord2f(0.0, 1)
        glVertex3f(-0.75 + moveX, -0.75 + moveY, -0.5 + moveZ)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-0.75 + moveX, -0.75 + moveY, 0.5 + moveZ)
        glTexCoord2f(1, 0.0)
        glVertex3f(0.75 + moveX, -0.75 + moveY, 0.5 + moveZ)
        glTexCoord2f(1, 1)
        glVertex3f(0.75 + moveX, -0.75 + moveY, -0.5 + moveZ)
        glEnd()

        # 건물 앞면 맞은 편
        glBindTexture(GL_TEXTURE_2D, self.texArr[27])
        glBegin(GL_QUADS)
        glNormal3f(0.0, 1, 0.0)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-0.75 + moveX, 0.75 + moveY, -0.5 + moveZ)
        glTexCoord2f(0.0, 1)
        glVertex3f(-0.75 + moveX, 0.75 + moveY, 0.5 + moveZ)
        glTexCoord2f(1, 1)
        glVertex3f(0.75 + moveX, 0.75 + moveY, 0.5 + moveZ)
        glTexCoord2f(1, 0.0)
        glVertex3f(0.75 + moveX, 0.75 + moveY, -0.5 + moveZ)
        glEnd()

    def draw(self):
        #glTranslate(10,0,0)
        self.firstBuilding(18,6,2.5)

