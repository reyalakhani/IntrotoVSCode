#Step 1: Create a virtual environment
#Python3 - m venv myvenv

#Step 2: Activate the VE
#Source myvenv/bin/activate

#Step3: Install the 3rd party libraries
#pip3 install matplotlib


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))

plt.show()

print("Hello there!")