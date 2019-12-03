from OpenGL.GL import *
from OpenGL.GLU import *
from math import *
import numpy as np

class Camera:

    def __init__(self):  # constructor
        self.loc_origin = np.array([15.0, -15.0, 20.0])
        self.loc = np.array([15.0, -15.0, 20.0])
        self.tar = np.array([10.0, 10.0, 0.0])
        self.up = np.array([0.0, 0.0, 1.0])
        self.right = np.array([1.0, 0.0, 0.0])
        self.dir = np.array([0.0, 0.0, -1.0])
        self.asp = 1.0
        self.fov = 60
        self.near = 0.1
        self.far = 100.0
        self.zoom = 1.0
        self.angle = 0.0

    def setCameraLoc(self, loc):
        self.loc = loc
        self.tar = self.loc + self.dir

    def setCamera(self, loc, tar, up):
        self.loc, self.tar, self.up = loc, tar, up

        self.dir = self.tar - self.loc
        l = np.linalg.norm(self.dir)
        if l > 0.0:
            self.dir = self.dir / l

        l = np.linalg.norm(self.up)
        if l > 0.0:
            self.up = self.up / l

        self.right = np.cross(self.dir, self.up)

    def setLens(self, fov, asp, near, far):
        self.fov, self.asp, self.near, self.far = fov, asp, near, far

    def applyCamera(self):
        gluLookAt(self.loc[0], self.loc[1], self.loc[2],
                  self.tar[0], self.tar[1], self.tar[2],
                  self.up[0], self.up[1], self.up[2])

    def applyLens(self):
        gluPerspective(self.fov, self.asp, self.near, self.far)

    def zoomIn(self):
        self.zoom = self.zoom - 0.05
        if self.zoom < 0.3:
            self.zoom = 0.3
        self.adjust()

    def zoomOut(self):
        self.zoom = self.zoom + 0.05
        if self.zoom > 2.0:
            self.zoom = 2.0
        self.adjust()

    def rotate(self, dx, dy):
        if dx > 0:
            self.angle = self.angle + 1.0
        elif dx < 0:
            self.angle = self.angle - 1.0
        self.adjust()

    def adjust(self):
        # 회전과 줌인을 한꺼번에 하는식을 드디어 구했다
        self.loc[0] = 5 * cos(radians(self.angle)) + 25 * self.zoom * sin(radians(self.angle)) + 10
        self.loc[1] = 5 * sin(radians(self.angle)) - 25 * self.zoom * cos(radians(self.angle)) + 10
        print(self.zoom)
        self.applyCamera()

    def reset(self):
        self.loc = self.loc_origin
        self.zoom = 1.0
        self.angle = 0.0
        self.applyCamera()
