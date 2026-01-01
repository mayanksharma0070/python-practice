import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,0,1,3])
y=np.array([2,1,3,1])
plt.plot(x,y,color="green",marker='o',ms=10,ls="-.")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("line chart")
plt.show()