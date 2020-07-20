[[Scripting|scripting]] > [[Alerting on blocks|Alerts-on-Blocks]]

Alerts can be configured on blocks using genie python, there is no GUI for this at the moment. Am alert will trigger when a block is outside of the specified `lowlimit,highlimit` range for the specified `delay_out` time, it is like run control but rather than putting the DAE into WAITING a message is sent. When the value comes back in range, it must be in range for `delay_in` seconds until an in-range alert is sent. 
```
## set mobiles and emails to alert
g.alerts.set_sms(["123456789", "987654321"])
g.alerts.set_email(["a@b", "c@d"])

## set alert on block1 with default delay_in and delay_out (2 seconds)
## setting a range automatically enabled the alert
g.alerts.set_range("block1", -10.0, 20.0)
## set alert on block2 with specified delay_in and delay_out times
g.alerts.set_range("block2", -10.0, 20.0, delay_in=5.0, delay_out=5.0)

## alerts can be separately enabled and disabled
g.alerts.enable("block1", True)
g.alerts.enable("block2", False)

## print status of all configured alerts to screen
g.alerts.status()

## test
g.cset("block1", -50) # With above settings, a message would be sent to say the block has gone out of range
g.cset("block1", 0) # With above settings, a message would be sent to say the block has gone back in range
```
