# Add blocks to run title

The value of a block can be embedded in a run title. This can be useful to differentiate the content of a run quickly at a glance.

The syntax to add a block to a run name is `@BLOCKNAME@` in the run title. For example:
```
Run with temperature @TEMPERATURE@ at angle @ANGLE@
```
where `TEMPERATURE` and `ANGLE` are the block names to be embedded. 
If the temperature was 298 and angle 180, the run title would be saved as `Run with temperature 298 at angle 180`.

This syntax can be used in both the IBEX GUI and through scripts.

## Things to note
 - The block **must** be logged.
 - The block names are case sensitive, so capitalisation must be constant.
 - The block value is updated in the title every time the block updates. Because of this, saving block values to the run title is best used when the values stay constant throughout the run. Otherwise the final value of the block will be saved in the title.
 - Blocks looking at binary or enumeration (BI/MBBI) fields will be saved only as their integer representation. For example, if a block could be 'on' or 'off', the saved value would be 0 or 1 rather than its string.