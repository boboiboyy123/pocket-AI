# Pocket AI Assistant – firmware cho Seeed XIAO ESP32-S3

Cấu hình board riêng cho firmware mã nguồn mở [xiaozhi-esp32](https://github.com/78/xiaozhi-esp32) (v2.5.3),
dùng: XIAO ESP32-S3 + micro INMP441 + ampli MAX98357A + OLED 0.96" I2C.

- Giao diện màn hình: **tiếng Việt**
- Từ đánh thức (wake word): **"Alexa"**
- Nút bấm: nút **BOOT** trên XIAO

## Sơ đồ đấu dây

| Linh kiện | Chân linh kiện | Nối vào XIAO |
|---|---|---|
| **INMP441** | SCK | D0 |
| | WS | D1 |
| | SD | D3 |
| | VDD | 3V3 |
| | GND, L/R | GND |
| **MAX98357A** | DIN | D8 |
| | BCLK | D9 |
| | LRC | D10 |
| | Vin | Pin + (sau công tắc) |
| | GND | GND |
| | SD, GAIN | để trống |
| | Cọc + / − | 2 dây loa |
| **OLED** | SDA | D4 |
| | SCL | D5 |
| | VCC | 3V3 |
| | GND | GND |
| **Pin LiPo** | + | Công tắc → pad **BAT+** (mặt sau XIAO) |
| | − | pad **BAT−** |

Pin được sạc qua cổng USB-C của XIAO (bật công tắc khi sạc).

## Nút bấm

| Thao tác | Chức năng |
|---|---|
| Bấm 1 lần | Bắt đầu / kết thúc trò chuyện |
| Bấm 1 lần lúc vừa khởi động | Vào chế độ cài WiFi |
| Bấm 2 lần | Tăng âm lượng |
| Giữ lâu | Giảm âm lượng |

## Build firmware bằng GitHub (không cần cài gì)

1. Tạo repo mới trên GitHub, tải toàn bộ thư mục này lên.
2. Tab **Actions** sẽ tự build (khoảng 10–20 phút).
3. Mở lần chạy → mục **Artifacts** → tải:
   - `bread-compact-wifi-128x64` nếu dùng board **ESP32-S3 N16R8 DevKit**
   - `xiao-esp32s3-pocket` nếu dùng **XIAO** (OLED SSD1306), hoặc `xiao-esp32s3-pocket-sh1106` (OLED SH1106)
4. Giải nén ra `merged-binary.bin`, nạp bằng https://web.esphome.io (Connect → Install).

## Sửa chân

Mọi chân nằm trong `board/config.h`. Sửa xong tải lên lại, GitHub sẽ build lại.

## Đấu dây cho board ESP32-S3 N16R8 DevKit

| Linh kiện | Chân linh kiện | Nối vào board |
|---|---|---|
| **INMP441** | WS / SCK / SD | 4 / 5 / 6 |
| | VDD | 3V3 |
| | GND, L/R | GND |
| **MAX98357A** | DIN / BCLK / LRC | 7 / 15 / 16 |
| | Vin / GND | 5Vin / GND |
| **OLED** | SDA / SCL | 41 / 42 |
| | VCC / GND | 3V3 / GND |

Nút bấm: nút **BOOT** trên board.
