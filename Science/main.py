"""Import packages."""
# import matplotlib
# matplotlib.use('Agg')  # For Bash on Windows
import matplotlib.pyplot as plt
import numpy as np

# matplotlib.use('Agg')  # For Bash on Windows
x = [1, 2, 3, 4]
y = [2, 3, 4, 5]

plt.plot(x, y)
plt.savefig("test.png")

a = [1, 2, 3]
b = [1, 2, 3]

print(np.cross(a, b))
