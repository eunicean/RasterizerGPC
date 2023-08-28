from gl import Renderer,V2,V3,color, Model
from obj import Obj
import shaders
import random


width = 480
height = 270

# width = 500
# height = 620

rend = Renderer(width,height)

# rend.glViewPort(width/4,height/4,width/2,height/2)

rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.gouradShader

rend.glClearColor(0.5,0.5,0.7)
rend.glBackgroundTexture("resources/texture/picnic.bmp")
rend.glclearBackground()

rend.glLookAt(camPos=(0,0,-10),
              eyePos=(0,0,-5))

# #cargamos los modelos
model1 = Model("resources/model/PenguinBaseMesh.obj",
              translate=(0,0,-10),
              rotate= (0,0,0),
              scale=(1,1,1))
model1.LoadTexture("resources/texture/PenguinDiffuseColor1.bmp")
model1.SetShaders(shaders.vertexShader, shaders.pink)

model2 = Model("resources/model/box.obj",
              translate=(1,0,-15),
              rotate= (0,0,0),
              scale=(1,1,1))
model2.LoadTexture("resources/texture/card.bmp")
model2.SetShaders(shaders.vertexShader, shaders.tempshader)

model3 = Model("resources/model/pumpkin.obj",
              translate=(0,0,-20),
              rotate= (0,0,0),
              scale=(1,1,1))
model3.LoadTexture("resources/texture/cloud.bmp")
model3.SetShaders(shaders.vertexShader, shaders.negativeShader)

model4 = Model("resources/model/pumpkin.obj",
              translate=(0,0,-20),
              rotate= (0,0,0),
              scale=(1,1,1))
model4.LoadTexture("resources/texture/cloud.bmp")
model4.SetShaders(shaders.vertexShader, shaders.gouradShader)

model5 = Model("resources/model/PenguinBaseMesh.obj",
              translate=(3,0,-5),
              rotate= (0,0,0),
              scale=(1,1,1))
model5.LoadTexture("resources/texture/PenguinDiffuseColor1.bmp")
model5.SetShaders(shaders.vertexShader, shaders.fatShader)

rend.glAddModel(model1)
rend.glAddModel(model2)
rend.glAddModel(model3)
rend.glAddModel(model4)
rend.glAddModel(model5)

rend.glRender()
rend.glFinish("./results/p1.bmp")

#56 min class 04-08 gpc