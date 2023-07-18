# AUTHOR:   Eunice Anahi Mata Ixcayau
# CARNET:   21231
# PROF:     Carlos Alonso
# CLASS:    Computer Graphics
# SECTION:  20

#matrices
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
    