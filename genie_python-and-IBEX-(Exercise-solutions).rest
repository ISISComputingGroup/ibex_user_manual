Exercise 1
==========

From [[Getting Started|genie_python-and-IBEX-(Getting-started)]].

-   Opening a scripting window should be straightforward if IBEX is installed correctly. Once you've opened the scripting perspective, check for the following

    - Ideally the instrument will appear as ``SETUP``
    - The output when the scripting window opens should look a bit like this:

.. image:: genie_python_and_ibex/StandardStartupOutputOnDemo.png

-   To print the message, enter something like ``print "Hello, World!`` and press return

-   The square of the integers between 1 and 10 can be output with the code below. A **blank line** will indicate to the scripting window that you've finished writing the loop and it can go ahead and be executed.:

        for i in range(1,11):
            print i*i

Exercise 2
==========

From [[Common commands|genie_python-and-IBEX-(Common-commands)]]

- Use ``g.change_title("Exercise 2")`` to change the title
- The following code will start the run, wait, and then pause:

.. code-block:: python

    g.begin()
    g.waitfor_uamps(1)
    g.pause()

- This code sets the value, run control, and limits on "MY_BLOCK". Your code may look slightly different depending how you've chosen to pass in the arguments:

.. code-block:: python

    g.cset("MY_BLOCK", 5, lowlimit=1, highlimit=10, runcontrol=True)

- The following resumes the run:

.. code-block:: python

    g.resume()

- This code will set the block value and check the subsequent state:

.. code-block:: python

    # Can use either way of specifying cset for a single block
    g.cset(MY_BLOCK=20)

    # Can verify in any sensible way, so long as we're getting g.get_runstate()
    if g.get_runstate()=="WAITING":
        print "The instrument is waiting"
    else:
        print "The instrument is not waiting"

- The following code will scan the block from its original value down to 4. It assumes the initial value is greater than 4:

.. code-block:: python

    for i in range(int(g.cget("MY_BLOCK")['value']), 4, -1):
        g.cset(MY_BLOCK=i)
        g.waitfor_time(seconds=1)
        
- This function will end the run:

.. code-block:: python

     g.end()

Exercise 3
==========

From [[Scripting|genie_python-and-IBEX-(Scripting)]].

-   **(a)** After creating the files, you should have one new file in ``C:\scripts`` and another in ``C:\Instrument\Settings\config\[Instrument name]\Python\inst``

-   **(b)** The function in ``set_up_instrument.py`` should look something like this:

            def set_up_instrument():
                g.change_title("My experiment")
                g.change_user("Adrian")

-   **(b)** The function in ``run_my_experiment.py`` should look something like this:

.. code-block:: python

            def get_uamps_run():
                g.begin()
                # Assume this doesn't change
                period = g.get_period()
                for i in range(10):
                    print "Total current after {0}s: {1}.format(i+1, g.get_uamps(period))
                    g.waitfor_time(seconds=1)
                g.end()

-   **(c)** This will load the user script: ``g.load_script("run_my_experiment.py")``

-   **(d)** This will run the instrument script: ``inst.set_up_instrument()``

-   **(e)** This will run the function from the user script ``get_uamps_run()`` 

Exercise 4
==========

From [[Scripting|genie_python-and-IBEX-(Scripting)]].

-   You should have created a Python file in ``C:\Instrument\Settings\config\[Machine name]\Python\inst`` that contains something like the following:

.. code-block:: python

        from genie_python import genie as g

        def ramp(block, target):
            try:
                initial = g.cget(block)['value']
            except:
                print "Problem getting value for block {0}. Make sure it exists".format(block)
            else:
                g.change_title("Ramping {0} from {1} to {2}".format(block, initial, target))
                g.begin()

                current = initial
                small = 0.0001
                while abs(current-target) > small:
                    current = min(target, current + 1) if initial < target else max(target, current -1)
                    g.cset(block, current)
            finally: 
                g.end()

-   Once you add the line to output the current title, the top of your file should look like this:

.. code-block:: python

        print g.get_title()
        def ramp(block, target):
            ...

-   This user-defined function will ramp the two blocks using the instrument function:

.. code-block:: python

        def ramp_two_blocks():
            for block, target in [("MY_BLOCK", 10), ("MY_OTHER_BLOCK", -10)]:
                inst.ramp(block, target)

-   To load the user script, assuming the file is called "ramp_blocks.py", run the following from the scripting perspective:

.. code-block:: python

             g.load_script("C:\scripts\ramp_blocks.py")
             ramp_two_blocks()
      
-   You should have seen the current title printed during the initialisation of the scripting window

Exercise 5
==========

From [[Converting from Open GENIE|genie_python-and-IBEX-(Converting-from-Open-GENIE)]].

- In ``genie_python``, the ``Open GENIE`` procedure could be written as:

.. code-block:: python

     def scan(start=-100, min=100, max=200, step_size=20, nframes=10, nimages=10):
         for i in range(1, nimages+1):
              setpoint = (start + i*step_size) % 360
              print "New angle is: {0}".format(setpoint)

              if min <= setpoint <= max:
                  g.change_title("Image {0}: {1} degrees".format(i, setpoint))
                  g.cset(POSITION=setpoint)
                  g.waitfor_move()
                  
                  print "Move complete. Counting for {0} frames".format(nframes)
                  g.begin()
                  g.waitfor(frames=nframes)
                  g.end()
              else:
                  print "Not in interval {1}<={0}<={2}".format(setpoint, min, max)

-     We've made the following simplifications:
      
      - We've put the key variables as defaulted input arguments. This allows for maximal flexibility. In reality, which variables we put as arguments and which we default will depend on context. It's not recommended to put everything as an argument and always provide defaults
      -    We've taken advantage of several pieces of Python syntax to simplify the logic
 
           - ``"...".format(*args)`` for constructing strings
           - Defining a range as a single condition ``a <= b <= c``
           - Taking the modulo of a number using ``%`` to avoid extra calculations
           - Removing the unused line ``setpoint = 0.0``
           - Several commands are unnecessary in Python, namely ``LOCAL``, ``ENDLOOP``, ``ENDIF``, ``ENDPROCEDURE``