'''
1.pascals triangle
       1
      1 1
     1 2 1
    1 3 3 1
   1 4 6 4 1
 1 5 10 10 5 1

'''


def generate_pascals_equilateral_triangle(n):
    triangle = [[0] * (i + 1) for i in range(n)]

    for i in range(n):
        triangle[i][0] = 1
        triangle[i][i] = 1

        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    return triangle


# Generate Pascal's equilateral triangle with 6 rows
triangle = generate_pascals_equilateral_triangle(6)

# Print the triangle
for row in triangle:
    print(' '.join(str(num) for num in row).center(15))

'''
4.last element of list
'''

list = [1, 2, 3, 4]

# method 1
# last_el=list.pop()
# print(last_el)

# method 2
last_el = list[-1]
print(last_el)

'''
5.
'''

import array

array1 = array.array('i', [1, 2, 3])
array2 = array.array('i', [4, 2, 3])
common = set(array1).intersection(set(array2))
common_array=array.array('i',common)
print(common_array)