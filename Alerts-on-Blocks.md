[[Scripting|scripting]] > [[Alerting on blocks|Alerts-on-Blocks]]

Alerts can be configured on blocks using genie python, there is no GUI for this at the moment. An alert will trigger when a block is outside of the specified `lowlimit,highlimit` range for the specified `delay_out` time, it is like run control but rather than putting the DAE into WAITING a message (via sms text and/or email) is sent. When the value comes back in range, it must be in range for `delay_in` seconds until an in-range alert is sent.

Note that this system is in addition to and independent of run control, it just uses some of the same underlying software. Alerts can be added to blocks that are not under run control, and both run control and alerts can bet set on the same block. The limits and delay times need not be the same for the run control and alert elements, so the instrument could be configured to go into a WAITING state when a block exceeded 100K but not send an alert until it exceeded 120K for a given length of time etc. (see below for how to set an alert on how long an instrument has been in a WAITING state)   
  
```python
## set mobiles and emails to send alerts to
## this is remembered and only needs to be repeated if values change 
g.alerts.set_sms(["123456789", "987654321"])
g.alerts.set_email(["a@b", "c@d"])

## set alert on block1 with default delay_in and delay_out (which is no delay)
## setting a range automatically enables the alert
g.alerts.set_range("block1", -10.0, 20.0)

## set alert on block2 with specified delay_in and delay_out times
## if you have a block value that may temporarily spike, but you are only
## interested in sustained periods out of range, then specify a delay_out
## so that e.g. it must be out of range for at least 15 seconds to trigger
## an out of range alert and back in range for at least 5 seconds to trigger
## an in range alert 
g.alerts.set_range("block2", -10.0, 20.0, delay_in=5.0, delay_out=15.0)

## alerts can be separately enabled and disabled, previous ranges
## and in/out delays are used
g.alerts.enable("block1", True)
g.alerts.enable("block2", False)

## print status of all configured alerts to screen
g.alerts.status()

## test
g.cset("block1", -50) # With above settings, message sent to say the block has gone out of range
g.cset("block1", 0) # With above settings, message sent to say the block has gone back in range
```
Alerts are saved across IBEX restarts, but the saving is not currently part of a configuration. The block related alert parameters will remain so long as the block exists (the email and sms parameters are always preserved), so you can change configuration and maintain an alert so long as the block continues to exists. If you change to a configuration where the block does not exist, then you lose those block specific alert settings. So it is best to create the blocks used for alerts as part of a common component included in all configurations.

Alerts, like run control, are normally set on floating point (or integer) value blocks. They can, however, be used on some "state" items that are symbolic names mapped to integers (enums). One example of this is the instrument state (SETUP=1,RUNNING=2,PAUSED=3,WAITING=4,VETOING=5) so if a block called `RunState` is attached to the process variable `IN:myinst:DAE:RUNSTATE` then
```python
g.alerts.set_range("RunState", -1.0, 3.5, delay_in=5.0, delay_out=300.0)
```   
will send an alert if the instrument has been WAITING or VETOING (>3.5) for more than 300 seconds.
 
## Sending alert messages directly from scripts
You can also send an immediate alert message from an executing script by doing the following
```python
## set mobiles and emails to alert, these aren't required if the email/phone numbers
## have already been set at some other point on your instrument
g.alerts.set_sms(["123456789", "987654321"])
g.alerts.set_email(["a@b", "c@d"])

if bad_thing_happened:
    g.alerts.send("Help, a bad thing has happened!")
```

## Future enhancements
* Create GUI for managing alerts, similar to how run control is done now
* Allow saving alerts into a configuration/component
    