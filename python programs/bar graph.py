import numpy as np
import matplotlib.pyplot as plt
x=np.array(["A","B","C"])
y=np.array([10,50,15])
plt.bar(x,y,color="skyblue")
plt.xlabel("categories")
plt.ylabel("values")
plt.title("Bar Graph using numpy and matplotlib")
plt.show()