# AUTHOR:   Eunice Anahi Mata Ixcayau
# CARNET:   21231
# PROF:     Carlos Alonso
# CLASS:    Computer Graphics
# SECTION:  20

#matrices

import math

def multiplymatrix(A,B):
    
    if len(A[0]) == len(B):
        C = [[0,0,0,0],
             [0,0,0,0],
             [0,0,0,0],
             [0,0,0,0]]

        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(A[0])):
                    C[i][j] += A[i][k] * B[k][j]

        return C
    else:
        return None

def multiplyMatrixVector(A,B):
    # A es el vector
    # B es la matriz
    if len(A) == len(B):
        C = [0,0,0,0]

        for i in range(len(A)):
            for j in range(len(B[0])):
                C[i] += B[i][j] * A[j]

        return C
    else:
        return None
    

def barycentrinCoords(A,B,C,P):

    areaPBC = (B[1]- C[1]) * (P[0]-C[0]) + (C[0] - B[0]) * (P[1]-C[1])
    areaACP = (C[1]- A[1]) * (P[0]-C[0]) + (A[0] - C[0]) * (P[1]-C[1])
    areaABC = (B[1]- C[1]) * (A[0]-C[0]) + (C[0] - B[0]) * (A[1]-C[1])

    # areaPBC = abs((P[0]*B[1] + B[0]*C[1] + C[0]*P[1]) - 
    #               (P[1]*B[0] + B[1]*C[0] + C[1]*P[0]))
    # areaACP = abs((A[0]*C[1] + C[0]*P[1] + P[0]*A[1]) - 
    #               (A[1]*C[0] + C[1]*P[0] + P[1]*A[0]))
    # areaABC = abs((A[0]*B[1] + B[0]*C[1] + C[0]*A[1]) - 
    #               (A[1]*B[0] + B[1]*C[0] + C[1]*A[0]))

    if areaABC ==0:
        return None

    u = areaPBC / areaABC
    v = areaACP / areaABC
    w = 1-u-v

    if 0<=u<=1 and 0<=v<=1 and 0<=w<=1 and math.isclose(u+v+w,1.0):
        return u,v,w
    else:
        return None