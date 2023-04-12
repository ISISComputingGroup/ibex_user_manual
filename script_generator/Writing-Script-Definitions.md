These must be python 2/3 compatible see https://github.com/ISISComputingGroup/ibex_user_manual/wiki/Using-Futurize

# ScriptDefinition

For an example script definition see: [The ScriptDefinition Class (with Example)](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Script-generator-high-level-design#the-scriptdefinition-class). A script definition is defined by creating a class implementing a ScriptDefinition (a python interface) `class DoRun(ScriptDefinition):`. ScriptDefinition must be imported before doing this so add at the top of your file `from genie_python.genie_script_generator import ScriptDefinition `. 

To implement an ScriptDefinition this DoRun class must have methods `run`, `parameters_valid` and `get_help`. With `run` and `parameters_valid` signatures may look like this: `def run(self, temp="1", field="1"):`, `def parameters_valid(self, temp="1", field="1"):`.

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

Optionally a script definition can specify an `estimate_time` method, which will take the same arguments as `run` and `parameters_valid` and return a float giving an estimate of how long a script will take (in seconds). When defining this method we are returning how long each row in the script generator table will take to run.
```python
    def estimate_time(self, field1="1", field2="2"):
        return float(field1) * float(field2)
```
In order for this method to perform arithmetic operations on scientific notations, it is mandatory to cast the argument as float for e.g. `float(field1)`.

# Default values

The initial value of an action in the table can be defined within your script definition. Simply set the default values of the run method and these will be converted into a string for the initial value in the table. 

Please note that the value you put as a default will be passed through any casters when running. So for example with our `magnet_device_type` caster below the valid inputs into the action table are LF, TF, ZF or N/A which are cast to Danfysik, T20, Active ZF and N/A. When defining the default you should use the valid inputs for the actions table e.g. LF, TF, ZF or N/A.


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

## Copying from previous rows

`CopyPreviousRow` instances can be used to specify parameters in functions which should copy any previous row's value. This could be used to avoid re-specifying the values manually when creating a script. 

Usage: 

```python
from genie_python.genie_script_generator import ScriptDefinition, cast_parameters_to, CopyPreviousRow

class DoRun(ScriptDefinition):
    @cast_parameters_to(temperature=float_or_keep, field=float_or_keep, mevents=int, magnet_device=magnet_device_type)
    def run(self, temperature=CopyPreviousRow(1.0), field=1.0, mevents=10, magnet_device="N/A"):
       ...
```

The `temperature` field here would still have a default value of 1.0 if no actions exist, however if a user changes this value and adds another row it will be copied over to the next row.

# Using python, genie and inst

The script generator uses the python that we bundle with it which comes pre-installed with everything you would expect on an instrument (except inst) so you can easily write genie commands into your script definition etc. 

However, it does not come with installed instrument scripts that you obtain via inst. Due to this, if you try to import inst outside of your `run` method your script definition will produce errors for your users and fail to load when not on the instrument itself. Our suggestion is to import inst inside the run function and use it as normal in there: 

```python
def run(...):
   import inst
   inst.instrument_script_method()
```

# Global parameters

In a script definition you can define a number of global parameters by creating an ordered dictionary field for your `DoRun` class named `global_params_definition` e.g. 

```python
class DoRun(ScriptDefinition):

    global_params_definition = OrderedDict({"example param:": ("0", int), "example param 2:": ("2", float),
                                            "example param 3:": ("any string", str)})
```

These global parameters can then be accessed in the `run`, `parameters_valid` and other methods by calling `self.global_params["example param 2:"]`. The global parameters will appear above the actions table in the user interface and can be set by the user. The set value is applied for the entirety of the script.

## Validating global parameters

You can provide a validation function for global parameters. For example with `"example param 2:": ("2", float)` if we want to force it to be between 1 and 3, we can change `float` to be a function say `param2_validator` which we define in our script definition:

```python
from genie_python.genie_script_generator import ScriptDefinition, GlobalParamValidationError
from collections import OrderedDict

def param2_validator(param2) :
    param2 = float(param2)
    if param2 < 1 or param2 > 3:
        raise GlobalParamValidationError("Param 2 must be between 1 and 3")
    return param2


class DoRun(ScriptDefinition):
    global_params_definition = OrderedDict({"example param:": ("1", int), "example param 2:": ("1.23", param2_validator),
                                            "example param 3:": ("hello", str), "example param 4:": ("0", int)})
```

When `example param 2` is then set in the script generator, it will be validated using `param2_validator`.