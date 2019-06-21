The `genie_python` distribution of python includes a powerful plotting library called [matplotlib](https://matplotlib.org/).

Matplotlib is a highly customizable, general purpose plotting library capable of producing a wide variety of plot types. There are lots of tutorials and examples online, such as:
- [Matplotlib tutorials](https://matplotlib.org/2.2.2/tutorials/index.html)
- [Matplotlib examples](https://matplotlib.org/2.2.2/gallery/index.html)
- [`matplotlib.pyplot` command reference](https://matplotlib.org/2.2.2/api/pyplot_summary.html)

### Contents
- [Quick-start](#quick-start)
    - [To import pyplot](#to-import-pyplot)
    - [Useful pyplot commands](#useful-pyplot-commands)
    - [Example: Plot and show a trivial graph](#example-plot-and-show-a-trivial-graph)
    - [Example: Plot a constantly updating sin wave](#example-plot-a-constantly-updating-sin-wave)
- [Plotting Spectra](#plotting-spectra)
- [Using matplotlib within the IBEX GUI](#using-matplotlib-within-the-ibex-gui)

# Quick-start

### To import pyplot

The most user-friendly interface to matplotlib is called `pyplot`. You can import `pyplot` using the following command:

```python
import matplotlib.pyplot as pyplot
```

### Useful pyplot commands:
- `pyplot.plot()`: Populate a plot with some data.
- `pyplot.clf()`: Clear the current figure, e.g. discard old data from the plot.
- `pyplot.show()`: Shows the matplotlib plotting window.
- `pyplot.draw()`: Draws updates to a plot that is already open.
- `pyplot.close('all')`: Closes all plots and removes all data.
- `pyplot.close(n)`: Close a specific figure.
- `pyplot.figure()`: Creates a new figure.
- `pyplot.figure(n)`: Creates or switches to figure n.


### Example: plot and show a trivial graph
```python
import matplotlib.pyplot as pyplot
pyplot.plot(range(10))
pyplot.show()
```

### Example: plot a constantly-updating sin wave
```python
import matplotlib.pyplot as pyplot
from math import sin
from time import time, sleep

# Create a new figure.
pyplot.figure()

# Show plot - only need to do this once,! (this will display the blank figure)
pyplot.show()

while True:
    # Clear the old data from the figure - we want to replace it completely.
    pyplot.clf()  
    # Plot our new data onto the figure.
    pyplot.plot([sin(x/1000.0 + time()) for x in range(10000)])
    # Draw the new data to the screen.
    pyplot.draw()
    # Short sleep to avoid going into a tight loop and using 100% processor.
    sleep(0.5)
```

# Plotting spectra

The `genie_python` library includes commands to plot the neutron spectra on an instrument quickly.

Plot a single spectrum:
```python
g.plot_spectrum(1)
```

Plot several spectra on one graph:
```python
graph = g.plot_spectrum(1)
graph.add_spectrum(2)
graph.add_spectrum(3, period=2)
```

Plot several spectra on different graphs:
```python
g.plot_spectrum(1)
g.plot_spectrum(2)
```

For greater control over the exact presentation or contents of the spectra plots, the raw spectrum data can be acquired using:
```python
g.get_spectrum(spectrum=1)
```

# Using matplotlib within the IBEX GUI

The IBEX user interface includes a python scripting window. When plotting graphs within IBEX, matplotlib is configured to display the plot within the IBEX gui. 

In the IBEX user interface, matplotlib is _non-blocking_ - that is, a script will continue once a plot has been drawn without the plot needing to be closed.

> Note: this is new functionality as of July 2018. If you prefer matplotlib windows to spawn separately from the main IBEX window, you can type the matplotlib command:
> ```python
> matplotlib.use('Qt4Agg')
> ```
> This needs to be typed before any matplotlib functionality is used for it to take effect.

# Troubleshooting

### Only 6 plots can be opened at once

By default, only 6 plots can be opened at a time. This is a limitation of the internet explorer view which displays the plot. The limit can be increased by an administrator on individual instruments by running the following command:

`reg add "\\<ndxinstname>\HKLM\SOFTWARE\Microsoft\Internet Explorer\MAIN\FeatureControl\FEATURE_WEBSOCKET_MAXCONNECTIONSPERSERVER"  /v iexplore.exe /t REG_DWORD /d 48`

Contact computing group if the limit is set too low on your instrument and they will be able to run the command above (it will require admin privileges).

As of Release Version 5.5, only 6 plots can be opened at a time, and if this limit is exceeded, the oldest plot will be automatically removed.