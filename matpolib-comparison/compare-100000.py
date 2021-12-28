import matplotlib.pyplot as plt
import numpy as np


labels = ['load', 'save', 's-path', ]
python_performance = [0.282, 1.4037, 0.135 ]
java_performance = [0.0263, 0.123, 0.00999 ]

x = np.arange(len(labels))  # the label locations
width = 0.28  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2,java_performance, width, label='Java')
rects2 = ax.bar(x + width/2, python_performance, width, label='Python')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('ms')
ax.set_title('10000Nodes')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()