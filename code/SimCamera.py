from OpenGL.GL import *
from OpenGL.GLU import *
from math import *

import numpy as np


def rotate(v, angle, axis) :
    c = cos(angle)
    s = sin(angle)
    C = 1-c
    x,y,z = axis[0], axis[1], axis[2]

    R1 = np.array([x*x*C+c, x*y*C - z*s, x*z*C+y*s])
    R2 = np.array([y*x*C+z*s, y*y*C+c, y*z*C-x*s])
    R3 = np.array([z*x*C-y*s, z*y*C+x*s, z*z*C+c])

    return np.array([R1.dot(v), R2.dot(v), R3.dot(v)])


class Camera :

    def __init__(self):  #constructor
        self.loc = np.array([0.0, 0.0,  0.0])
        self.tar = np.array([0.0, 0.0, 0.0])
        self.up  = np.array([0.0, 1.0,  0.0])
        self.right = np.array([1.0, 0.0, 0.0])
        self.dir = np.array([0.0, 0.0, -1.0])
        self.asp = 1.0
        self.fov = 60
        self.near= 0.1
        self.far = 100.0

    def setCameraLoc(self, loc):
        self.loc = loc
        self.tar = self.loc + self.dir

    def setCamera(self, loc, tar, up):
        self.loc, self.tar, self.up = loc, tar, up

        self.dir = self.tar - self.loc
        l = np.linalg.norm(self.dir)
        if l > 0.0 :
            self.dir = self.dir / l

        l = np.linalg.norm(self.up)
        if l > 0.0 :
            self.up = self.up / l

        self.right = np.cross(self.dir, self.up)


    def setLens(self, fov, asp, near, far):
        self.fov, self.asp, self.near, self.far = fov, asp, near, far

    def applyCamera(self):
        gluLookAt(self.loc[0], self.loc[1], self.loc[2],
                  self.tar[0], self.tar[1], self.tar[2],
                  self.up [0], self.up [1], self.up [2])

    def applyLens(self):
        gluPerspective(self.fov, self.asp, self.near, self.far)


    def moveForward(self, step=1.0):
        self.tar += self.dir*step
        self.loc += self.dir*step


    def moveBackward(self, step=1.0):
        self.moveForward(-step)

    def moveForward(self, step=1.0):
        self.tar += self.dir * step
        self.loc += self.dir * step

    def moveBackward(self, step=1.0):
        self.moveForward(-step)

    def moveRight(self, step=1.0):
        self.tar += self.right * step
        self.loc += self.right * step

    def moveLeft(self, step=1.0):
        self.moveRight(-step)

    def zoomIn(self):
        self.fov *= 0.95

    def zoomOut(self):
        self.fov *= 1.05

    def turnRight(self, angle=0.01):
        self.right = rotate(self.right, -angle, self.up)
        self.dir = rotate(self.dir, -angle, self.up)
        self.tar = self.loc + self.dir

    def turnLeft(self, angle=0.01):
        self.turnRight(-angle)

    def turnUp(self, angle=0.01):
        self.up = rotate(self.up, angle, self.right)
        self.dir = rotate(self.dir, angle, self.right)
        self.tar = self.loc + self.dir

    def turnDown(self, angle=0.01):
        self.turnUp(-angle)
