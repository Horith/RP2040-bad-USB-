# BadUSB Mode Selection Guide

## Hardware Setup

Your RP2040 board has been configured to use **GPIO 3** for mode selection via a simple bridge connection.

## How to Use

### Normal BadUSB Operation (Payload Execution)
1. **Disconnect any jumper wire** from GPIO 3
2. Connect the device to target computer
3. The BadUSB payload in `pico_usb.txt` will execute automatically
4. USB mass storage is disabled (stealth mode)

### Boot/Safe Mode (File Editing)
1. **Bridge GPIO 3 to any GND pin** using a jumper wire
2. Connect the device to your computer
3. The device appears as a USB drive named "PicoUSB"
4. You can safely edit:
   - `pico_usb.txt` (your payload)
   - `layout.txt` (keyboard layout)
   - Any other files
5. Remove the jumper wire before deploying

## GPIO Pin Locations

On most RP2040 mini USB boards:
- **GPIO 3** is usually labeled as "GP3" or "3"
- **GND** pins are usually labeled as "GND" or "-"
- Use any available GND pin (there are typically multiple)

## Troubleshooting

- If the device doesn't enter boot mode: Check that GPIO 3 is properly connected to GND
- If payload doesn't execute: Make sure GPIO 3 is completely disconnected (not touching GND)
- If you get stuck: Use the manual safe mode commands shown in `boot.py` comments

## Advantages of This Method

1. **Simple**: Just one jumper wire needed
2. **Reliable**: No timing issues with button combinations  
3. **Safe**: Clear distinction between operational and configuration modes
4. **Flexible**: Easy to switch modes during development