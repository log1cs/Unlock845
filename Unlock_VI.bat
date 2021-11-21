echo off
title Unlock Bootloader cac thiet bi LG chay Snapdragon 845 bang script. Dang trong giai doan phat trien.
echo =======================================================================================================================
echo 			  	       Unlock Bootloader cua LG 845 bang tap lenh (LG G7)                  
echo 			   Project under GPL-3.0 Public License. Duoc tao boi Log1cs (github.com/log1cs)
echo =======================================================================================================================

set currentpath=%~dp0


echo Gio hay ket noi dien thoai o che do EDL(9008), va sau do nhan Enter.
pause
powershell -Command "$temp=Get-WmiObject -Class Win32_PnPEntity | where { $_.Description -eq 'Qualcomm HS-USB QDLoader 9008' } | Select-Object Name | out-string;  $temp=[Regex]::Matches($temp, '(?<=\()(.*?)(?=\))') | Select -ExpandProperty Value; $temp.SubString(3, $temp.length-3)" > comport
set /p COM=<comport
del comport
%currentpath%tools\QFIL.exe -Mode=3 -COM=%COM% -RawProgram=%currentpath%v35abl\rawprogram4.xml -Sahara=true -SEARCHPATH=%currentpath%v35abl -RESETAFTERDOWNLOAD=true -AckRawDataEveryNumPackets=TRUE;100 -FLATBUILDPATH=%currentpath%v35abl -PROGRAMMER=true;"%currentpath%prog_ufs_firehose_Sdm845_lge.elf" -DEVICETYPE=ufs -DOWNLOADFLAT -RESETTIMEOUT=”10”
echo Neu ban thay tam giac mau do, thi cu ke no. Tai vi ban vua nap abl cua V35 vao nen he thong bao Red Case, doi 1 phut sau no se vao fastboot
echo Neu bi ket o <waiting for devices>, thi lam cac buoc sau day:
echo Step 1: Vao Device Manager, ban se thay muc Android voi dau cham than mau vang. Neu khong thay, Bam > o phan "Other devices" la duoc.
echo Step 2: Click chuot phai vao, chon "Update Driver" hoac "Update Driver Software", sau do "Browse my computer for drivers"
echo Step 3: Click "Let me pick from a list of available on my computer"
echo Step 4: Click vao "Show All Devices", sau do click "Have Disk", va click Browse. Sau do vao duong dan sau %currentpath%Fastboot Driver(manually install it)
echo Step 5: Click dup chuot vao "android_winusb.inf" va sau do chon OK. Sau do chon Android Bootloader Interface va click Next. Se co canh cao hien len, bo qua no va nhan OK. Gio thi ban da cai duoc driver Fastboot.
%currentpath%tools\fastboot flash frp %currentpath%v35abl\frp.img
%currentpath%tools\fastboot reboot bootloader
timeout 3
echo Dang Unlock Bootloader...
%currentpath%tools\fastboot oem unlock
echo Khoi dong lai bootloader lan cuoi:
%currentpath%tools\fastboot reboot bootloader
timeout 3
echo Kiem tra tinh trang Unlock Bootloader(neu unlocked:yes thi la mo roi):
%currentpath%tools\fastboot getvar unlocked
timeout 5
echo Dang khoi dong lai vao EDL...
%currentpath%tools\fastboot oem edl
timeout 5
echo Dang nap phan vung...
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
echo Thiet bi se khoi dong lai trong 5s...
echo Gio hay giu tang am luong de vao Download Mode. Neu nhu ban thay tam giac mau do 1 lan nua, ke no, cu giu tang am luong roi no se tu vao Download Mode.
timeout 5
%currentpath%tools\fastboot reboot
echo Neu may da vao Download Mode roi thi nhan Enter.
pause
echo Dang khoi dong LGUP_DEV 1.15.0.6...
echo Hay chac chan la ban chon dung KDZ cua model ban dang dung.
echo Nap firmware cua may khac co the dan den mat VoLTE/VoWiFi. Can than truoc khi lam!
timeout 5
powershell -Command "$temp=Get-WmiObject -Class Win32_PnPEntity | where { $_.Description -eq 'LGE AndroidNet USB Serial Port' } | Select-Object Name | out-string;  $temp=[Regex]::Matches($temp, '(?<=\()(.*?)(?=\))') | Select -ExpandProperty Value; $temp.SubString(3, $temp.length-3)" > comport
set /p COMB=<comport
del comport
set /p var3="Gio hay keo tha KDZ cua ban vao day, roi sau do bam Enter:  "
echo Tien trinh flash KDZ se duoc bat dau trong 10 giay nua...
echo KHONG DUOC RUT THIET BI TRONG LUC DANG FLASH KDZ!
timeout 10
echo QUA TRINH NAP KDZ BAT DAU!
%currentpath%tools\LGUP_Cmd.exe com%COM% "%currentpath%tools\LGUP_Common.dll" "%var3%" 
echo QUA TRINH NAP KDZ XONG!
echo Gio hay doi may khoi dong lai. Neu dien thoai hien tam giac mau cam va co them dong chu "Your device can't be checked for corruption" thi do nghia la may ban da Unlock Bootloader thanh cong.
echo Cam on vi da su dung tool :D 
timeout 20
pause
