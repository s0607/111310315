import numpy as np

n = int(input("請輸入多項式次數 n："))

c = []
for i in range(n + 1):
    ci = float(input(f"請輸入 c[{i}]："))
    c.append(ci)

roots = np.roots(c[::-1])
print("多項式的根為：")
print(roots)
//https://chatgpt.com/share/695a0a27-1784-8004-8d9e-f1804e0c7902