# This file was *autogenerated* from the file source_terms.sage.
from sage.all_cmdline import *   # import sage library
_sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0)
t = var('t')
x = var('x')
y = var('y')
g = var('g')
h = var('h')
H = var('d0')

eta = (t+_sage_const_1 )*h*cos(_sage_const_2 *pi*x)
u_x = (t+_sage_const_1 )*h*sin(_sage_const_2 *pi*x)
u_y = cos(_sage_const_2 *pi*x)+cos(_sage_const_2 *pi*y)

u_x_src = g*diff(eta, x) + diff(u_x, t)
u_y_src = g*diff(eta, y) + diff(u_y, t)
eta_src = diff(eta, t) + diff(H*u_x, x) + diff(H*u_y, y)

print "u_x: ", u_x
print "u_y: ", u_y
print "eta: ", eta

print "u_x src: ", u_x_src
print "u_y src: ", u_y_src
print "eta_src: ", eta_src

J = integrate(integrate((eta.subs(t=_sage_const_1 ))**_sage_const_2 , x, _sage_const_0 , _sage_const_1 ), y, _sage_const_0 , _sage_const_1 )
print "J(t=1): ", J.subs(h=_sage_const_1 )
print "diff(J(t=1), h).subs(h=1): ", diff(J, h).subs(h=_sage_const_1 )
