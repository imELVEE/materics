"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    m = ""
    for i in range(4):
        for v in matrix[i]:
            m += str(v) + " "
        m += "\n"
    print(m)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    return [[1.0 , 0.0 , 0.0 , 0.0],
            [0.0 , 1.0 , 0.0 , 0.0],
            [0.0 , 0.0 , 1.0 , 0.0],
            [0.0 , 0.0 , 0.0 , 1.0],
                                    ]

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    row,col = [],[]
    #make answer the correct size
    answer = []
    for r in range(len(m1)):
        answer.append([])
        for c in m2[0]:
            answer[r].append(0)
    #take the row of m1
    row = m1[0]

    for r1 in m1:
        ra = 0
        for r2 in m2:
            for col in r2:
                ca = 0
                for i in range(len(r1)):
                    sum = 0
                    

    #take the column of m2
    for r in m2:
        col.append(r[0])
    #dot product
    sum = 0
    for i in range(len(row)):
        sum += row[i]*col[i]

    answer[0][0] = sum
    #m2 becomes the new matrix
    return answer



def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
