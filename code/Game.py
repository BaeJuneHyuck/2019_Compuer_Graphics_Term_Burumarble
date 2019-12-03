from SimCamera import *
from Board import *
from Dice import *
from PlayState import *
from Character import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image


class GameManager():
    """게임을 관리하는 클래스"""

    def __init__(self):
        self.prev_click_x = 0
        self.prev_click_y = 0
        self.board = []
        self.current_turn = 0
        self.camera = Camera()
        self.player = []
        self.x_resolution = 800
        self.y_resolution = 800

        print("loading textures...")
        self.state = PlayState(self.camera, self.x_resolution, self.y_resolution)
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

        # load textures


    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60.0, 1.0, 0.1, 1000)

        ''' draw game '''
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # draw player state window
        self.state.draw()

        # draw gameboard
        glViewport(0, 0, self.x_resolution, self.y_resolution)
        glPushMatrix()
        self.camera.applyCamera()

        for index in range(16):
            self.board[index].draw()
        self.board[0].drawDice()
        glPopMatrix()
        # double 버퍼 사용, glFlush() 대신 GLUTSwapBuffers()써서 깜빡거림 제거
        glutSwapBuffers()

    def reshape(self, w, h):
        self.x_resolution = w
        self.y_resolution = h
        self.state.setWidthHeight(w, h)
        glViewport(0, 0, w, h);
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

    def GLInit(self):
        # clear color setting
        glClearColor(0, 0, 1, 0)
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)

    def gameStart(self):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(self.x_resolution, self.y_resolution)
        glutInitWindowPosition((glutGet(GLUT_SCREEN_WIDTH) - self.x_resolution) // 2, 0)
        glutCreateWindow(b"Burumarble!")
        self.GLInit()
        self.gameInit()
        glutDisplayFunc(self.display)
        # glutReshapeFunc(self.reshape)
        # glutIdleFunc(self.)
        glutMouseFunc(self.mouseClick)
        glutMouseWheelFunc(self.mouseWheel)
        glutMotionFunc(self.mouseMove)
        glutMainLoop()

    def mouseClick(self, button, state, x, y):
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            self.prev_click_x = x
            self.prev_click_y = y
            print("click x={}, y={}".format(x, y))
            if x >= 340 and x < 460 and y >= 720:
                print("button click!!")

    def mouseMove(self, current_x, current_y):
        dx = self.prev_click_x - current_x
        dy = self.prev_click_y - current_y
        if dx >= 5 or dx <= -5:
            self.camera.rotate(dx, dy)
            glutPostRedisplay()
        self.prev_click_x = current_x
        self.prev_click_y = current_y

    def mouseWheel(self, button, state, x, y):
        if state == 1:
            self.camera.zoomIn()
        elif state == -1:
            self.camera.zoomOut()
        glutPostRedisplay()

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
