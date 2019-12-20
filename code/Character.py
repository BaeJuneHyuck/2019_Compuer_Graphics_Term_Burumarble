from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time

class Character():
    """ 플레이어가 가지고 있는 게임말 """
    def __init__(self, type, player):
        self.pos = 0
        self.type = type
        self. player = player
        self.color = [0.6, 0.6, 0.2, 0.4, 0.4, 1.0, 0,0.6, 0, 1.0, 0.4, 0.4]
        self.vertices = []
        self.normals = []
        self.texcoords = []
        self.faces = []
        self.gl_list = None
        self.moving = False
        self.load()
        self.coordinate_fix = [0,0,0]
        if player == 0:
            self.coordinate_fix = [-0.5, -0.5, 1.5]
        elif player == 1:
            self.coordinate_fix = [1.5, -0.5, 1.5]
        elif player == 2:
            self.coordinate_fix = [-0.5, 1.5, 1.5]
        elif player == 3:
            self.coordinate_fix = [1.5, 1.5 , 1.5]

    def load(self):
        path = "src/char_human.obj"
        for line in open(path, "r"):
            if line.startswith('#'): continue
            values = line.split()
            if not values: continue
            if values[0] == 'v':
                v = list(map(float, values[1:4]))
                v = v[0]/5, v[2]/5, v[1]/5
                self.vertices.append(v)
            elif values[0] == 'vn':
                v = list(map(float, values[1:4]))
                v = v[0], v[2], v[1]
                self.normals.append(v)
            elif values[0] in ('usemtl', 'usemat'):
                material = values[1]
            elif values[0] == 'mtllib':
                continue
            elif values[0] == 'f':
                face = []
                texcoords = []
                norms = []
                for v in values[1:]:
                    w = v.split('/')
                    face.append(int(w[0]))
                    if len(w) >= 2 and len(w[1]) > 0:
                        texcoords.append(int(w[1]))
                    else:
                        texcoords.append(0)
                    if len(w) >= 3 and len(w[2]) > 0:
                        norms.append(int(w[2]))
                    else:
                        norms.append(0)
                self.faces.append((face, norms, texcoords, ))

    def draw(self):
        glPushMatrix()
        x,y = self.getCord()
        glTranslatef(x,y,0)
        glTranslatef(self.coordinate_fix[0],self.coordinate_fix[1],self.coordinate_fix[2])
        glRotatef(90, 1.0, 0, 0.0)

        glColor3f(self.color[self.player * 3] , self.color[self.player * 3 + 1], self.color[self.player * 3 + 2])
        for face in self.faces:
            glBegin(GL_POLYGON)
            vertices, normals, __ = face
            total_vertice = range(len(vertices))
            for i in total_vertice:
                glVertex3fv(self.vertices[vertices[i] - 1])
            glEnd()
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

    def move(self, dice_value):
        print("char{} move{}".format(self.player, dice_value))
        self.moving = True

        while(dice_value != 0 ):
            print("move once")
            self.pos += 1
            dice_value -=1
            glutPostRedisplay()

        self.moving = False

