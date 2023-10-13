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

# # #cargamos los modelos
model1 = Model("./resources/model/PenguinBaseMesh.obj",
              translate=(-1,0,-15),
              rotate= (180,0,0),
              scale=(1.5,1.5,1.5))
model1.LoadTexture("./resources/texture/PenguinDiffuseColor1.bmp")
model1.SetShaders(shaders.vertexShader, shaders.pink)

model2 = Model("./resources/models/notepad.obj",
              translate=(1,0.75,-15),
              rotate= (20,60,180),
              scale=(0.05,0.05,0.05))
model2.LoadTexture("./resources/textures/notepad.bmp")
model2.SetShaders(shaders.vertexShader, shaders.tempshader)

model3 = Model("./resources/models/vpot.obj",
              translate=(-0.85,0.55,-17),
              rotate= (180,0,0),
              scale=(0.05,0.05,0.05))
model3.LoadTexture("./resources/textures/terracota.bmp")
model3.SetShaders(shaders.vertexShader, shaders.negativeShader)

model4 = Model("./resources/models/hand.obj",
              translate=(-0.75,0.55,-18),
              rotate= (30,50,0),
              scale=(0.10,0.10,0.10))
model4.LoadTexture("./resources/textures/skin.bmp")
model4.SetShaders(shaders.vertexShader, shaders.gouradShader)

model5 = Model("./resources/model/PenguinBaseMesh.obj",
              translate=(2,1.15,-15),
              rotate= (180,-20,0),
              scale=(1.5,1.5,1.5))
model5.LoadTexture("./resources/texture/PenguinDiffuseColor1.bmp")
model5.SetShaders(shaders.vertexShader, shaders.distortionshader)


rend.glAddModel(model1)
rend.glAddModel(model2)
rend.glAddModel(model3)
rend.glAddModel(model4)
rend.glAddModel(model5)

rend.glRender()
rend.glFinish("./results/p1.bmp")

