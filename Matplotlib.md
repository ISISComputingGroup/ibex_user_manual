# Plotting via matplotlib

The `genie_python` distribution of python includes a powerful plotting library called [matplotlib](https://matplotlib.org/).

Matplotlib is a highly customizable, general purpose plotting library capable of producing a wide variety of plot types. There are lots of tutorials and examples online, such as:
- [`matplotlib.pyplot` API reference](https://matplotlib.org/2.2.2/api/pyplot_summary.html)
- [Matplotlib tutorials](https://matplotlib.org/2.2.2/tutorials/index.html)
- [Matplotlib examples](https://matplotlib.org/2.2.2/gallery/index.html)

# Quick-start

### To import pyplot
```python
import matplotlib.pyplot as pyplot
```

### To create (and show) an example plot
```python
pyplot.plot(range(10))
pyplot.show()
```

### To remove all plots and start with a completely clean matplotlib screen.
```python
pyplot.close('all')
```

### To plot a constantly-updating sin wave
```python
from math import sin
from time import time, sleep
pyplot.show()
while True:
    pyplot.clf()
    pyplot.plot([sin(x/1000.0 + time()) for x in range(10000)])
    pyplot.draw()
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

