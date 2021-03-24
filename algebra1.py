from numpy import *
from pylab import *
x = linspace(-3, 3, 100)
y1 = cos(x)
y2 = cos(2 * x)
plot(x, y1)
plot(x, y2)
show()