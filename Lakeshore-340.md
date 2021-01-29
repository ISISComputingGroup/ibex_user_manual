Guide on Lakeshore 340 excitation thresholds.

They are loaded from the instrument config area for example on LET `NDXLET\configurations\excitation_thresholds`. They are `.txt` files where each line is a pair of temperature threshold and excitation value in that order separated by a comma, for example:

```
20,30 nA
15,1 mV
18,100 nA
```

The file is read from top to bottom and the first temperature threshold that is greater than the temperature setpoint on the lakeshore 340 is the line that is selected. Subsequently, the IOC will wait for the temperature to reach the setpoint and then set the excitation to the value on the same file line as the matching temperature threshold. If no temperature threshold is found to match the file then the last excitation listed in the file will be set.

The default file is None.txt if you leave the file to this then no writing of excitations will occur from this mechanism. 

If the set file contains invalid values or does not exist then the OPI will display this on the excitations tab. 