[[Scripting|scripting]] > [[Alerting on blocks|Alerts-on-Blocks]]

Alerts can be configured on blocks in python, the will trigger when a block is outside of the specified `lowlimit,highlimit` range for the specified `delay_out` time. When the value comes back in range, it must be in range for `delay_in` seconds until an in-range alert is sent. 
```
# set mobiles and emails to alert
g.alerts.set_sms(["123456", "789"])
g.alerts.set_email(["a@b", "c@d"])

# set alert on block1 with default delay_in and delay_out
g.alerts.set_range("block1", -10.0, 20.0)
# set alert on block2 with specified delay_in and delay_out
g.alerts.set_range("block2", -10.0, 20.0, 5.0, 5.0)

# enable alerts
g.alerts.enable("block1", True)
g.alerts.enable("block2", True)

g.cset("block1", -50) # A message will be sent to all specified phone numbers/emails to say the block has gone out of range
g.cset("block1", 0) # A message will be sent to all specified phone numbers/emails to say the block has gone back in range

# print alert status to screen
g.alerts.status()
```
