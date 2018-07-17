# Plotting via matplotlib

The `genie_python` distribution of python includes a powerful plotting library called [matplotlib](https://matplotlib.org/).

Matplotlib is a highly customizable, general purpose plotting library capable of producing a wide variety of plot types. There are lots of tutorials and examples online, such as:
- [`matplotlib.pyplot` API reference](https://matplotlib.org/2.2.2/api/pyplot_summary.html)
- [Matplotlib tutorials](https://matplotlib.org/2.2.2/tutorials/index.html)
- [Matplotlib examples](https://matplotlib.org/2.2.2/gallery/index.html)

# Quick-start

### To import pyplot

The most user-friendly interface to matplotlib is called `pyplot`. You can import `pyplot` using the following command:

```python
import matplotlib.pyplot as pyplot
```

### Useful pyplot commands:
- `pyplot.plot()`: Populate a plot with some data. If you want to discard old data first, use `plot.clf()`
- `pyplot.clf()`: Clear the current figure. Useful if you need to discard old data from the plot.
- `pyplot.show()`: Shows the matplotlib plotting window.
- `pyplot.draw()`: Draws any updates. Requires a plot to have been opened by `pyplot.show()` first.


### Example: plot and show a trivial graph
```python
pyplot.plot(range(10))
pyplot.show()
```

### Example: plot a constantly-updating sin wave
```python
from math import sin
from time import time, sleep

# Show plot - only need to do this once!
pyplot.show()

while True:
    # Clear the old data from the figure - we want to completely replace it.
    pyplot.clf()  

    # Plot our new data onto the figure.
    pyplot.plot([sin(x/1000.0 + time()) for x in range(10000)])

    # Draw the new data to the screen .
    pyplot.draw()

    # Short sleep to avoid going into a tight loop and using 100% processor.
    sleep(0.05)
```

# Plotting spectra

The `genie_python` library includes commands to quickly plot the neutron spectra on an instrument.

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

