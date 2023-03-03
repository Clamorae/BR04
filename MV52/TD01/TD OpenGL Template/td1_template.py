# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 10:24:40 2020

@author: LAURI
"""


import random
from opengl_fcts import *
import math


class RainbowCube(Object3D):
    def __init__(self):
        super().__init__()

        n = 5

        vertices = polygon(n)

        indices = []

        for i in range(n+1):
            indices.append(i)
            print(indices)
        indices.append(1)
        print(indices)

        primitives = [
                (GL_TRIANGLE_FAN,indices)
                ]

        self.Shader=ColorPositionShader(vertices,primitives)


    def updateTRSMatrices(self):
        time=glfw.get_time()
        rot_x = pyrr.Matrix44.from_x_rotation(0.5 * time)
        rot_y = pyrr.Matrix44.from_y_rotation(0.8 * time)

        self.R=np.matmul(rot_x,rot_y)

def polygon(poly):
    coordinate = [(0,10,0)]
    tab = []

    diff = 2*math.pi / poly
    for i in range(poly):
        coordinate.append((math.cos(diff * i),0,math.sin(diff * i)))
    print(coordinate)
    coordinate = tuplesToGlArray(coordinate)
    return coordinate

    

def tuplesToGlArray(vertices):
    out = []
    for vertice in vertices:
        for coord in vertice:
            out.append(coord)
        for _ in range(0,3):
            out.append(random.random())
    return out

def main():
    window=Window(1024,768,"TD - Template Exercice 1")

    if not window.Window:
        return

    window.initViewMatrix(eye=[0,0,5])

    rc=RainbowCube()
    rc.translate((0.0,0.0,0.0))

    objects=[rc]

    window.render( objects )


if __name__ == "__main__":
    main()


