import random
from matplotlib import pyplot as plt 

# Add your code below:
numeros_a = range(1, 13)
numeros_b = [random.randint(1, 1000) for i in range(12)]
plt.plot(numeros_a, numeros_b)
plt.show()