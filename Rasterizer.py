from gl import Renderer,V2,V3,color
from obj import Obj
import shaders
import random


def drawPoly(poligon):
    i = 0
    while (i+1<len(poligon)):
        rend.glLine(poligon[i],poligon[i+1])
        if i == len(poligon) - 2:
            rend.glLine(poligon[i+1],poligon[0])
        i+= 1 

width = 920
height = 480

rend = Renderer(width,height)

Poligon1 = [V2(165, 380), V2(185, 360),
            V2(180, 330), V2(207, 345), 
            V2(233, 330), V2(230, 360), 
            V2(250, 380), V2(220, 385), 
            V2(205, 410), V2(193, 383)]

Poligon2 = [V2(321, 335), V2(288, 286), 
            V2(339, 251), V2(374, 302)]

Poligon3 = [V2(377, 249), V2(411, 197), V2(436, 249)]

Poligon4 = [V2(413, 177), V2(448, 159), 
            V2(502, 88), V2(553, 53), 
            V2(535, 36), V2(676, 37), 
            V2(660, 52), V2(750, 145), 
            V2(761, 179), V2(672, 192), 
            V2(659, 214), V2(615, 214), 
            V2(632, 230), V2(580, 230), 
            V2(597, 215), V2(552, 214), 
            V2(517, 144), V2(466, 180)]

Poligon5 = [V2(682, 175), V2(708, 120), 
            V2(735, 148), V2(739, 170)]

# i = 0
# while (i+1<len(Poligon1)):
#     rend.glLine(Poligon1[i],Poligon1[i+1])
#     if i == len(Poligon1) - 2:
#         rend.glLine(Poligon1[i+1],Poligon1[0])
#     i+= 1 

drawPoly(Poligon1)
drawPoly(Poligon2)
drawPoly(Poligon3)
drawPoly(Poligon4)
drawPoly(Poligon5)


rend.glFinish("output.bmp")