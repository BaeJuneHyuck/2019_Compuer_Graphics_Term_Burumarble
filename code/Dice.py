from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Dice():
    """ 주사위 굴리기(stage 1)에서 보여질 주사위 """
    def __init__(self, textures):
        self.texArr = textures
        self.value = 1
        self.z = 0.0
        self.rotation = 0.0

    def draw(self):
        # 높이 조절하는부분을 쓰레드로 따로 빼거나 타이머 적용해서 gutPostRedisplay 넣어서 바로바로 보이도록해야함
        if self.z >= 0:
            self.z -= 0.3
            self.rotation -= 5

        glPushMatrix()
        glTranslatef(0, 0, self.z)
        glRotatef(self.rotation, 1.0, 1.0, 0.0)
        glBindTexture(GL_TEXTURE_2D, self.texArr[0])
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

        glBindTexture(GL_TEXTURE_2D, self.texArr[1])
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

        glBindTexture(GL_TEXTURE_2D, self.texArr[2])
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

        glBindTexture(GL_TEXTURE_2D, self.texArr[3])
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

        glBindTexture(GL_TEXTURE_2D, self.texArr[4])
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

        glBindTexture(GL_TEXTURE_2D, self.texArr[5])
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
        glutPostRedisplay


    def roll(self):
        self.z += 3.0
        self.rotation += 50
