import cmath

def root2(a, b, c):

    D = b**2 - 4*a*c

  
    x1 = (-b + cmath.sqrt(D)) / (2*a)
    x2 = (-b - cmath.sqrt(D)) / (2*a)

 
    def f(x):
        return a*x**2 + b*x + c

    check1 = cmath.isclose(f(x1), 0, rel_tol=1e-9, abs_tol=0.0)
    check2 = cmath.isclose(f(x2), 0, rel_tol=1e-9, abs_tol=0.0)

    return (x1, x2), (check1, check2)
//https://chatgpt.com/share/695a0746-25c0-8004-8493-022caf2d8b46