# Unlock845

**This project aimed to unlock your phone bootloader with only one script. Do it at your own risk!**

**Supported phones/Thiết bị được hỗ trợ:** 

[Click here./Bấm vào đây.](https://github.com/log1cs/Unlock845/blob/main/SupportedDevices.md)

# How this script works?

Basically it will flash a Prototype ABL taken from an LGE SDM845 phone and will trigger your phone to Fastboot mode. After that it will flash the FRP Image that has been patched (patched to get OEM Unlock enabled) and will unlock your bootloader in under ~2 minutes then it will reflash all of your phone partition to get you into download mode. After that it will ask for your KDZ (firmware file) to flash in download mode to prevent Fastboot mode loop.

**Caution: If you are Windows 7/8.1 users then use the W7_W8.1 version**



**Head to the Releases if you want to download the program!**

You can extract it in where you wanted to. (Huge thanks to [vvanloc](https://github.com/vvanloc) for making this) 

**Preparation**

- Your phone's KDZ
- Windows PC
- A cable with data transfer

**USAGE:**

1 - Reboot the phone in EDL mode

2 - Let the tool do the remaining thing, also do not forget to follow the tool steps. (Credit to [vvanloc](https://github.com/vvanloc) for making the tool auto detect the COM port, huge thanks)

3 - Drag and drop your KDZ when the tool asked

4 - Done! Your bootloader got unlocked

**Related**

How to enter EDL Mode on the V30/G7/V40/V50/G8/G8X:

![ezgif-1-7f9379ed0b3d](https://user-images.githubusercontent.com/60842977/132087777-a1b574f9-399b-485f-874b-0c536166055b.gif)

1 - Connect the cable. Then hold your Power Button and your Volume Down button till you see the screen goes black

2 - As soon as the screen goes black, still hold Power and Vol - , also press Vol + repeatedly.

3 - In Device Manager it will show you QHSUSB_BULK or Qualcomm HS-USB QLoader 9008(COMx)



**Vietnamese:**

# Script được chạy như thế nào?

Bản chất script sẽ nạp Prototype ABL (được lấy từ 1 máy mẫu dùng chip SDM845 của LGE) trong chế độ EDL. Khi nạp xong thì script sẽ nạp phân vùng FRP đã được patch để mở OEM Unlock và sẽ máy sẽ được unlock không dưới 2 phút. Khi unlock xong thì script sẽ nạp tất cả các phân vùng gốc trong máy lại và nhảy vào Download Mode.
Trong Download Mode thì script sẽ hỏi người dùng KDZ (file firmware của máy) và nạp để tránh hiện tượng treo ở Fastboot mode.

**Cảnh cáo: Nếu bạn là người dùng Windows 7 và Windows 8.1 thì hãy nhớ sử dụng phiên bản có dòng W7_8.1.**

 **Chuẩn bị**

- KDZ cho điện thoại của bạn
- Windows PC
- Một cái cáp có khả năng truyền dữ liệu

**Cách sử dụng**

1 - Khởi động lại vào EDL Mode

2 - Để tool làm nốt phần còn lại. Và hãy làm theo chỉ dẫn của tool.

3 - Kéo thả KDZ vào khi được hỏi và bấm Enter

4 - Xong! Bootloader đã được unlock

**Cách kết nối điện thoại vào EDL**

![ezgif-1-7f9379ed0b3d](https://user-images.githubusercontent.com/60842977/132087777-a1b574f9-399b-485f-874b-0c536166055b.gif)

1 - Kết nối cáp từ điện thoại vào máy tính. Sau đó giữ nguồn và giảm âm lượng cho đến khi màn hình đen.

2 - Khi màn hình tắt đi, vẫn giữ Nguồn và giảm âm lượng, và đồng thời bấm tăng âm lượng liên tục.

3 - Trong Device Manager sẽ hiển thị QHSUSB_BULK hoặc Qualcomm HS-USB QLoader 9008(COMx)


** FAQ: **

** My phone showing Press any key to shut down, what should i do? **

Use the FastbootFix included in the folder. Run it as administrator and it will work.
