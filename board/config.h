#ifndef _BOARD_CONFIG_H_
#define _BOARD_CONFIG_H_

// =====================================================================
//  Pocket AI Assistant - Seeed XIAO ESP32-S3
//  INMP441 (micro I2S) + MAX98357A (ampli I2S) + OLED 0.96" I2C
//
//  Chan XIAO  ->  GPIO  ->  Noi vao
//   D0        ->  1     ->  INMP441 SCK
//   D1        ->  2     ->  INMP441 WS
//   D3        ->  4     ->  INMP441 SD
//   D4        ->  5     ->  OLED SDA
//   D5        ->  6     ->  OLED SCL
//   D8        ->  7     ->  MAX98357A DIN
//   D9        ->  8     ->  MAX98357A BCLK
//   D10       ->  9     ->  MAX98357A LRC
// =====================================================================

#include <driver/gpio.h>

#define AUDIO_INPUT_SAMPLE_RATE  16000
#define AUDIO_OUTPUT_SAMPLE_RATE 24000

// Micro va loa chay tren 2 cong I2S rieng (simplex), giong ban breadboard chinh thuc
#define AUDIO_I2S_MIC_GPIO_SCK  GPIO_NUM_1   // D0
#define AUDIO_I2S_MIC_GPIO_WS   GPIO_NUM_2   // D1
#define AUDIO_I2S_MIC_GPIO_DIN  GPIO_NUM_4   // D3

#define AUDIO_I2S_SPK_GPIO_DOUT GPIO_NUM_7   // D8
#define AUDIO_I2S_SPK_GPIO_BCLK GPIO_NUM_8   // D9
#define AUDIO_I2S_SPK_GPIO_LRCK GPIO_NUM_9   // D10

#define BUILTIN_LED_GPIO        GPIO_NUM_21  // LED vang tren XIAO (sang khi muc thap)
#define BUILTIN_LED_INVERT      1
#define BOOT_BUTTON_GPIO        GPIO_NUM_0   // nut BOOT tren board

#define DISPLAY_SDA_PIN GPIO_NUM_5           // D4
#define DISPLAY_SCL_PIN GPIO_NUM_6           // D5
#define DISPLAY_WIDTH   128

#if CONFIG_OLED_SSD1306_128X32
#define DISPLAY_HEIGHT  32
#elif CONFIG_OLED_SSD1306_128X64
#define DISPLAY_HEIGHT  64
#elif CONFIG_OLED_SH1106_128X64
#define DISPLAY_HEIGHT  64
#define SH1106
#else
#error "OLED display type is not selected"
#endif

// Lat man hinh 180 do neu chu bi nguoc (doi true/false)
#define DISPLAY_MIRROR_X true
#define DISPLAY_MIRROR_Y true

#endif // _BOARD_CONFIG_H_
