# Source:
# https://donjayamanne.github.io/pythonVSCodeDocs/docs/jupyter_getting-started/

# init_notebook_mode(Connected = True)
#open Jupyter Notebook
# run with Jupyter: Run Selection Line (strg+alt+Enter)
# Print / plots are shown in python interactive


import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show() 

print('a')


print(x[1])

#interactive plot, only works with jupyter Notbeook mode in vsc

import matplotlib.pyplot as plt
import numpy as np
import mpld3



mpld3.enable_notebook()
fig, ax = plt.subplots(subplot_kw=dict(axisbg='#EEEEEE'))
ax.grid(color='white', linestyle='solid')
N = 50
scatter = ax.scatter(np.random.randn(size=N),
                     np.random.randn(size=N),
                     c=np.random.random(size=N),
                     s = 1000 * np.random.random(size=N),
                     alpha=0.3,
                     cmap=plt.cm.jet)
ax.set_title("D3 Scatter Plot", size=18);




from bokeh.io import push_notebook, show, output_notebook
from bokeh.layouts import row, gridplot
from bokeh.plotting import figure, show, output_file
output_notebook()

import numpy as np

x = np.linspace(0, 4*np.pi, 100)
y = np.sin(x)
TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select"

p1 = figure(title="Legend Example", tools=TOOLS)
p1.circle(x,   y, legend="sin(x)")
p1.circle(x, 2*y, legend="2*sin(x)", color="orange")
p1.circle(x, 3*y, legend="3*sin(x)", color="green")
show(p1)