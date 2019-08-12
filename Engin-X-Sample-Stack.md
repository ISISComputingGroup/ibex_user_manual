# Define a Motor Position on the Engin-X Sample Stack
- Using a file explorer, go to the following location on `ndxenginx`: `C:\Labview Modules\Drivers\Galil DMC2280`
![](https://raw.githubusercontent.com/wiki/ISISComputingGroup/ibex_user_manual/enginx_sample_stack_1.png)
- Double click on the file Galil – System Functions.llb
![](https://raw.githubusercontent.com/wiki/ISISComputingGroup/ibex_user_manual/enginx_sample_stack_2.png)
- Double click on the file in the top section called “Galil – Table of motor details.vi”. The following LabVIEW vi will appear – but populated with the motors for ENGINX
![](https://raw.githubusercontent.com/wiki/ISISComputingGroup/ibex_user_manual/enginx_sample_stack_3.png)
- IMPORTANT: Select the correct motor on the left hand side.
- Select the tab called Tools. 
![](https://raw.githubusercontent.com/wiki/ISISComputingGroup/ibex_user_manual/enginx_sample_stack_4.png)
- Select “Enable” 
![](https://raw.githubusercontent.com/wiki/ISISComputingGroup/ibex_user_manual/enginx_sample_stack_5.png)
- Enter the new position in “Define Motor Position”. 
- Enter the new position in “Define Encoder Position”
- Click the two “Apply” buttons next to these controls
![](https://raw.githubusercontent.com/wiki/ISISComputingGroup/ibex_user_manual/enginx_sample_stack_6.png)
- Minimise the vi (DO NOT STOP the VI). IBEX uses this in the background to perform the motion control for the sample stack.
