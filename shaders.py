import meth as metha

import random

def vertexShader(vertex, **kwargs):
    modelMatrix = kwargs["modelMatrix"]

    vt = [vertex[0],
          vertex[1],
          vertex[2],
          1]
    
    vt = metha.multiplyMatrixVector(vt, modelMatrix)


    vt = [vt[0]/vt[3],
          vt[1]/vt[3],
          vt[2]/vt[3]]

    return vt

def fragmentShader(**kwargs):
    color = (random.random(),random.random(),random.random())
    return color