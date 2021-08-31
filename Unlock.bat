echo off
title Unlocking LG 845 devices with just 1 click. Under development tbh.
echo WARNING: YOU SHOULD REMEMBER WHAT IS YOUR STOCK FIRMWARE VERSION BEFORE DOING THIS!
echo =======================================================================================================================
echo 			  Unlocking your LG 845 devices bootloader with just 1 click, or maybe more lol                    
echo 			   Project under GPL-3.0 Public License. Created by Log1cs (github.com/log1cs)
echo					  Under development. Subject to change.              
echo =======================================================================================================================
set /p var1="Enter COM port showing on the Device Manager, make sure you enter the right COM Port in Qualcomm HS-USB QLoader 9008(COMx): "
echo off 	
QFIL.exe -Mode=3 -COM=%var1% -RawProgram=C:\Unlock845\rawprogram4.xml -Sahara=true -SEARCHPATH=C:\Unlock845 -RESETAFTERDOWNLOAD=true -AckRawDataEveryNumPackets=TRUE;100 -FLATBUILDPATH=C:\Unlock845 -PROGRAMMER=true;"C:\Unlock845\prog_ufs_firehose_Sdm845_lge.elf" -DEVICETYPE=ufs -DOWNLOADFLAT -RESETTIMEOUT=”10”
echo If you see the Red triangle then just ignore it, because you flashed the V35 engineering abl and the system just detected you modify the abl. No need to worry, just ignore it
fastboot flash frp C:\Unlock845\frp.img
fastboot reboot bootloader
timeout 3
echo Unlocking your Bootloader...
fastboot oem unlock
echo Rebooting to Bootloader one last time:
fastboot reboot bootloader
timeout 3
echo Checking your unlocked state:
fastboot getvar unlocked
echo Rebooting to EDL...
fastboot oem edl
timeout 5
QFIL.exe -Mode=3 -COM=%var1% -RawProgram=rawprogram0.xml,rawprogram1.xml,rawprogram2.xml,rawprogram3.xml,rawprogram5.xml,rawprogram6.xml -Sahara=true -SEARCHPATH=C:\Unlock845 -RESETAFTERDOWNLOAD=true -AckRawDataEveryNumPackets=TRUE;100 -FLATBUILDPATH=C:\Unlock845 -PROGRAMMER=true;"C:\Unlock845\prog_ufs_firehose_Sdm845_lge.elf" -DEVICETYPE=ufs -DOWNLOADFLAT -RESETTIMEOUT=”10”
echo Waiting for the device to reboot...
timeout 10
echo NOW IMMIDIATELY HOLD YOUR VOLUME+ KEY TO GO TO THE DOWNLOAD MODE
echo Bootloader unlock successfully, now go to the Download mode and flash your KDZ using Refurbish/Partition DL!
echo Thanks for using the tool!
pause