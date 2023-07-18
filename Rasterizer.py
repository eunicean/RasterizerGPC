from gl import Renderer,V3,V3,color
from obj import Obj
import shaders
import random


width = 1920
height = 1080

rend = Renderer(width,height)

rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.fragmentShader

rend.glLoadModel("P1.obj", 
                 translate=(width/2,height/4,0), 
                 scale=(500,500,500))

rend.glRender()

rend.glFinish("output.bmp")