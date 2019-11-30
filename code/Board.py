from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Board():
    """ 게임이 이뤄질 보드 """
    def __init__(self, pos, type,  text):
        super().__init__()
        # 시작지점 0 부터 끝지점 19 까지 순서대로 pos 번호 부여
        self.pos = pos

        # type 0 일반적인 땅(건물 구입가능한)
        # type 1 특수한 지역,  따로 처리
        self.type = 0
        self.owner = -1

        # 건물이 지어질 경우
        self.building = 0

        # 설명용 텍스트 설정
        self.text = text

        # pos에 맞게 x,y 위치 설정 하기
        # x = pos
        # y = 5-pos....

    def draw(self):
        glBegin(GL_QUADS)

