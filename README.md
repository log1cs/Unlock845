# Unlock845
## English
Unlock your LGE sdm845 phones has never been easier!

Before proceeding further, please check our [supported devices](https://github.com/log1cs/Unlock845/blob/main/SupportedDevices.md).

The script does not support Windows 7 and 8.1.

## How does this script works?

It'll flash an unsigned Oreo Prototype ABL taken from a V35 prototype version to your phone.

Does it brick your phone? No.

This unsigned ABL will only boot into system on a prototype phone, flashing it on a production phone will cause bootloader to return Red Case because it's not a signed image for production device and fall back to Bootloader mode (lol LG Electronics moment :tm: - usually it'll reboot to the opposite slot after a few failed tries), and this ABL image will allow you to have full bootloader mode control, allows you to unlock bootloader, flashing partitions and such under locked bootloader.

The script will then flash a patched FRP image with OEM unlock bit turned on (screw Verizon) and then unlock your phone's bootloader.

### Download the scripts in [Release](https://github.com/log1cs/Unlock845/releases).

## Preparation
* KDZ firmware file (preferred is Android 10 firmware, but it's up to you)
* Windows PC
* A cable with working data transfer

## How-to-start
- Reboot your phone into EDL mode.
- Follow the script's guide.
- Drag and drop your KDZ when asked, then press Enter.
- Done! Your bootloader will be unlocked.

## Frequently asked questions
### My phone showing Press any key to shut down, what should i do?
Use the FastbootFix included in the folder then reboot your phone in bootloader mode again. Run FastbootFix as administrator and it will work.

# Vietnamese
Unlock các thiết bị LG sdm845 chưa bao giờ dễ dàng hơn!

Trước khi bắt đầu, hãy [bấm vào đây](https://github.com/log1cs/Unlock845/blob/main/SupportedDevices.md) để tham khảo thêm về thiết bị được hỗ trợ.

Script không hỗ trợ các Windows 7 và Windows 8.1.

## Nguyên lý hoạt động
Bản chất thì script sẽ nạp 1 file ABL được lấy từ chiếc V35 phiên bản prototype.

Đương nhiên là nó không thể biến thiết bị của bạn thành cục chặn giấy được :D

File unsigned ABL trên chỉ có thể boot được vào hệ thống trên chính thiết bị prototype đó, và boot nó trên 1 chiếc máy thương mại sẽ khiến bootloader trả về Red Case vì image này không được sign và sẽ fallback về Bootloader Mode (thường thì nó sẽ khởi động lại sang boot slot khác sau vài lần khởi động lại thất bại), và ABL image này cho phép bạn toàn quyền sử dụng bootloader, cho phép bạn unlock bootloader, nạp phân vùng và nhiều thứ khác trong khi bootloader vẫn bị khoá.

Script sau đó sẽ nạp 1 file FRP đã được patch với bit OEM unlock đã được bất lên (vì máy Verizon không cho phép mở OEM unlock) và rồi sẽ unlock bootloader của thiết bị.

## Chuẩn bị
* Firmware (đuôi .kdz) - ưu tiên Android 10.
* Windows PC
* Sợi cáp có khả năng truyền dữ liệu tốt

## How-to-start
- Đưa thiết bị vào EDL mode.
- Làm theo chỉ dẫn được yêu cầu của script.
- Kéo thả file KDZ vào khi được hỏi và bấm Enter.
- Done!

## Câu hỏi thường gặp
### Thiết bị hiển thị "Press any key to shut down", thì tôi phải làm thế nào?
Dùng FastbootFix đặt trong thư mục của script, khởi động lại máy vào bootloader.

Lưu ý: Nhớ chạy FastbootFix dưới quyền administrator.

### How to enter EDL mode/Cách vào EDL Mode
![ezgif-1-7f9379ed0b3d](https://user-images.githubusercontent.com/60842977/132087777-a1b574f9-399b-485f-874b-0c536166055b.gif)

### English:
* Connect your USB cable to the computer. Then hold your Power Button and your Volume Down button till you see the screen goes black.
* As soon as the screen goes black, still hold Power and Volume Down, and press Volume Up repeatedly.
* Go to Device Manager, it will show you QHSUSB_BULK or Qualcomm HS-USB QLoader 9008 (COMx)
* If the phone reboots, do it again until you reach EDL mode.
### Vietnamese:
* Kết nối cáp từ điện thoại vào máy tính. Sau đó giữ nguồn và giảm âm lượng cho đến khi màn hình tắt đi.
* Khi màn hình tắt đi, vẫn giữ Nguồn và giảm âm lượng, hãy bấm tăng âm lượng liên tục.
* Mở Device Manager, bạn sẽ thấy QHSUSB_BULK hoặc Qualcomm HS-USB QLoader 9008(COMx)
* Nếu thiết bị khởi động lại, bắt đầu lại cho đến khi bạn vào được chế độ EDL.
