from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from Game import *


class Play_State():

    def __init__(self):
        pass


    def Picture_Space(self):
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

    def Draw_Background(self):
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


    #"플레이어 스테이터스 보여주는 화면"
    def State_Init(self):

        #오른쪽 상단 스테이터스
        glViewport(0, 0, 200, 100)
        glPushMatrix()
        gluLookAt(0, 0, 1, 0, 0, 0, 0, 1, 0)
        self.state.Draw_Background()
        self.state.Picture_Space()
        glPopMatrix()

        #오른쪽 하단 스테이터스
        glViewport(0, 700, 200, 100)
        glPushMatrix()
        gluLookAt(0, 0, 50, 0, 0, 0, 0, 1, 0)
        self.state.Draw_Background()
        self.state.Picture_Space()
        glPopMatrix()

        #왼쪽 하단 스테이터스
        glViewport(600, 0, 200, 100)
        glPushMatrix()
        gluLookAt(0, 0, 1, 0, 0, 0, 0, 1, 0)
        self.state.Draw_Background()
        self.state.Picture_Space()
        glPopMatrix()

        #왼쪽 상단 스테이터스
        glViewport(600, 700, 200, 100)
        glPushMatrix()
        gluLookAt(0, 0, 1, 0, 0, 0, 0, 1, 0)
        self.state.Draw_Background()
        self.state.Picture_Space()
        glPopMatrix()


        glViewport(0, 0, 800, 800)
        glPushMatrix()
        gluLookAt(15, -15, 20, 10, 10, 0, 0, 0, 1)
        #gluLookAt(30, -35, 25, 10, 10, 0, 0, 0, 1)

        for index in range(16):
            self.board[index].draw()

        glPopMatrix()
