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


#mediumshot
# rend.glLookAt(camPos=(0,0,0),
#               eyePos=(0,0,-5))

# rend.glLoadModel(filename="model.obj",
#                  textureName= "model.bmp",
#                  translate=(0,0,-5), 
#                  rotate= (0,0,0),
#                  scale=(1.5,1.5,1.5))

# rend.glRender()
# rend.glFinish("./results/MediumShot.bmp")

#lowangle
# rend.glLookAt(camPos=(0,-3,0),
#               eyePos=(0,0,-5))

# rend.glLoadModel(filename="model.obj",
#                  textureName= "model.bmp",
#                  translate=(0,0,-5), 
#                  rotate= (0,0,0),
#                  scale=(1.5,1.5,1.5))

# rend.glRender()
# rend.glFinish("./results/LowShot.bmp")

#highangle
# rend.glLookAt(camPos=(0,4,0),
#               eyePos=(0,0,-5))

# rend.glLoadModel(filename="model.obj",
#                  textureName= "model.bmp",
#                  translate=(0,0,-5), 
#                  rotate= (0,0,0),
#                  scale=(1.5,1.5,1.5))

# rend.glRender()
# rend.glFinish("./results/HighShot.bmp")

#dutchangle
rend.glCamMatrix(translate=(0,-2,0),
                    rotate=(0,0,25))
# rend.glLookAt(camPos=(0,-3,0),
#               eyePos=(0,0,-5))

rend.glLoadModel(filename="model.obj",
                 textureName= "model.bmp",
                 translate=(0,-2,-5), 
                 rotate= (0,0,0),
                 scale=(1.5,1.5,1.5))

rend.glRender()
rend.glFinish("./results/DutchShot.bmp")