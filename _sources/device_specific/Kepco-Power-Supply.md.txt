# KEPCO Power Supply

KEPCO power supply units (PSU) come in various sizes and models. The two major differences are analogue (i.e. the PSU has analogue dials on the front panel) and digital (i.e. the PSU has digital readbacks on the front panel). 

KEPCO PSUs run in two modes:

1. Voltage Mode
    - Setting voltage means the KEPCO will supply will try to maintain the requested (+ve or -ve) voltage
    - In voltage mode, the current that is set will be the maximum allowed current. I.e. If the resistance is low then to reach the desired voltage a current larger than the setpoint will be needed, so the KEPCO will not reach the desired voltage.
1. Current Mode
    - Setting a current will mean the KEPCO will supply the given current.
    - In current mode, the voltage that is set will be the maximum allowed current.

## Macros

`RESET_ON_START` This macro controls whether the ioc resets and resends parameters on start of the IOC and can be set to 0, 1 or 2. 

- 0 tells the IOC to not reset and resend setpoints on startup
- 1 tells the IOC to reset and resend setpoints if the firmware is less than version 2.0
- 2 tells the IOC to reset and resend setpoints no matter what the firmware version is

## Troubleshooting

### Current/voltage will not go negative when I set the current/voltage

If the device is in voltage mode then the sign of the current will be set by the voltage, not the current and vice-versa. 

### Current/voltage does not reach the value set

For voltage mode, check the current setting is high enough (see voltage mode above). In current mode, check that the voltage is set high enough (see current mode above).
