import matplotlib.pyplot as plt
import numpy as np


labels = ['load', 'save', 's-path', ]
python_performance = [5.829 , 26.626, 5.5979]
java_performance = [7.882, 6.971 , 17 ]

x = np.arange(len(labels))  # the label locations
width = 0.28  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2,java_performance, width, label='Java')
rects2 = ax.bar(x + width/2, python_performance, width, label='Python')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('ms')
ax.set_title('1000Nodes')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()