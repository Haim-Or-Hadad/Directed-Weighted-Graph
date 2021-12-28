import matplotlib.pyplot as plt
import numpy as np


labels = ['TSP', 'center']
python_performance = [57.95708 ,1347.7275 ]
java_performance = [1 , 00000 ]

x = np.arange(len(labels))  # the label locations
width = 0.20  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2,java_performance, width, label='Java')
rects2 = ax.bar(x + width/2, python_performance, width, label='Python')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('seconds')
ax.set_title('10000Nodes')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()