from SimCamera import *
from Board import *
from Dice import *
from Character import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image

class GameManager():
    """게임을 관리하는 클래스"""
    def __init__(self):
        self.clickX = 0
        self.clickY = 0
        self.board = []
        self.current_turn = 0
        self.camera = Camera()
        self.player = []
        # 각 플레이어의 턴을 스테이지로 나눠서 처리
        # 주사위 굴리기전, 이동애니메이션(시점변경), 이동후액션(시점복귀)
        self.stage = 0

    def gameInit(self):
        # make game board 0~19
        self.board.append(Board(0, 1, "정문"))
        self.board.append(Board(1, 0, "대학본부"))
        self.board.append(Board(2, 0, "대학본부"))

        # player setting
        for player_no in range(4):
            self.player.append(Player(player_no))

    def display(self):
        pass

    def GLInit(self):
        # clear color setting
        glClearColor(0, 0, 0, 1)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)

    def gameStart(self):
        glutInit()
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(1024, 1024)
        glutInitWindowPosition(100, 100)
        glutCreateWindow(b"Burumarble!")
        self.GLInit()
        glutDisplayFunc(self.display)
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

