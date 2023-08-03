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
rend.fragmentShader = shaders.fragmentShader

rend.glLoadModel(filename="model.obj",
                 textureName= "model.bmp",
                 translate=(width/4,height/4,0), 
                 rotate= (0,270,0),
                 scale=(350,350,350))

rend.glLoadModel(filename="model.obj",
                 textureName= "model.bmp",
                 translate=(width/4,3*(height/4),0), 
                 rotate= (0,90,0),
                 scale=(350,350,350))

rend.glLoadModel(filename="model.obj",
                 textureName= "model.bmp",
                 translate=(3*(width/4), 3*(height/4), 0), 
                 rotate= (0,0,0),
                 scale=(350,350,350))

rend.glLoadModel(filename="model.obj",
                 textureName= "model.bmp",
                 translate=(3*(width/4),height/4,0), 
                 rotate= (0,180,0),
                 scale=(350,350,350))

rend.glRender()

rend.glFinish("output.bmp")