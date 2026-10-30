"""Chep board XIAO ESP32-S3 Pocket vao ma nguon xiaozhi-esp32 va dang ky no.

Cach dung: python apply_board.py <thu_muc_xiaozhi-esp32>
Chay nhieu lan cung khong sao (idempotent).
"""
import shutil
import sys
from pathlib import Path

SYMBOL = "BOARD_TYPE_SEEED_XIAO_ESP32S3_POCKET"
BOARD_DIR = "seeed/xiao-esp32s3-pocket"

root = Path(sys.argv[1]).resolve()
here = Path(__file__).resolve().parent.parent

# 1. Chep 3 file cau hinh board
dest = root / "main" / "boards" / BOARD_DIR
dest.mkdir(parents=True, exist_ok=True)
for f in (here / "board").iterdir():
    shutil.copy2(f, dest / f.name)

# 2. Them board vao menu Kconfig + cho phep chon loai OLED
kconfig = root / "main" / "Kconfig.projbuild"
k = kconfig.read_text(encoding="utf-8")
if f"config {SYMBOL}" not in k:
    anchor = "    config BOARD_TYPE_SEEED_XIAO_ESP32S3_RESPEAKER_XVF3800\n"
    if anchor not in k:
        sys.exit("Khong tim thay vi tri chen board trong Kconfig.projbuild")
    k = k.replace(anchor,
        f"    config {SYMBOL}\n"
        '        bool "Seeed XIAO ESP32-S3 Pocket (INMP441 + MAX98357A + OLED)"\n'
        "        depends on IDF_TARGET_ESP32S3\n" + anchor, 1)
oled = "choice DISPLAY_OLED_TYPE\n    depends on "
if oled + SYMBOL not in k:
    if oled not in k:
        sys.exit("Khong tim thay muc DISPLAY_OLED_TYPE trong Kconfig.projbuild")
    k = k.replace(oled, oled + SYMBOL + " || ", 1)
kconfig.write_text(k, encoding="utf-8")

# 3. Cho CMake biet thu muc board
cmake = root / "main" / "CMakeLists.txt"
c = cmake.read_text(encoding="utf-8")
if f"CONFIG_{SYMBOL})" not in c:
    anchor = "elseif(CONFIG_BOARD_TYPE_SEEED_XIAO_ESP32S3_RESPEAKER_XVF3800)"
    if anchor not in c:
        sys.exit("Khong tim thay vi tri chen board trong main/CMakeLists.txt")
    c = c.replace(anchor,
        f"elseif(CONFIG_{SYMBOL})\n"
        f'    set(BOARD_DIR "{BOARD_DIR}")\n'
        "    set(BUILTIN_TEXT_FONT font_noto_sans_basic_14_1)\n"
        "    set(BUILTIN_ICON_FONT font_material_symbols_14_1)\n" + anchor, 1)
    cmake.write_text(c, encoding="utf-8")

print("Da them board", BOARD_DIR)
