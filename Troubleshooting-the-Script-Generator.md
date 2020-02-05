## Cannot import inst

When using the script generator not on an instrument the instrument scripts will not be available. This means we cannot import inst.

Therefore we cannot use inst outside of the `run` function. Our suggestion is to `import inst` inside the run function and use it as normal in there: 

```python
def run(...):
    import inst
    inst.instrument_script_method()
```

## Warning: Could not load any configs from 

- The configs have not been loaded into the correct place in the filesystem
   - To fix simply move them into the location that is given in the warning message
- The place IBEX is looking for configs in the file
   - See "Want your configs to be loaded from ...?" below
- It is possible the configs have errors in them
   - The script generator will display a table detailing these errors if this is the case
   - Please review your configs keeping in mind the errors detailed in the table
- If it is none of these there is a chance it is because part of the script generator has crashed
   - Please contact the IBEX team to see if it is a bug: see [How do I report a problem with IBEX?](https://github.com/ISISComputingGroup/ibex_user_manual/wiki/FAQ#id1)

## Some of my configs have not loaded

- The config may be placed in the wrong place 
   - Please place your config on the filesystem where your configs are loaded from
- One of the locations where configs are loaded from may be incorrect 
   - See "Want your configs to be loaded from ...?" below
- Some of the configs may have errors in the and so failed to load
   - These errors will be displayed in a table in the script generator graphical user interface
   - Please fix the script or ask the maintainer of the script to fix it

## I get a blank screen where the script generator should be

Please contact the IBEX team to see if it is a bug: see [How do I report a problem with IBEX?](https://github.com/ISISComputingGroup/ibex_user_manual/wiki/FAQ#id1)

## My script generator never finished loading

Please contact the IBEX team to see if it is a bug: see [How do I report a problem with IBEX?](https://github.com/ISISComputingGroup/ibex_user_manual/wiki/FAQ#id1)