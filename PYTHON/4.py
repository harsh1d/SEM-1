# class MyClass:
#   x = 5

# p1 = MyClass()
# print(p1.x)

class MyClass:
    def __init__(self):
        self.x = 5

p1 = MyClass()
print('p1.x =', p1.x)

c = 23892.80076
k = 4099768.2
m = 2000
Y = 0.1
import numpy as np
w = np.linspace(0, 100)

X = Y * ((k ** 2 + (c * w) ** 2) / ((k - m * (w ** 2)) ** 2 + (c * w) ** 2)) ** 0.5

import matplotlib.pyplot as plt
plt.figure()
plt.plot(w, X, 'b-', linewidth=2)
plt.grid(True)
plt.xlabel('w', fontsize=15)
plt.ylabel('X', fontsize=15)

# Plot point at w = 29.08882087
w = 29.08882087
X = Y * ((k**2 + (c*w)**2) / ((k-m*(w**2))**2 + (c*w)**2))**0.5
plt.hold(True)
plt.plot(w, X, 'r.', linewidth=2, markersize=25)
plt.show()