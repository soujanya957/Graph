from matplotlib import pyplot as plt

import numpy as np


dev_x = [25, 26, 27, 28, 29, 30, 31, 32,33,34,35]
dev_y = [38000, 42000, 47000, 49000, 53000, 56000, 62000, 65000, 67000, 69000, 74000 ]



plt.scatter(dev_x, dev_y, color="k", linestyle="--", marker='.', label="All devs")
#axis label
plt.xlabel("Ages")
plt.ylabel("Meow")

#plot title
plt.title("Median Salaray (USD) by age")


#legend chronological
plt.legend()

#grid 
plt.grid(True)

#prevent padding
plt.tight_layout()


#save
plt.savefig("plot.png")

#show graph
plt.show()
