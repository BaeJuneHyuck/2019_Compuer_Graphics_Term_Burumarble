from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

class Building():
    vertexQuadArray = [(4.0, 4.0, 4.0), (4, -4, 4), (-4, -4, 4), (-4, 4, 4), (4, 4, -4), (4, -4, -4), (-4, -4, -4),
                       (-4, 4, -4)]
    vertexTraArray = [(5, 5, 5), (-5, 5, 5), (-5, 5, -5), (5, 5, -5), (0, 5, 0)]
    def __init__(self, pos, texArr):
        self.pos = pos
        self.player = -1
        self.texArr = texArr
        self.z = 8
        self.color = [0.6, 0.6, 0.2, 0.4, 0.4, 1.0, 0, 0.6, 0, 1.0, 0.4, 0.4]
        self.direction = 0
        self.isSet = False
        if (pos >= 0 and pos < 5):
            self.x = (pos + 0.5) * 4
            self.y = 2
            self.direction = 0

        if (pos >= 5 and pos < 9):
            self.x = 18
            self.y = (pos - 3.5) * 4
            self.direction = 1
        if (pos >= 9 and pos < 13):
            self.x = 20 - (pos - 7.5) * 4
            self.y = 18
            self.direction = 2
        if (pos >= 13 and pos < 16):
            self.x = 2
            self.y = 20 - (pos - 11.5) * 4
            self.direction = 3

    def Set(self,player):
        self.player=player
        self.isSet = True

    # 1번 땅이 6,2,2.5 이다.
    # moveZ 에 2.5를 넣으면 딱 땅바닥에 안착
    # moveX 엥 +4 씩 하면 됨
    # moveY 도 + 4 씩 하면 됨
    def firstBuilding(self, moveX, moveY, moveZ):
        # 정면 왼쪽 삼각형
        glDisable(GL_TEXTURE_2D)
        glBegin(GL_TRIANGLES)
        glColor3f(self.color[self.player * 3], self.color[self.player * 3 + 1], self.color[self.player * 3 + 2])
        glVertex3f(-1 + moveX, -1 + moveY, 0.5 + moveZ)
        glVertex3f(-1 + moveX, 1 + moveY, 0.5 + moveZ)
        glVertex3f(moveX, moveY, 2 + moveZ)
        if(self.z > 2.5):
            self.z -= 0.25
        glEnd()

        # 정면 삼각형

        glBegin(GL_TRIANGLES)
        glVertex3f(1 + moveX, -1 + moveY, 0.5 + moveZ)
        glVertex3f(-1 + moveX, -1 + moveY, 0.5 + moveZ)
        glVertex3f(moveX, moveY, 2 + moveZ)
        glEnd()

        # 정면 오른쪽 삼각형
        glBegin(GL_TRIANGLES)
        glVertex3f(1 + moveX, 1 + moveY, 0.5 + moveZ)
        glVertex3f(1 + moveX, -1 + moveY, 0.5 + moveZ)
        glVertex3f(moveX, moveY, 2 + moveZ)
        glEnd()

        # 정면 맞은편 삼각형
        glBegin(GL_TRIANGLES)
        glVertex3f(-1 + moveX, 1 + moveY, 0.5 + moveZ)
        glVertex3f(1 + moveX, 1 + moveY, 0.5 + moveZ)
        glVertex3f(moveX, moveY, 2 + moveZ)
        glColor3f(1.0, 1.0, 1.0)
        glEnd()
        glEnable(GL_TEXTURE_2D)

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
        if self.player == -1: # 아직 소유주가 없다면
            pass
        else:
            self.firstBuilding(self.x,self.y,self.z) # 그릴필요없지

