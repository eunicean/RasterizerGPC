import meth as metha


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
    texCoords = kwargs["texCoords"]
    texture = kwargs["texture"]

    if texture != None:
        color = texture.getColor(texCoords[0],texCoords[1])
    else:
        color =  (1,1,1)
    return color