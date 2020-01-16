It is possible to hook in functions that run pre and post the execution of some genie commands (begin, end, abort, pause, resume). 

This is done passing functions to genie python setter commands. There are setter commands for begin, end, abort, pause and resume (func is the function you wish to run before or after the command):

- `set_begin_precmd(func)`
- `set_begin_postcmd(func)`
- `set_end_precmd(func)`
- `set_end_postcmd(func)`
- `set_abort_precmd(func)`
- `set_abort_postcmd(func)`
- `set_pause_precmd(func)`
- `set_pause_postcmd(func)`
- `set_resume_precmd(func)`
- `set_resume_postcmd(func)`

You only ever need to call the `set_<RUN_ACTION>_<>cmd(func)` once and func will then always be called for RUN_ACTIONs.

An example of usage would be:

```python
>>> def before_begin_func(**pars):
...    print("About to begin!!")
>>>
>>> set_begin_pre_cmd(before_begin_func) # Note the lack of brackets on before_begin_func here
>>> begin()
About to begin!!
** Beginning Run...
```
