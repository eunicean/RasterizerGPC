import struct
import meth as metha
import math

from collections import namedtuple
from obj import Obj

V2 = namedtuple('Point2',['x','y'])
V3 = namedtuple('Point3',['x','y','z'])

POINTS = 0
LINES = 1
TRIANGLES = 2
QUADS = 3

def char(c):
    #1 byte
    return struct.pack('=c', c.encode('ascii'))

def word(w):
    #2 bytes
    return struct.pack('=h',w)

def dword(d):
    #4 bytes
    return struct.pack('=l',d)

def color(r,g,b):
    return bytes([int(b*255),
                  int(g*255),
                  int(r*255)])

class Model(object):
    def __init__(self, filename, translate = (0,0,0), rotate = (0,0,0), scale = (1,1,1)):
        model = Obj(filename)

        self.vertices = model.vertices
        self.textcoords = model.vertices
        self.normals = model.normals
        self.faces = model.faces

        self.translate = translate
        self.rotate = rotate
        self.scale = scale

class Renderer(object):
    def __init__(self, width,height):
        self.width = width
        self.height = height

        self.glClearColor(0,0,0)
        self.glClear()

        self.glColor(1,1,1)

        self.vertexShader = None
        self.fragmentShader = None

        self.primitiveType = TRIANGLES
        self.vertexBuffer = []

        self.objects = []

    def glAddVertices(self, vertices):
        for vert in vertices:
            self.vertexBuffer.append(vert)

    def glPrimitiveAssembly(self, tverts):
        primitives = []
        
        if self.primitiveType == TRIANGLES:
            for i in range(0,len(tverts),3):
                triangle = []
                triangle.append(tverts[i])
                triangle.append(tverts[i+1])
                triangle.append(tverts[i+2])
                primitives.append(triangle)
        
        return primitives

    def glClearColor(self, r, g, b):
        self.clearColor = color(r,g,b)

    def glColor(self, r, g, b):
        self.currColor = color(r,g,b)
 

    def glClear(self):
        self.pixels = [[self.clearColor for y in range(self.height)]
                       for x in range(self.width)]
        
        self.zbuffer = [[float('inf') for y in range(self.height)]
                       for x in range(self.width)]
        
    def glPoint(self,x,y,clr=None):
        if (0<=x<self.width) and (0<=y<self.height):
            self.pixels[x][y] = clr or self.currColor

    # def glTriangle(self, v0,v1,v2, clr=None):
    #     self.glLine(v0,v1,clr or self.currColor)
    #     self.glLine(v1,v2,clr or self.currColor)
    #     self.glLine(v2,v0,clr or self.currColor)

    def glTriangle(self, A,B,C, clr=None):
        #asegurarse de que siempre mantengan un orden
        if A[1] < B[1]:
            A,B = B,A
        if A[1] < C[1]:
            A,C = C,A
        if B[1] < C[1]:
            B,C = C,B
            
        self.glLine(A,B,clr or self.currColor)
        self.glLine(B,C,clr or self.currColor)
        self.glLine(C,A,clr or self.currColor)

        def flatbottom(vA,vB,vC):
            try:
                mBA = (vB[0] - vA[0])/(vB[1] - vA[1])
                mCA = (vC[0] - vA[0])/(vC[1] - vA[1])
            except:
                pass
            else:
                x0 = vB[0]
                x1 = vC[0]

                for y in range(int(vB[1]),int(vA[1])):
                    self.glLine((x0,y),(x1,y),clr or self.currColor)
                    x0 += mBA
                    x1 += mCA
        
        def flattop(vA,vB,vC):
            try:
                mCA = (vC[0] - vA[0])/(vC[1] - vA[1])
                mCB = (vC[0] - vB[0])/(vC[1] - vB[1])
            except:
                pass
            else:
                x0 = vA[0]
                x1 = vB[0]

                for y in range(int(vA[1]),int(vC[1]),-1):
                    self.glLine((x0,y),(x1,y),clr or self.currColor)
                    x0 -= mCA
                    x1 -= mCB

        if B[1] == C[1]:
            #parte plana abajo
            flatbottom(A,B,C)
        elif A[1] == B[1]:
            #parte plana arriba
            flattop(A,B,C)
        else:
            #dibujar ambos casos con un nuevo vertice D
            D = (A[0]+ ((B[1]-A[1])/(C[1]-A[1])) * (C[0]-A[0]),B[1])

            flatbottom(A,B,D)
            flattop(B,D,C)

    def glTriangle_bc(self, A,B,C):
        minX = round(min(A[0],B[0],C[0]))
        maxX = round(max(A[0],B[0],C[0]))
        minY = round(min(A[1],B[1],C[1]))
        maxY = round(max(A[1],B[1],C[1]))

        colorA = (1,0,0)
        colorB = (0,1,0)
        colorC = (0,0,1)

        for x in range(minX,maxX + 1):
            for y in range(minY,maxY+1):
                if (0<= x < self.width) and (0<=y<= self.height):
                    P = (x,y)
                    bCoords = metha.barycentrinCoords(A,B,C,P)

                    if bCoords != None:
                        u,v,w = bCoords
                        if 0<=u<=1 and 0<=v<=1 and 0<=w<=1:
                            z = u*A[2] + v*B[2] + w*C[2]

                            if z < self.zbuffer[x][y]:
                                self.zbuffer[x][y] = z

                                colorP = color(u*colorA[0] + v*colorB[0] + w*colorC[0],
                                            u*colorA[1] + v*colorB[1] + w*colorC[1],
                                            u*colorA[2] + v*colorB[2] + w*colorC[2])

                                self.glPoint(x,y,colorP)


    def glModelMatrix(self, translate = (0,0,0),rotate = (0,0,0), scale = (1,1,1)):
        translation = [[1,0,0,translate[0]],
                     [0,1,0,translate[1]],
                     [0,0,1,translate[2]],
                     [0,0,0,1]]
        
        rotMat = self.glRotationMatrix(rotate[0],rotate[1],rotate[2])

        scaleMat = [[scale[0],0,0,0],
                    [0,scale[1],0,0],
                    [0,0,scale[2],0],
                    [0,0,0,1]]
        
        return metha.multiplymatrix(metha.multiplymatrix(translation,rotMat),scaleMat)

    def glRotationMatrix(seld, pitch = 0, yaw = 0, roll = 0):
        pitch *= math.pi /180
        yaw *= math.pi /180
        roll *= math.pi /180

        pitchMat = [[1,0,0,0],
                    [0,math.cos(pitch),-math.sin(pitch),0],
                    [0,math.sin(pitch),math.cos(pitch),0],
                    [0,0,0,1]]
        
        yawMat = [[math.cos(yaw),0,math.sin(yaw),0],
                  [0,1,0,0],
                  [-math.sin(yaw),0,math.cos(yaw),0],
                  [0,0,0,1]]
        
        rollMat = [[math.cos(roll),-math.sin(roll),0,0],
                   [math.sin(roll),math.cos(roll),0,0],
                   [0,0,1,0],
                   [0,0,0,1]]
        
        return metha.multiplymatrix(metha.multiplymatrix(pitchMat,yawMat),rollMat)

    def glLine(self,v0,v1,clr=None):
        #Bresenham line algorith
        # y = m*x + b
        
        #m = (v1.y-v0.y)/(v1.x-v0.x
        #y = v0.y
        #for x in range(v0.x,v1.x+1):
        #    self.glPoint(x,int(y))
        #    y += m

        x0 = int(v0[0])    
        x1 = int(v1[0])    
        y0 = int(v0[1])    
        y1 = int(v1[1])

        #si el punto 0 es igual al punto 1, se dibuja un punto
        if x0 == x1 and y0 == y1:
            self.glPoint(x0,y0)
            return
        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        steep = dy > dx

        # si la linea tiene pendiente mayor a 1 o menor a -1 
        # intercambiamos las x por las y, y se dibuja la linea
        # de manera vertical en vez de horizontal
        if steep:
            x0,y0 = y0,x0
            x1,y1 = y1,x1

        # si e punto inicial en X es mayor que el punto final en X,
        # intercambiamos los puntos para siempre dibujar de izquierda
        # a derecha
        if x0 > x1:
            x0,x1 = x1,x0
            y0,y1 = y1,y0
        
        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        offset = 0
        limit = 0.5
        m = dy/dx
        y = y0

        for x in range(x0,x1+1):
            if steep:
                #dibujar de manera vertical
                self.glPoint(y,x,clr or self.currColor)
            else:
                #dibujar de manera horizontal
                self.glPoint(x,y,clr or self.currColor)

            offset += m

            if offset >= limit:
                if y0 < y1:
                    y += 1
                else:
                    y -= 1
                    
                limit += 1

    def glLoadModel(self, filename, translate = (0,0,0), rotate = (0,0,0), scale = (1,1,1)):
        self.objects.append(Model(filename,translate,rotate,scale))

    def glRender(self):
        transformedVerts = []

        for model in self.objects:
            mMat = self.glModelMatrix(model.translate,model.rotate, model.scale)

            for face in model.faces:
                vertCount = len(face)

                v0 = model.vertices[face[0][0]-1]
                v1 = model.vertices[face[1][0]-1]
                v2 = model.vertices[face[2][0]-1]

                if vertCount == 4:
                    v3 = model.vertices[face[3][0]-1]
                
                if self.vertexShader:
                    v0 = self.vertexShader(v0, modelMatrix = mMat)
                    v1 = self.vertexShader(v1, modelMatrix = mMat)
                    v2 = self.vertexShader(v2, modelMatrix = mMat)
                    if vertCount == 4:
                        v3 = self.vertexShader(v3, modelMatrix = mMat)
                
                transformedVerts.append(v0)
                transformedVerts.append(v1)
                transformedVerts.append(v2)
                if vertCount == 4:
                    transformedVerts.append(v0)
                    transformedVerts.append(v2)
                    transformedVerts.append(v3)

        # for vert in self.vertexBuffer:
        #     if self.vertexShader:
        #         transformedVerts.append(self.vertexShader(vert, modelMatrix = self.modelMatrix))
        #     else:
        #         transformedVerts.append(vert)
        
        primitives = self.glPrimitiveAssembly(transformedVerts)


        for prim in primitives:
            if self.primitiveType == TRIANGLES:
                self.glTriangle_bc(prim[0],prim[1],prim[2])



    def glFinish(self, filename):
        with open(filename,"wb") as file:
            #header
            file.write(char("B"))
            file.write(char("M"))
            file.write(dword(14 + 40 + (self.width * self.height * 3)))
            file.write(dword(0))
            file.write(dword(14 + 40))

            #infoHeader
            file.write(dword(40))
            file.write(dword(self.width))
            file.write(dword(self.height))
            file.write(word(1))
            file.write(word(24))
            file.write(dword(0))
            file.write(dword(self.width * self.height * 3))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))

            #color table
            for y in range(self.height):
                for x in range(self.width):
                    file.write(self.pixels[x][y])


    