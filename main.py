from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix(0,0)

add_edge(matrix,20,20,0,50,20,0)

'''
matrix2 = new_matrix()

identi = ident(matrix)
matrix = [[1.00, 4.00, 7.00, 10.00],
          [2.00, 5.00, 8.00, 11.00],
          [3.00, 6.00, 9.00, 12.00],
          [1.00, 1.00, 1.00, 1.00]]
matrix2 = [[1.00, 4.00],
           [2.00, 5.00],
           [3.00, 6.00],
           [1.00, 1.00]]

print_matrix(matrix)
print_matrix(matrix2)
matrix_mult(matrix,matrix2)
print_matrix(matrix2)
print_matrix(identi)
'''

draw_lines( matrix, screen, color )
display(screen)
