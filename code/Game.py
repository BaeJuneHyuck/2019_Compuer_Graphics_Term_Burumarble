from SimCamera import *
from Board import *
from Dice import *
from PlayState import *
from Character import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import numpy as np
from PIL import Image


class GameManager():
    """게임을 관리하는 클래스"""

    def __init__(self):
        self.prev_click_x = 0
        self.prev_click_y = 0
        self.board = []
        self.dice = None
        self.current_turn = 0
        self.camera = Camera()
        self.player = []
        self.characters = []
        self.char_moved = False
        self.x_resolution = 800
        self.y_resolution = 800

        # 각 플레이어의 턴을 스테이지로 나눠서 처리
        # 주사위 굴리기전, 이동애니메이션(시점변경), 이동후액션(시점복귀)
        self.stage = 0

    def loadImage(self, imageName):
        img = Image.open(imageName)
        img_data = np.array(list(img.getdata()), np.uint8)
        return img.size[0], img.size[1], img_data

    def setTexture(self, texArr, idx, fileName, option):
        glBindTexture(GL_TEXTURE_2D, texArr[idx])
        imgW, imgH, myImage = self.loadImage(fileName)
        # print(imgW, imgH, myImage)

        # texture image 생성
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB,
                     imgW, imgH, 0, option,
                     GL_UNSIGNED_BYTE, myImage)

        # texture 매핑 옵션 설정
        glTexParameterf(GL_TEXTURE_2D,
                        GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D,
                        GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D,
                        GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D,
                        GL_TEXTURE_MIN_FILTER, GL_NEAREST)

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

        # draw dice
        self.dice.draw()

        # draw character
        glDisable(GL_TEXTURE_2D)
        if self.char_moved:
            for index in range(4):
                self.characters[index].draw()
        glEnable(GL_TEXTURE_2D)

        # draw map
        for index in range(16):
            self.board[index].draw()
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
        glDisable(GL_BLEND)
        print("loading textures...")

        # 텍스처 로드
        # 0 ~ 15 각 맵의 그림 텍스쳐
        # 16 나무 텍스처
        # 17 굴리기 버튼 텍스쳐
        # 18~ 23 : 주사위 1~6까지
        self.texArr = glGenTextures(25)
        for i in range(0, 16):
            if i <= 9:
                path = "texture/board_0" + str(i) + ".jpg"
            else:
                path = "texture/board_" + str(i) + ".jpg"
            self.setTexture(self.texArr, i, path, GL_RGB)
        self.setTexture(self.texArr, 16, "texture/wood.jpg", GL_RGB)
        self.setTexture(self.texArr, 17, "texture/dice_roll.jpg", GL_RGB)
        for i in range(18, 24):
            path = "texture/dice_" + str(i-17) + ".jpg"
            self.setTexture(self.texArr, i, path, GL_RGB)
        # state screen
        self.state = PlayState(self.camera, self.x_resolution, self.y_resolution, self.texArr)

    def gameInit(self):
        # make game board 0~16
        self.board.append(Board(0, 1, "정문", self.texArr))
        self.board.append(Board(1, 0, "넉터", self.texArr))
        self.board.append(Board(2, 0, "제6 공학관", self.texArr))
        self.board.append(Board(3, 0, "인문관", self.texArr))
        self.board.append(Board(4, 0, "대학본부", self.texArr))
        self.board.append(Board(5, 0, "제2 공학관", self.texArr))
        self.board.append(Board(6, 0, "문창회관", self.texArr))
        self.board.append(Board(7, 0, "자연대 연구실험동", self.texArr))
        self.board.append(Board(8, 0, "새벽벌도서관", self.texArr))
        self.board.append(Board(9, 0, "사회관", self.texArr))
        self.board.append(Board(10, 0, "금정회관", self.texArr))
        self.board.append(Board(11, 0, "법학관", self.texArr))
        self.board.append(Board(12, 0, "테니스장", self.texArr))
        self.board.append(Board(13, 0, "제 1도서관", self.texArr))
        self.board.append(Board(14, 0, "무지개문", self.texArr))
        self.board.append(Board(15, 0, "건설관", self.texArr))

        self.dice = Dice(self.texArr)

        # player setting
        for player_no in range(4):
            self.player.append(Player(player_no))

        # character setting
        for player_no in range(4):
            self.characters.append(Character(player_no, player_no))

    def gameStart(self):
        glutInit()
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
                self.dice.roll()
                self.char_moved = not self.char_moved

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
