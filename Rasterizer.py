from gl import Renderer,V2,V3,color
from obj import Obj
import shaders
import random


width = 1920
height = 1080

# width = 500
# height = 620

rend = Renderer(width,height)

rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.fragmentShader

rend.glLoadModel(filename="model.obj",
                 textureName= "model.bmp",
                 translate=(width/2,height/4,0), 
                 rotate= (0,180,0),
                 scale=(300,300,300))



rend.glRender()

rend.glFinish("output.bmp")