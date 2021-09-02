echo off
title Unlocking LG 845 devices with just 1 click. Under development.
echo =======================================================================================================================
echo 			  	    Unlocking your LG 845 devices bootloader with script                    
echo 			   Project under GPL-3.0 Public License. Created by Log1cs (github.com/log1cs)
echo =======================================================================================================================

set currentpath=%~dp0

echo Installing Qualcomm USB Driver for Mobile Phones
%currentpath%Prerequisites\QualcommUSBDriver.exe
echo Installing LG Mobile Driver
%currentpath%Prerequisites\LGMobileDriver_WHQL_Ver_4.8.0.exe /s
echo Installing Visual Studio Runtime 2013
%currentpath%Prerequisites\vcredist_x86.exe /s
%currentpath%Prerequisites\vcredist_x64.exe /s
echo Now plug your device in EDL mode, and press Enter.
pause
powershell -Command "$temp=Get-WmiObject -Class Win32_PnPEntity | where { $_.Description -eq 'Qualcomm HS-USB QDLoader 9008' } | Select-Object Name | out-string;  $temp=[Regex]::Matches($temp, '(?<=\()(.*?)(?=\))') | Select -ExpandProperty Value; $temp.SubString(3, $temp.length-3)" > comport
set /p COM=<comport
del comport
%currentpath%tools\QFIL.exe -Mode=3 -COM=%COM% -RawProgram=%currentpath%v35abl\rawprogram4.xml -Sahara=true -SEARCHPATH=%currentpath%v35abl -RESETAFTERDOWNLOAD=true -AckRawDataEveryNumPackets=TRUE;100 -FLATBUILDPATH=%currentpath%v35abl -PROGRAMMER=true;"%currentpath%prog_ufs_firehose_Sdm845_lge.elf" -DEVICETYPE=ufs -DOWNLOADFLAT -RESETTIMEOUT=”10”
echo If you see the Red triangle then just ignore it, because you flashed the V35 engineering abl and the system just detected you modify the abl. No need to worry, just ignore it
echo If it stuck in the <waiting for devices>, then follow the step:
echo Step 1: Go to Device Manager, you should see Android with a yellow sign. If not, extend "Other devices", now you should see it
echo Step 2: Right click on it, select "Update Driver" or "Update Driver Software", then click "Browse my computer for drivers"
echo Step 3: Click on "Let me pick from a list of available on my computer"
echo Step 4: Click on "Show All Devices", then click "Have Disk", and click Browse. After that go to %currentpath%Fastboot Driver(manually install it)
echo Step 5: Double-click on "android_winusb.inf" then select OK. Select Android Bootloader Interface and click Next. A warning should appears, just ignore it and press OK. Now you got Fastboot driver installed.
%currentpath%tools\fastboot flash frp %currentpath%v35abl\frp.img
%currentpath%tools\fastboot reboot bootloader
timeout 3
echo Unlocking your Bootloader...
%currentpath%tools\fastboot oem unlock
echo Rebooting to Bootloader one last time:
%currentpath%tools\fastboot reboot bootloader
timeout 3
echo Checking your unlocked state:
%currentpath%tools\fastboot getvar unlocked
timeout 10
echo Flashing necessary partition...
%currentpath%tools\fastboot erase laf_a
%currentpath%tools\fastboot erase abl_a
%currentpath%tools\fastboot erase abl_b
%currentpath%tools\fastboot erase laf_b
%currentpath%tools\fastboot erase dtbo_a
%currentpath%tools\fastboot erase dtbo_b 
%currentpath%tools\fastboot flash laf_a %currentpath%tools\laf.bin
%currentpath%tools\fastboot flash laf_b %currentpath%tools\laf.bin
%currentpath%tools\fastboot flash abl_a %currentpath%tools\abl.bin
%currentpath%tools\fastboot flash abl_b %currentpath%tools\abl.bin
%currentpath%tools\fastboot flash dtbo_a %currentpath%tools\dtbo.bin
%currentpath%tools\fastboot flash dtbo_b %currentpath%tools\dtbo.bin
echo Device will REBOOT in 5 seconds!
echo NOW IMMIDIATELY HOLD YOUR VOLUME+ KEY TO GO TO THE DOWNLOAD MODE. IF YOU SEE THE RED CASE JUST IGNORE IT, THE PHONE WILL AUTOMATICALLY GO TO DOWNLOAD MODE.
timeout 5
%currentpath%tools\fastboot reboot
echo If your phone connected in Download Mode, then press Enter.
pause
echo Starting LGUP_DEV 1.15.0.6...
echo Make sure to select correct KDZ of your model.
echo Crossflashing can cause lost VoLTE/VoWiFi function. Proceed at risk!
timeout 5
powershell -Command "$temp=Get-WmiObject -Class Win32_PnPEntity | where { $_.Description -eq 'LGE AndroidNet USB Serial Port' } | Select-Object Name | out-string;  $temp=[Regex]::Matches($temp, '(?<=\()(.*?)(?=\))') | Select -ExpandProperty Value; $temp.SubString(3, $temp.length-3)" > comport
set /p COMB=<comport
del comport
set /p var3="Drag and drop your KDZ in the tool (Example: D:\G710N30g.kdz):  "
echo Flashing operation will start in 10 seconds.
echo DO NOT DISCONNECT THE CABLE WHILE FLASHING DEVICE!
timeout 10
echo FLASHING OPERATION STARTED!
%currentpath%tools\LGUP_Cmd.exe com%COMB% "%currentpath%tools\LGUP_Common.dll" "%var3%" 
echo FLASHING OPERATION DONE!
echo Now wait for your phone to reboot. If you see the orange triangle with the text like "Your device can't be checked for corruption" then that is the sign of bootloader unlocked. Congrats!
echo Thank you for using the tool :D 
timeout 20
pause