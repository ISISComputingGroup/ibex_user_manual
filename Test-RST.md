-    ``get_blocks``: Gets a list of the currently available blocks
-    ``cshow``: Shows the properties of a named block/all blocks

     - If given a name (e.g. ``MY_BLOCK``) it will return a string containing properties of the block
         - Example: ``MY_BLOCK = 10 (runcontrol = NO, lowlimit = 0.0, highlimit = 0.0)``
     - If called without arguments, it will show the same information for all blocks, with each block on a new line

-    ``cget``: Gets properties of a named block as a dictionary of values

     - Example: ``MY_BLOCK = 10 (runcontrol = NO, lowlimit = 0.0, highlimit = 0.0)``
     - Unlike ``cshow``, a block name must be specified
     - Properties can be accessed as standard Python::

          block_info = g.cget("MY_BLOCK")
          name = block_info("name")
          value = block_info("value")
          print "The value of block {0} is {1}".format(name, value)

-    ``cset``: Sets the value for a particular block

     - Assumes that either a setpoint exists for the underlying value or the block itself points at a setpoint
     - Can be called with block names as named arguments. This is useful for setting multiple blocks
          - Example: ``g.cset(MY_BLOCK=1, MY_OTHER_BLOCK=2)``
     - The block can also be passed in by name. This is useful when setting advanced block properties
          - Example: ``g.cset("MY_BLOCK", lowlimit=1, highlimit=10, runcontrol=True)``