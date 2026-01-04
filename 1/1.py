import numpy as np

def f(x):
    return x**2

def F(x, n=10000):
    t = np.linspace(0, x, n)
    return np.trapz(f(t), t)
x = 2.0
h = 1e-5

numerical_derivative = (F(x+h) - F(x-h)) / (2*h)

print("f(x) =", f(x))
print("F'(x) ≈", numerical_derivative)
//https://chatgpt.com/share/695a0746-25c0-8004-8493-022caf2d8b46