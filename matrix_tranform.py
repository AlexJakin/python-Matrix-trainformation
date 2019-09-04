"""
@author: Alex
@contact: 1272296763@qq.com or jakinmili@gmail.com
@software: PyCharm
@file: matrix_tranform.py
@time: 2019/9/4 22:10
"""
import matplotlib.pyplot as plt
from Matrix.Matrix import Matrix
from Matrix.Vector import Vector
import math
points = [[0, 0], [0, 5], [3, 5], [3, 4], [1, 4], [1, 3], [2, 3], [2, 2], [1, 2], [1, 0]]


x = [point[0] for point in points]
y = [point[1] for point in points]

plt.figure(figsize=(5, 5))
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.plot(x, y)
# plt.show()

P = Matrix(points)


# 1.缩放
T = Matrix([[2, 0], [0, 1.5]])

# 2.x轴翻转
T = Matrix([[1, 0], [0, -1]])

# 3.y轴翻转
T = Matrix([[-1, 0], [0, 1]])

# 4.关于原点旋转
T = Matrix([[-1, 0], [0, -1]])

# 5.沿x轴错切
T = Matrix([[1, 0.5], [0, 1]])

# 5.沿y轴错切
T = Matrix([[1, 0], [0.5, 1]])

# 绕theta角旋转
theta = math.pi / 3
T = Matrix([[math.cos(theta), math.sin(theta)], [-math.sin(theta), math.cos(theta)]])

P2 = T.dot(P.T())
plt.plot([P2.col_vector(i)[0] for i in range(P2.col_num())],
         [P2.col_vector(i)[1] for i in range(P2.col_num())])
plt.show()