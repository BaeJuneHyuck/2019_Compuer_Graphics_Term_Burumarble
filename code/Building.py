from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time

class Building():
    """ 플레이어가 가지고 있는 건물 """
    def __init__(self, pos, player):
        self.pos = pos
        self. player = player
        self.color = [0.6, 0.6, 0.2, 0.4, 0.4, 1.0, 0,0.6, 0, 1.0, 0.4, 0.4]

    def draw(self):
        glPushMatrix()
        x,y = self.getCord()
        glTranslatef(x,y,0)
        glRotatef(90, 1.0, 0, 0.0)

        glColor3f(self.color[self.player * 3] , self.color[self.player * 3 + 1], self.color[self.player * 3 + 2])

        # 빌딩 그리기

        glPopMatrix()
        glColor3f(1.0, 1.0 ,1.0)

    def getCord(self):
        x = 0
        y = 0
        if (self.pos >= 0 and self.pos < 5):
            x = (self.pos + 0.5) * 4
            y = 2

        if (self.pos >= 5 and self.pos < 9):
            x = 18
            y = (self.pos - 3.5) * 4

        if (self.pos >= 9 and self.pos < 13):
            x = (self.pos - 7.5) * 16
            y = 18

        if (self.pos >= 13 and self.pos < 16):
            x = 2
            y = (self.pos - 11.5) * 16
        return x,y

    def building_animation(self, dice_value):
        print("char{} move{}".format(self.player, dice_value))
        self.moving = True

        while(dice_value != 0 ):
            print("move once")
            self.pos += 1
            dice_value -=1
            glutPostRedisplay()

        self.moving = False

