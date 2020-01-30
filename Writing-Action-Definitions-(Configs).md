These must be python 2/3 compatible see https://github.com/ISISComputingGroup/ibex_user_manual/wiki/Using-Futurize

# ActionDefinition

A config is defined by creating a class implementing an ActionDefinition (a python interface) `class DoRun(ActionDefinition):`. ActionDefinition must be imported before doing this so add at the top of your file `from genie_python.genie_script_generator import ActionDefinition`. 

To implement an ActionDefinition this DoRun class must have methods `run`, `parameters_valid` and `get_help`. With `run` and `parameters_valid` signatures may look like this: `def run(self, temp="1", field="1"):`, `def parameters_valid(self, temp="1", field="1"):`.

Both `run` and `parameters_valid` methods must take the same arguments (in this case `temp="1", field="1"`) and must have the `self` argument first. All the arguments except self must have a default value in our example "1" is the defaults. All the arguments taken except for `self` are of type string, if you want to change this see "Casting Parameters" below.

When defining a `get_help` method we are returning a string that we want to be displayed to the users in the script generator UI, for example:

```python
def get_help(self):
   return "My help string"
``` 

If we do not want to display a string to the user we return None:


```python
def get_help(self):
   return None
``` 


# Casting Parameters

## cast_parameters_to

This decorator allows you to cast the parameters you receive for your `run` and `parameters_valid` methods, for example:

```python
@cast_parameters_to(temp=float, field=float)
def run(self, temp=1.0, float=1.0):
```

Here we pass temp a cast called float. This will call `float(temp)` on whatever is passed to `run` before `run` is called so you can treat temp as a floating-point number. If casting the input fails this will be propagated back up to the user. Other casters include int, long and hex. If there does not exist a caster that fits your specification you can write one yourself see "Custom Casters".

## Custom Casters

When float, int etc. are not enough you can define your own function to cast an input. These take one argument (the argument to cast) and return the casted value. See examples below for details.

Say we want our users to be able to input a floating-point value for the temperature, but we also want them to be able to input the word "KEEP" or even "KeEp" to not change the value we can define the caster below:

```python
def float_or_keep(temp):
    if temp.lower() == "keep":
        return None
    else:
        return float(temp)
```

Say we have a set of magnets that we are wanting the user to select in an argument (or no magnet "N/A") we can define the below caster:

```python 
magnet_devices = {"ZF": "Active ZF", "LF": "Danfysik", "TF": "T20 Coils"}

# Convert to magnet device type if possible, if not they have input an incorrect magnet_device
# Raise a ValueError and this will be caught and displayed to the user that the conversion is incorrect 
def magnet_device_type(magnet_device):
    magnet_device = magnet_device.upper()
    if magnet_device in magnet_devices.keys():
        return magnet_devices[magnet_device]
    elif magnet_device == "N/A":
        return magnet_device
    raise ValueError("Magnet device must be one of {} or N/A".format(magnet_devices))
```

To say we cannot cast the argument we raise a ValueError which tells cast_parameters_to that we have failed to cast the argument. The string you type into the ValueError (e.g. "Magnet device must be one of {} or N/A".format(magnet_devices))  will be propagated back up to the user.

# Using python, genie and inst

The script generator uses the python that we bundle with it which comes pre-installed with everything you would expect on an instrument (except inst) so you can easily write genie commands into your config etc. 

However, it does not come with installed instrument scripts that you obtain via inst. Due to this, if you try to import inst outside of your `run` method your config will produce errors for your users and fail to load when not on the instrument itself. Our suggestion is to import inst inside the run function and use it as normal in there: 

```python
def run(...):
   import inst
   inst.instrument_script_method()
```
