import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(-200,200,400)
y1 = x1**2
x2 = np.linspace(-200,200,400)
y2 = -x2**2 + 40000

plt.plot(x1,y1, linewidth=4,color='green',label='y1=x1**2')
plt.plot(x2,y2, linewidth=3,color='red',label='y2=-x2**2+40000')

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Parabola")
plt.show()
