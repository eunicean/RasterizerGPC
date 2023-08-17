from gl import Renderer,V2,V3,color
from obj import Obj
import shaders
import random


width = 1920
height = 1920

# width = 500
# height = 620

rend = Renderer(width,height)

rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.gouradShader

rend.glClearColor(0.5,0.5,0.7)
rend.glClear()

rend.glLoadModel(filename="model.obj",
                 textureName= "model.bmp",
                 translate=(0,0,-5), 
                 rotate= (0,0,0),
                 scale=(1.5,1.5,1.5))

rend.glRender()
rend.glFinish("./results/output.bmp")

#56 min class 04-08 gpc