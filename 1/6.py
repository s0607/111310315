import matplotlib.pyplot as plt
import numpy as np

# 1. 定義點
A = np.array([1, 1])
B = np.array([4, 3])
C = np.array([2, 5])

# 2. 計算兩直線交點
# 線 AB 與直線 y = -x + 6
def line_intersection(p1, p2, q1, q2):
    A = np.array([[p2[0]-p1[0], q1[0]-q2[0]],
                  [p2[1]-p1[1], q1[1]-q2[1]]])
    b = np.array([q1[0]-p1[0], q1[1]-p1[1]])
    t = np.linalg.solve(A, b)
    intersection = p1 + t[0]*(p2-p1)
    return intersection

P = line_intersection(A, B, np.array([0,6]), np.array([6,0]))
print("交點:", P)

# 3. 給定直線和線外一點，作垂直線
def perpendicular_line_through_point(p1, p2, point, length=5):
    # p1 p2 是直線，point 是線外點
    delta = p2 - p1
    slope_perp = np.array([-delta[1], delta[0]])
    slope_perp = slope_perp / np.linalg.norm(slope_perp)
    line_points = np.array([point - slope_perp*length/2, point + slope_perp*length/2])
    return line_points

perp_line = perpendicular_line_through_point(A, B, C)

# 4. 驗證垂直三角形（畫出直角三角形）
triangle = np.array([A, B, C, A])  # 將 A B C 連回 A

# 5. 畫圖
plt.figure()
plt.plot([A[0], B[0]], [A[1], B[1]], 'b-', label='線 AB')
plt.plot(perp_line[:,0], perp_line[:,1], 'r--', label='垂直線')
plt.plot(triangle[:,0], triangle[:,1], 'g-', label='三角形')
plt.scatter([A[0], B[0], C[0]], [A[1], B[1], C[1]], color='k')
plt.text(A[0], A[1], 'A')
plt.text(B[0], B[1], 'B')
plt.text(C[0], C[1], 'C')

plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()
//https://chatgpt.com/share/695a0d25-0088-8004-9744-e070bfb9dac3