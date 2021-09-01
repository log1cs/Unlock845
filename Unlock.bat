echo off
title Unlocking LG 845 devices with just 1 click. Under development tbh.
echo =======================================================================================================================
echo 			  	    Unlocking your LG 845 devices bootloader with script                    
echo 			   Project under GPL-3.0 Public License. Created by Log1cs (github.com/log1cs)
echo =======================================================================================================================
echo Installing Qualcomm USB Driver for Mobile Phones
C:\Unlock845\Prerequisites\QualcommUSBDriver.exe
echo Installing LG Mobile Driver
C:\Unlock845\Prerequisites\LGMobileDriver_WHQL_Ver_4.8.0.exe
echo Installing Visual Studio Runtime 2013
C:\Unlock845\Prerequisites\vcredist_x86.exe /s
C:\Unlock845\Prerequisites\vcredist_x64.exe /s
echo Now plug your device in EDL mode, and press Enter.
pause
set /p var1="Enter COM port showing on the Device Manager, make sure you enter the right COM Port in Qualcomm HS-USB QLoader 9008(COMx) (Example: if it's showing COM6, you just press 6 in here en press enter, same with others): "
echo off 	
C:\Unlock845\tools\QFIL.exe -Mode=3 -COM=%var1% -RawProgram=C:\Unlock845\v35abl\rawprogram4.xml -Sahara=true -SEARCHPATH=C:\Unlock845\v35abl -RESETAFTERDOWNLOAD=true -AckRawDataEveryNumPackets=TRUE;100 -FLATBUILDPATH=C:\Unlock845\v35abl -PROGRAMMER=true;"C:\Unlock845\prog_ufs_firehose_Sdm845_lge.elf" -DEVICETYPE=ufs -DOWNLOADFLAT -RESETTIMEOUT=”10”
echo If you see the Red triangle then just ignore it, because you flashed the V35 engineering abl and the system just detected you modify the abl. No need to worry, just ignore it
echo If it stuck in the <waiting for devices>, then follow the step:
echo Step 1: Go to Device Manager, you should see Android with a yellow sign. If not, extend "Other devices", now you should see it
echo Step 2: Right click on it, select "Update Driver" or "Update Driver Software", then click "Browse my computer for drivers"
echo Step 3: Click on "Let me pick from a list of available on my computer"
echo Step 4: Click on "Show All Devices", then click "Have Disk", and click Browse. After that go to C:\Unlock845\Fastboot Driver(manually install it)
echo Step 5: Double-click on "android_winusb.inf" then select OK. Select Android Bootloader Interface and click Next. A warning should appears, just ignore it and press OK. Now you got Fastboot driver installed.
C:\Unlock845\tools\fastboot flash frp C:\Unlock845\v35abl\frp.img
C:\Unlock845\tools\fastboot reboot bootloader
timeout 3
echo Unlocking your Bootloader...
C:\Unlock845\tools\fastboot oem unlock
echo Rebooting to Bootloader one last time:
C:\Unlock845\tools\fastboot reboot bootloader
timeout 3
echo Checking your unlocked state:
C:\Unlock845\tools\fastboot getvar unlocked
timeout 5
echo Rebooting to EDL...
C:\Unlock845\tools\fastboot oem edl
timeout 5
C:\Unlock845\tools\QFIL.exe -Mode=3 -COM=%var1% -RawProgram=C:\Unlock845\ubl1\rawprogram0.xml,C:\Unlock845\ubl1\rawprogram1.xml,C:\Unlock845\ubl1\rawprogram2.xml,C:\Unlock845\ubl1\rawprogram3.xml,C:\Unlock845\ubl1\rawprogram5.xml,C:\Unlock845\ubl1\rawprogram6.xml -Sahara=true -SEARCHPATH=C:\Unlock845\ubl1 -RESETAFTERDOWNLOAD=true -AckRawDataEveryNumPackets=TRUE;100 -FLATBUILDPATH=C:\Unlock845\ubl1 -PROGRAMMER=true;"C:\Unlock845\prog_ufs_firehose_Sdm845_lge.elf" -DEVICETYPE=ufs -DOWNLOADFLAT -RESETTIMEOUT=”10”
echo Waiting for the device to reboot...
echo NOW IMMIDIATELY HOLD YOUR VOLUME+ KEY TO GO TO THE DOWNLOAD MODE. IF YOU SEE THE RED CASE JUST IGNORE IT, THE PHONE WILL AUTOMATICALLY GO TO DOWNLOAD MODE.
timeout 10
echo Starting LGUP_DEV 1.15.0.6...
echo Make sure to select correct KDZ of your model.
echo Crossflashing can cause lost VoLTE/VoWiFi function. Proceed at risk!
timeout 5
set /p var2="Enter COM port showing on the Device Manager, make sure you enter the right COM Port in LGE AndroidNet USB Serial Port(COMx) (Example: if it's showing COM10, you just press 10 in here en press enter, same with others): "
set /p var3="Now type your KDZ Path in here(need a full path, so enter it carefully or else the tool will fail to flash the KDZ) (Example: D:\G710N30g.kdz):  "
echo Flashing operation will start in 10 seconds.
echo DO NOT DISCONNECT THE CABLE WHILE FLASHING DEVICE!
timeout 10
echo FLASHING OPERATION STARTED!
C:\Unlock845\tools\LGUP_Cmd.exe com%var2% "C:\Unlock845\tools\LGUP_Common.dll" "%var3%" 
echo FLASHING OPERATION DONE!
echo Now wait for your phone to reboot. If you see the orange triangle with the text like "Your device can't be checked for corruption" then that is the sign of bootloader unlocked. Congrats!
echo Thank you for using the tool :D 
timeout 20
pause