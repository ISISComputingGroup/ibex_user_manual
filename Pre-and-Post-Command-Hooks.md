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

An example of usage would be:

```python
>>> def before_begin_func(**pars):
  >>> cset(block1=100, wait=True) // Wait for block 1 to get to 100
>>>
>>> set_begin_pre_cmd(before_begin_func)
>>> begin()
```
