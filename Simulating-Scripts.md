[[Scripting|scripting]] > [[Simulating Scripts|Simulating-Scripts]]

Simulated Genie Python
======================

Before running a script on real hardware you may want to check that the script will behave as expected and contains no errors. To help do this `genie_python` has a simulated mode where commands that would normally communicate with hardware instead print what they are doing. To get in and out of simulation mode there is a [context manager](https://www.geeksforgeeks.org/context-manager-in-python/) which will turn simulation mode on only for the code inside it's scope and will then turn it off for you after. This can be used like:

```python
with g.sim.Simulate():
    g.begin()
    g.cset("Freq_T0", 10)
    print(g.cget("Freq_T0"))
    g.end()
```
which would give:
```
Run started
Waiting to exit state SETUP
Setting Freq_T0 to value 10
OrderedDict([('connected', True), ('name', 'Freq_T0'), ('value', 10), ('runcontrol', None), ('lowlimit', None), ('highlimit', None), ('alarm', 'NO_ALARM')])
Run ended
Waiting for state SETUP
```

This can also be used to run your own functions, e.g.
```python
g.load_script("my_script.py")
with g.sim.Simulate():
    my_function()  # Any genie_python calls in here will be simulated 
```

By default the simulation environment will be populated with all the current blocks that you have in your configuration and will give you errors if the script you are simulating tries to access blocks that do not exist in the current config.

Within your scripts you can check if you are in simulation mode or not using `g.sim.in_sim_mode()` e.g.

```python
with g.sim.Simulate():
    print(g.sim.in_sim_mode())
print(g.sim.in_sim_mode())
```
```
True
False
```

## Initial Block Values in simulation mode

By default when entering simulation mode all blocks have the value `INITIAL_VALUE`. However, you may want to provide some defaults of your own so that you can simulate how the script will run from various starting conditions. You can do this by providing a dictionary of values when creating the context manager e.g.:

```python
with g.sim.Simulate(initial_block_values={'TEST_BLOCK': 42.42}):
    test_block_data = g.cget("TEST_BLOCK")
    print(test_block_data['value'])
```
```
42.42
```

You could also provide the current state of the instrument by using `cgets` before starting simulation mode:

```python
current_block_values = {"TEST_BLOCK": g.cget("TEST_BLOCK")}
with g.sim.Simulate(initial_block_values=current_block_values):
    ...
```

What is and is not simulated
============================

Simulation mode **will only simulate the functions inside genie_python**, i.e. those beginning with `g.` e.g. `g.cset`, `g.cget` etc. It will **not** simulate the following:
* Anything deeper inside genie_python e.g. `g.os.open`
* Anything outside of `g.` e.g. `time.sleep()`

There is some logic in simulation mode in that if you do `g.cset("my_block", 10)` followed by `g.cget("my_block")` the new value of the block will be 10. However, this is very limited and is a work in progress, if there are additional behaviours you would like to see in simulation mode please get in touch.

The following are some examples of potential mistakes that could be made with simulation mode and some examples of how to fix them:

```python
import matplotlib.pyplot as pyplot
from time import sleep
block_values = []
while(True):
    block_values.append(g.cget("my_block")["value"])
    sleep(10) # This will still wait for 10 seconds even when simulating!!
    if my_block_value > 100: # The simulated value of my_block may never reach 100 and so this may loop forever
        break 
pyplot.plot(my_block_value)
pyplot.show() # This will still show a plot even when simulating!!
```

this could be improved by:

```python
import matplotlib.pyplot as pyplot
from time import sleep
block_values = []
while(True):
    block_values.append(g.cget("my_block")["value"])
    g.waitfor_time(seconds=10) # Simulated genie_python will skip the wait here and just print
    if my_block_value > 100 or g.sim.in_sim_mode(): # We will now stop looping if in simulation mode
        break
if not g.sim.in_sim_mode(): # This will now only plot if not in simulation
    pyplot.plot(my_block_value)
    pyplot.show() 
```