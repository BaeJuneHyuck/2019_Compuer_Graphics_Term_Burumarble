from SimCamera import *
from Board import *
from Dice import *
from Play_State import *
from Character import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image

X_RESOLUTION = 800
Y_RESOLUTION = 800

class GameManager():
    """게임을 관리하는 클래스"""
    def __init__(self):
        self.clickX = 0
        self.clickY = 0
        self.board = []
        self.current_turn = 0
        self.camera = Camera()
        self.player = []
        self.state = Play_State()
        # 각 플레이어의 턴을 스테이지로 나눠서 처리
        # 주사위 굴리기전, 이동애니메이션(시점변경), 이동후액션(시점복귀)
        self.stage = 0

    def gameInit(self):
        # make game board 0~16
        self.board.append(Board(0, 1, "정문"))
        self.board.append(Board(1, 0, "넉터"))
        self.board.append(Board(2, 0, "제6 공학관"))
        self.board.append(Board(3, 0, "인문관"))
        self.board.append(Board(4, 0, "대학본부"))
        self.board.append(Board(5, 0, "제2 공학관"))
        self.board.append(Board(6, 0, "문창회관"))
        self.board.append(Board(7, 0, "자연대 연구실험동"))
        self.board.append(Board(8, 0, "새벽벌도서관"))
        self.board.append(Board(9, 0, "사회관"))
        self.board.append(Board(10, 0, "금정회관"))
        self.board.append(Board(11, 0, "법학관"))
        self.board.append(Board(12, 0, "테니스장"))
        self.board.append(Board(13, 0, "제 1도서관"))
        self.board.append(Board(14, 0, "무지개문"))
        self.board.append(Board(15, 0, "건설관"))

        # player setting
        for player_no in range(4):
            self.player.append(Player(player_no))

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60.0, 1.0, 0.1, 1000)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()



        Play_State.State_Init(self)


    def GLInit(self):
        # clear color setting
        glClearColor(0, 0, 1, 0)
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)

    def gameStart(self):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(X_RESOLUTION, Y_RESOLUTION)
        glutInitWindowPosition(100, 100)
        glutCreateWindow(b"Burumarble!")
        self.GLInit()
        self.gameInit()
        glutDisplayFunc(self.display)
        # glutIdleFunc(self.display)
        glutMouseFunc(self.mouseClick)
        glutMainLoop()

    def mouseClick(self, Button, State, X, Y):
        if Button == GLUT_LEFT_BUTTON and State == GLUT_DOWN:
            self.clickX = X
            self.clickY = Y
            print("click x={}, y={}".format(self.clickX, self.clickY))

    def draw(self):
        glBegin()


    def nextStage(self):
        if self.stage == 0:
            pass
        elif self.stage == 0:
            pass
        elif self.stage == 0:
            pass


class Player():
    def __init__(self, number):
        self.money = 0
        self.number = number

