from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Character():
    """ 플레이어가 가지고 있는 게임말 """
    def __init__(self, type, player):
        self.pos = 0
        self.type = type
        self. player = player
        self.vertices = []
        self.normals = []
        self.texcoords = []
        self.faces = []
        self.gl_list = None
        self.load()
        self.coordinate_fix = [0,0,3]

    def load(self):
        if self.type == 0:
            path = "src/char_Bishop.obj"
        elif self.type == 1:
            path = "src/char_King.obj"
        elif self.type == 2:
            path ="src/char_Knight.obj"
        else:
            path="src/char_Queen.obj"

        for line in open(path, "r"):
            if line.startswith('#'): continue
            values = line.split()
            if not values: continue
            if values[0] == 'v':
                v = list(map(float, values[1:4]))
                v = v[0], v[2], v[1]
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
        glTranslatef(self.coordinate_fix[0],self.coordinate_fix[1],self.coordinate_fix[2])
        glRotatef(90, 1.0, 0, 0.0)

        glColor3f(1.0, 0.5, 0.3)
        for face in self.faces:
            glBegin(GL_POLYGON)
            vertices, normals, __ = face
            total_vertice = range(len(vertices))
            for i in total_vertice:
                '''
                if normals[i] > 0:
                    glNormal3fv(self.normals[normals[i] - 1])
                '''
                glVertex3fv(self.vertices[vertices[i] - 1])
            glEnd()
        glPopMatrix()

        glColor3f(1.0, 1.0 ,1.0)


