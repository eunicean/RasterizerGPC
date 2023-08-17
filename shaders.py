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
    normal = kwargs["normals"]
    texCoords = kwargs["texCoords"]
    texture = kwargs["texture"]

    b = 1.0
    g = 1.0
    r = 1.0

    if texture != None:
        textureColor = texture.getColor(texCoords[0],texCoords[1])
        b = textureColor[2]
        g = textureColor[1]
        r = textureColor[0]


    dLight = list(dLight)
    for e in range(len(dLight)):
        dLight[e] = -1 * dLight[e]

    intensity = metha.dotProd(normal,dLight)

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r,g,b
    else:
        return (0,0,0)
    
def gouradShader(**kwargs):
    dLight = kwargs["dLight"]
    nA,nB,nC = kwargs["normals"]
    tA,tB,tC = kwargs["texCoords"]
    texture = kwargs["texture"]
    u,v,w = kwargs["bCoords"]

    b = 1.0
    g = 1.0
    r = 1.0

    if texture != None:
        tU = u*tA[0] + v*tB[0] + w*tC[0]
        tV = u*tA[1] + v*tB[1] + w*tC[1]

        textureColor = texture.getColor(tU,tV)
        b = textureColor[2]
        g = textureColor[1]
        r = textureColor[0]

    normal = [u*nA[0] + v*nB[0] + w*nC[0],
              u*nA[1] + v*nB[1] + w*nC[1],
              u*nA[2] + v*nB[2] + w*nC[2],]
    
    dLight = list(dLight)
    for e in range(len(dLight)):
        dLight[e] = -1 * dLight[e]

    intensity = metha.dotProd(normal,dLight)
    
    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r,g,b
    else:
        return (0,0,0)
    
def negativeShader(**kwargs):
    dLight = kwargs["dLight"]
    nA,nB,nC = kwargs["normals"]
    tA,tB,tC = kwargs["texCoords"]
    texture = kwargs["texture"]
    u,v,w = kwargs["bCoords"]

    b = 1.0
    g = 1.0
    r = 1.0

    if texture != None:
        tU = u*tA[0] + v*tB[0] + w*tC[0]
        tV = u*tA[1] + v*tB[1] + w*tC[1]

        textureColor = texture.getColor(tU,tV)
        b = textureColor[2]
        g = textureColor[1]
        r = textureColor[0]

    normal = [u*nA[0] + v*nB[0] + w*nC[0],
              u*nA[1] + v*nB[1] + w*nC[1],
              u*nA[2] + v*nB[2] + w*nC[2],]
    
    dLight = list(dLight)
    for e in range(len(dLight)):
        dLight[e] = -1 * dLight[e]

    intensity = metha.dotProd(normal,dLight)
    
    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        r = 1.0 - r
        g = 1.0 - g
        b = 1.0 - b
        return r,g,b
    else:
        return (1,1,1) 

def experimentshader(**kwargs):
    dLight = kwargs["dLight"]
    nA,nB,nC = kwargs["normals"]
    tA,tB,tC = kwargs["texCoords"]
    texture = kwargs["texture"]
    u,v,w = kwargs["bCoords"]

    b = 1.0
    g = 1.0
    r = 1.0

    if texture != None:
        tU = u*tA[0] + v*tB[0] + w*tC[0]
        tV = u*tA[1] + v*tB[1] + w*tC[1]

        textureColor = texture.getColor(tU,tV)
        b = textureColor[2]
        g = textureColor[1]
        r = textureColor[0]

    normal = [u*nA[0] + v*nB[0] + w*nC[0],
              u*nA[1] + v*nB[1] + w*nC[1],
              u*nA[2] + v*nB[2] + w*nC[2],]
    
    dLight = list(dLight)
    for e in range(len(dLight)):
        dLight[e] = -1 * dLight[e]

    intensity = metha.dotProd(normal,dLight)
    
    if intensity < 0.3:
        b = 0.890
        g = 0.090
        r = 0.039
    if intensity > 0.3 and intensity < 0.35:
        b = 0.627
        g = 0.839
        r = 0.024
    if intensity > 0.35 and intensity < 0.65:
        b = 0.435
        g = 0.278
        r = 0.937
    if intensity > 0.65 and intensity < 0.7:
        b = 0.627
        g = 0.839
        r = 0.024
    if intensity > 0.7 and intensity < 0.95:
        b = 0.400
        g = 0.819
        r = 1.0
    if intensity > 0.95:
        b = 0.572
        g = 0.929
        r = 0.850

    

    if intensity > 0:
        return r,g,b
    else:
        return (0,0,0)
