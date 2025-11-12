#   Copyright 2024 PicoUSB
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""Pico USB boot.py file with GPIO 3 bridge mode selection.

USAGE:
- Normal BadUSB operation: Leave GPIO 3 unconnected (floating)
- Boot/Safe mode: Bridge GPIO 3 to any GND pin with a jumper wire

When GPIO 3 is bridged to GND:
- USB mass storage is enabled (you can access files)
- System enters SAFE MODE (code.py is not executed)
- You can modify payload files safely

When GPIO 3 is not connected:
- USB mass storage is disabled (stealth mode)
- code.py executes normally (BadUSB payload runs)
"""
import time
import board
import storage
import digitalio
import microcontroller

# Mode selection via GPIO 3 bridge to GND
# Bridge GPIO 3 to GND to enter boot/safe mode
# Leave GPIO 3 unconnected for normal BadUSB operation
mode = digitalio.DigitalInOut(board.GP3)
mode.direction = digitalio.Direction.INPUT
mode.pull = digitalio.Pull.UP

storage.remount("/", readonly=False)
m = storage.getmount("/")
m.label = "PicoUSB"
storage.remount("/", readonly=True)
storage.enable_usb_drive()

time.sleep(0.1) #wait a bit so the button gets pulled up

if mode.value:
    storage.disable_usb_drive()
else:
    time.sleep(0.1) #check again after 100ms to see if the button is still pressed
    if mode.value:
        storage.disable_usb_drive()
    else:
        storage.enable_usb_drive()
        microcontroller.on_next_reset(microcontroller.RunMode.SAFE_MODE)
        microcontroller.reset()
    

# in case you screw up and disable usb drive without the ability to enable it, to enter safe mode write in shell:
# import microcontroller
# microcontroller.on_next_reset(microcontroller.RunMode.SAFE_MODE)
# microcontroller.reset()
