Tips & Examples
###############

Tips from the developers
========================

Even with correct syntax, a working script can become bug-prone and difficult for users to update. Here we document some tips
to help keep your scripts working as expected and easy to modify in the future.

Argument ordering
-----------------

As this is Python, ``genie_python`` conforms to the standard pattern of
calling Python functions. The arguments to the function are contained
within brackets and the variables passed in as a comma-separated list.
Ordering is important but can be overridden by using named variables,
for instance the following are all correct and equivalent:

::

    g.change_beamline_pars("PAR1",1)
    g.change_beamline_pars(name="PAR1",value=1)
    g.change_beamline_pars(value=1,name="PAR1")
    g.change_beamline_pars("PAR1",value=1)

In the last example, named and unnamed variables are mixed. Unnamed
variables must precede named variables. The following examples are not
valid

::

    g.change_beamline_pars(name="PAR1",1) # Named variable before unnamed
    g.change_beamline_pars(1,"PAR1") # Cannot change order of unnamed variables

Using named variables can be **very useful in avoiding mistakes**. For
instance, getting the order of high and low limits the wrong way round.
For instance this example:

::

    g.change_monitor(1,10,0)

is wrong and wouldn't work. Instead, we could have written:

::

    g.change_monitor(1,high=10,low=0)

which would have worked and makes it clear for whoever comes to edit the
code in future (hint: that person might be you!).

Making Errors Standout in Python Console
----------------------------------------

Python console will display most output in black this is from the standard out but will display error information in red. Error information should be written to standard error using `sys.stderr.write("error\n")`.

Some examples
========================

Sequentially sets a position (e.g. sample changer) and waits for a fixed number of uamps

::


    from genie_python import genie as g, BLOCK_NAMES as b
    
    def loop_over_samples(block_name, position_names, charge_to_wait_for):
        """
        Begins a run. Loops over a set of sample positions. Ends the run
        
        :param block_name: The name of the block containing the sample position
        :param position_names: A collection of the positions to loop over
        :param uamps_to_wait_for: The number of uamps to wait for between samples
        """
        g.begin()
        total_charge_to_wait_for = 0
        for position_name in position_names:
            print("Moving sample changer to position: {0}".format(position_name))
            g.cset(block_name, position_name)
            total_charge_to_wait_for += charge_to_wait_for
            g.waitfor_uamps(total_charge_to_wait_for)
        g.end()

Reads the value of a block and moves it through a series of intervals to a new values taking a fixed time

::

    from genie_python import genie as g, BLOCK_NAMES as b
    
    def ramp(time, block_name, steps=100, final_value=0.0):
        """
        Moves a block between an initial and target value over a sequence of steps, waiting a fixed time at each step.
        
        :param time: The overall time to take to ramp. Time will be split evenly between steps
        :param nsteps: The number of steps to take during the ramp
        :param block_name: The name of the block whose value to set
        :param final_value: The value we want to ramp to
        """
        
        initial_value = g.cget(block_name)['value']
        if initial_value is None:
            print("Unable to determine temperature from block {0}. No action will be taken".format(block_name))
            return
            
        def values_match(v1, v2):
            tolerance = 0.001
            small = 1.0e-20
            return 2*abs(v1-v2)/(abs(v1)+abs(v2)+small) < tolerance
        
        step_duration = time/steps
        for i in range(1, steps+1):
            step_value = initial_value + (final_value - initial_value)/steps*i
            g.cset(block_name, step_value)
            print("Ramping to: {0} Target value: {1}".format(step_value, final_value))
            g.waitfor_time(seconds=step_duration)
            new_block_value = g.cget(block_name)['value']
            if not values_match(new_block_value, step_value):
                print("WARNING: The current value for block {0}, {1}, does not match the target value of {2}".format(block_name, new_block_value, step_value))
        
        print("Ramp complete")
            