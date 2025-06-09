# Matplotlib

The python distribution deployed on instruments includes a powerful plotting library called {external+matplotlib:py:mod}`matplotlib`.

Matplotlib is a highly customisable, general purpose plotting library capable of producing a wide variety of plot types. There are lots of tutorials and examples online, such as:
- {external+matplotlib:ref}`Matplotlib tutorials <tutorials>`
- {external+matplotlib:ref}`Matplotlib examples <examples-index>`
- {external+matplotlib:py:mod}`matplotlib.pyplot` command reference

```{contents}
```

## Import pyplot

The most user-friendly interface to matplotlib is called {external+matplotlib:py:mod}`matplotlib.pyplot`. You can import {external+matplotlib:py:mod}`pyplot <matplotlib.pyplot>` using the following command:

```python
import matplotlib.pyplot as pyplot
```

## Useful pyplot commands
- {external+matplotlib:py:obj}`matplotlib.pyplot.plot`: Populate a plot with some data.
- {external+matplotlib:py:obj}`matplotlib.pyplot.clf`: Clear the current figure, e.g. discard old data from the plot.
- {external+matplotlib:py:obj}`matplotlib.pyplot.show`: Shows the matplotlib plotting window.
- {external+matplotlib:py:obj}`matplotlib.pyplot.draw`: Draws updates to a plot that is already open.
- {external+matplotlib:py:obj}`matplotlib.pyplot.close`: Closes plots and removes all data.
- {external+matplotlib:py:obj}`matplotlib.pyplot.figure`: Creates or switches to figure n.


## Example: plot and show a trivial graph
```python
import matplotlib.pyplot as pyplot
pyplot.plot(range(10))
pyplot.show()
```

## Example: plot a constantly-updating sin wave
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

## Plotting spectra

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

## Using matplotlib within the IBEX GUI

The IBEX user interface includes a python scripting window. When plotting graphs within IBEX, matplotlib is configured to display the plot within the IBEX gui. 

In the IBEX user interface, matplotlib is _non-blocking_ - that is, a script will continue once a plot has been drawn without the plot needing to be closed.

:::{note}
This is new functionality as of July 2018. If you prefer matplotlib windows to spawn separately from the main IBEX window, you can type the matplotlib command:
```python
matplotlib.use('Qt4Agg')
```
This needs to be typed before any matplotlib functionality is used for it to take effect.
:::

By default, only 3 plots can be opened at a time. If this limit is exceeded, the oldest plot will be automatically removed.