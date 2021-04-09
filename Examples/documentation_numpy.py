


from numpy import array

from sympy import symbols, Eq, Matrix, diff, Derivative, simplify, factor, expand, latex, init_printing, collect
init_printing()
from IPython.display import display, Math

x1, y1, x2, y2, x3, y3, x4, y4 = symbols('x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4')
r, s = symbols('r, s')

# Define the interpolation functions
h1 = factor(1/4*(1+r)*(1+s))
h2 = factor(1/4*(1-r)*(1+s))
h3 = factor(1/4*(1-r)*(1-s))
h4 = factor(1/4*(1+r)*(1-s))

display(Math('h_1 = ' + latex(h1)))
display(Math('h_2 = ' + latex(h2)))
display(Math('h_2 = ' + latex(h3)))
display(Math('h_2 = ' + latex(h4)))

x = h1*x1 + h2*x2 + h3*x3 + h4*x4
y = h1*y1 + h2*y2 + h3*y3 + h4*y4

display(Math('x = ' + latex(x)))
display(Math('y = ' + latex(y)))

J = Matrix([[diff(x, r), diff(y, r)],
            [diff(x, s), diff(y, s)]])

display(Math('J = (1/4)' + latex(factor(J*4))))

dH_drs = Matrix([[diff(h1, r), diff(h2, r), diff(h3, r), diff(h4, r)],
                 [diff(h1, s), diff(h2, s), diff(h3, s), diff(h4, s)]])

display(Math(r'\begin{bmatrix} \frac{dH}{dx} \\ \frac{dH}{dy} \end{bmatrix} = J^{-1}(1/4)' + latex(dH_drs*4)))
display(Math(r'\begin{bmatrix} \frac{dH}{dx} \\ \frac{dH}{dy} \end{bmatrix} = J^{-1}(1/4)' + latex(dH_drs*4)))