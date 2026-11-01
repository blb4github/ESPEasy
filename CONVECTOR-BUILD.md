# PET10 V2 convector firmware — experimental compact build

Base: official ESPEasy `mega-20260720`, commit `8ceb5eeeb1dad281196f072f2fec9e43469f8798`.
Branch: `convector-v2-mega-20260720`. **Do not merge into upstream or flash production devices yet.**

## Target

PlatformIO environment: `convector_ESP8266_4M1M` defined in `platformio_esp82xx_envs.ini`.

Build locally:

```sh
pio run -e convector_ESP8266_4M1M
```

Plugin selection is isolated in `tools/pio/pre_convector_esp82xx.py`:

- P003 Generic Pulse Counter — tach input
- P004 Dallas — DS18B20
- P005 DHT — DHT22
- P026 System Info — existing Status task
- P033 Dummy — control/configuration/validity tasks
- P037 MQTT Import — presence and heat-pump MQTT
- C002 MQTT controller — Publish from rules

Also retains the ESP8266 4M1M flash/filesystem layout, web UI, rules engine and the standard OTA support paths inherited from the normal build. Actual availability and behavior must be confirmed by a successful compilation and on-device test.

## IMPORTANT: status

This is the **first experimental configuration**. It has **not yet been compiled, flashed, or measured**. The objective is improved free heap and largest available heap block — *not merely a smaller firmware binary*.

The preceding stock firmware on CW reports (2026-11-01): free RAM 4512 bytes; max free block 2368 bytes; fragmentation 39%; free stack 3504 bytes; 47 compiled plugins.

## Test and rollback procedure

1. First ensure PlatformIO compilation succeeds and the output fits the 4M1M OTA partition.
2. Make a complete CW configuration and rules backup; record the existing firmware file `ESP_Easy_mega_20260720_normal_ESP8266_4M1M.bin` for rollback.
3. Test on CW **only** with access to local recovery/flashing if necessary.
4. Confirm six sensor plugins and C002; check the existing device tasks and MQTT controller.
5. Confirm inlet/DHT/dewpoint/status, dutycycle and tachometer rpm; check GPIO13 PWM, GPIO15 relay and GPIO0 tach signal, including HEAT/COOL and fallback operation.
6. Compare RAM, largest free block, fragmentation, stack, uptime and WiFi/MQTT behavior with the original build over comparable operating conditions.
7. If anything fails, flash the original stock firmware and restore configuration as required.

Do **not** assume missing libraries/features will be safe until the build and the pilot have been validated.

The canonical V2 rules/HA monitoring documentation lives in `blb4github/PET10-infrastructuur`, under `warmtepomp/espeasy-convector-v2/`.
