import meth as metha

def vertexShader(vertex, **kwargs):
    modelMatrix = kwargs["modelMatrix"]
    viewMatrix = kwargs["viewMatrix"]
    projectionMatrix = kwargs["projectionMatrix"]
    vpMatrix = kwargs["vpMatrix"]

    vt = [vertex[0],
          vertex[1],
          vertex[2],
          1]
    
    vt = metha.multiplyMatrixVector(vt,metha.multiplymatrix(metha.multiplymatrix(metha.multiplymatrix(vpMatrix,projectionMatrix),viewMatrix),modelMatrix))


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

def flatShader(**kwargs):
    dLight = kwargs["dLight"]
    normal = kwargs["triangleNormal"]

    dLight = list(dLight)
    for e in range(len(dLight)):
        dLight[e] = -1 * dLight[e]

    intensity = metha.dotProd(normal,dLight)

    color = (intensity,intensity,intensity)

    if intensity > 0:
        return color
    else:
        return (0,0,0)