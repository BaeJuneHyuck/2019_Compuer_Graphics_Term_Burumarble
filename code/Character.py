from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time


class Character():
    """ 플레이어가 가지고 있는 게임말 """

    def __init__(self, type, player):
        self.pos = 0
        self.x, self.y = self.getCord(0)
        self.nextx, self.nexty, self.movex, self.movey = 0, 0, 0, 0
        self.type = type
        self.player = player
        self.color = [0.99, 0.65, 0.01, 0.4, 0.4, 1.0, 0, 0.6, 0, 1.0, 0.4, 0.4]

        self.direction = 0

        # obj 파일 정보
        self.vertices = []
        self.normals = []
        self.texcoords = []
        self.faces = []
        self.gl_list = None
        self.load()

        # 이동 애니메이션 관련 정보
        self.nextmove = 0  # 주사위값을 받고 아직 nextmove만큼 이동해함
        self.moving = False
        self.animation = 0

        # 플레이어별로 캐릭터가 겹치지 않게 약간씩 다른위치로 이동
        self.coordinate_fix = [0, 0, 0]
        if player == 0:
            self.coordinate_fix = [-1.2, -0.5, 1.5]
        elif player == 1:
            self.coordinate_fix = [1.0, -0.5, 1.5]
        elif player == 2:
            self.coordinate_fix = [-1.2, 1.2, 1.5]
        elif player == 3:
            self.coordinate_fix = [1.0, 1.2, 1.5]

    def load(self):
        path = "src/char_human.obj"
        for line in open(path, "r"):
            if line.startswith('#'): continue
            values = line.split()
            if not values: continue
            if values[0] == 'v':
                v = list(map(float, values[1:4]))
                v = v[0] / 7, v[2] / 7, v[1] / 7
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
                self.faces.append((face, norms, texcoords,))

    def draw(self):
        if (self.nextmove > 0 and self.animation == 0):  # 애니메이션 재생(한칸 이동)이 끝낫지만 아직 더 이동해야한다면
            self.pos = (self.pos + 1) % 16  # pos 을 증가시키고 mov 감소
            self.nextmove -= 1
            self.animation = 1  # 다음 한칸을 이동하는 애니메이션 시작
            self.nextx, self.nexty = self.getCord(self.pos)  # 다음 가야할 좌표를 설정
            self.movex = self.nextx - self.x  # 다음좌표 - 현재좌표 : 이동해야할 거리
            self.movey = self.nexty - self.y

        elif (self.moving == True and self.animation > 0):  # 이동해야할 거리를 10번 나눠서 부드럽게 전진
            self.x = self.x + self.movex * 0.1
            self.y = self.y + self.movey * 0.1
            self.animation += 1
            if (self.animation == 10):  # 10번 이동햇으면
                self.animation = 0  # 한칸이동하는 애니메이션 종료
        elif (self.moving == True and self.nextmove == 0):  # 남은 이동거리가 0 이면 이동 종료
            self.animation = 0  # 애니메이션 종료
            self.moving = False  # 이동 종료

        glPushMatrix()
        glTranslatef(self.x, self.y, 0)
        glTranslatef(self.coordinate_fix[0], self.coordinate_fix[1], self.coordinate_fix[2])

        if self.direction == 1 or self.direction == 3:
            glRotatef(90, 1.0, 0, 0.0)
            glRotatef(90, 0.0, 1.0, 0.0)
        else:
            glRotatef(90, 1.0, 0, 0.0)
        num = 0
        for face in self.faces:
            glBegin(GL_POLYGON)
            vertices, normals, __ = face
            total_vertice = range(len(vertices))
            num += 1
            if num < 10:
                glColor3f(self.color[self.player * 3], self.color[self.player * 3 + 1], self.color[self.player * 3 + 2])
            else:
                glColor3f(1.0, 0.8, 0.6)
            for i in total_vertice:
                glVertex3fv(self.vertices[vertices[i] - 1])
            glEnd()
        glPopMatrix()
        glColor3f(1.0, 1.0, 1.0)

        glutPostRedisplay()

    def getCord(self, pos):
        x = 0
        y = 0
        if (pos >= 0 and pos < 5):
            x = (pos + 0.5) * 4
            y = 2
            self.direction = 0

        if (pos >= 5 and pos < 9):
            x = 18
            y = (pos - 3.5) * 4
            self.direction = 1
        if (pos >= 9 and pos < 13):
            x = 20 - (pos - 7.5) * 4
            y = 18
            self.direction = 2
        if (pos >= 13 and pos < 16):
            x = 2
            y = 20 - (pos - 11.5) * 4
            self.direction = 3
        print("pos for {} is {}, {}".format(pos, x, y))
        return x, y

    def setmove(self, dice_value):
        print("char{} move{}".format(self.player, dice_value))
        self.nextmove = dice_value
        self.moving = True
