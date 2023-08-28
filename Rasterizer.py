from gl import Renderer,V2,V3,color, Model
from obj import Obj
import shaders
import random


width = 960
height = 540

# width = 500
# height = 620

rend = Renderer(width,height)

rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.gouradShader

rend.glClearColor(0.5,0.5,0.7)
rend.glClear()

# #cargamos los modelos
model1 = Model("PenguinBaseMesh.obj",
              translate=(0,0,-5),
              rotate= (0,0,0),
              scale=(1.5,1.5,1.5))
model1.LoadTexture("PenguinDiffuseColor1.bmp")
model1.SetShaders(shaders.vertexShader, shaders.gouradShader)



# model3 = Model("PenguinBaseMesh.obj",
#               translate=(3,0,-5),
#               rotate= (0,0,0),
#               scale=(1.5,1.5,1.5))
# model3.LoadTexture("PenguinDiffuseColor1.bmp")
# model3.SetShaders(shaders.vertexShader, shaders.tempshader)


rend.glAddModel(model1)
# rend.glAddModel(model2)
# rend.glAddModel(model3)

rend.glRender()
rend.glFinish("./results/output.bmp")

#56 min class 04-08 gpc