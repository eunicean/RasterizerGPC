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

rend.glLoadModel("P2.obj", 
                 translate=(width/2,height/4,0), 
                 rotate= (0,180,0),
                 scale=(500,500,500))

rend.glRender()

# triangle = [(100,100),(450,180),(250,500)]

# rend.glTriangle_bc(triangle[0],triangle[1],triangle[2])

rend.glFinish("output.bmp")