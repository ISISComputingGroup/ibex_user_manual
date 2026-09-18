# Pre & Post-command Hooks

It is possible to hook in functions that run pre and post the execution of some genie commands (begin, end, abort, pause, resume). 

This is done passing functions to genie python setter commands. There are setter commands for begin, end, abort, pause and resume (func is the function you wish to run before or after the command):

- {external+genie_python:py:obj}`genie_advanced.set_begin_precmd`
    - This has a special case where the function returns None to say that after the function we should execute begin.
    - If anything else is returned the run does not begin but a string representation of whatever is returned will be printed to the user. A possible use of this is returning a string saying "Run already in progress, continuing run".
- {external+genie_python:py:obj}`genie_advanced.set_begin_postcmd`
- {external+genie_python:py:obj}`genie_advanced.set_end_precmd`
- {external+genie_python:py:obj}`genie_advanced.set_end_postcmd`
- {external+genie_python:py:obj}`genie_advanced.set_abort_precmd`
- {external+genie_python:py:obj}`genie_advanced.set_abort_postcmd`
- {external+genie_python:py:obj}`genie_advanced.set_pause_precmd`
- {external+genie_python:py:obj}`genie_advanced.set_pause_postcmd`
- {external+genie_python:py:obj}`genie_advanced.set_resume_precmd`
- {external+genie_python:py:obj}`genie_advanced.set_resume_postcmd`

You only ever need to call the `set_<RUN_ACTION>_<>cmd(func)` once and func will then always be called for subsequent RUN_ACTIONs.

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
