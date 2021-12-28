import matplotlib.pyplot as plt
import numpy as np


labels = ['TSP', 'center']
python_performance = [4.2500 ,8.908 ]
java_performance = [0.57 , 7.50 ]

x = np.arange(len(labels))  # the label locations
width = 0.20  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2,java_performance, width, label='Java')
rects2 = ax.bar(x + width/2, python_performance, width, label='Python')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('seconds')
ax.set_title('1000Nodes')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()