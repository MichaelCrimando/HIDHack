import board
import digitalio
import time
import usb_hid
from hid_gamepad import Gamepad

gp = Gamepad(usb_hid.devices)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Equivalent of Arduino's map() function.
def range_map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

while True:
    gp.press_buttons(1)
    print(" press", 1, end="")
    gp.move_joysticks(
    x=range_map(500, 0, 65535, -127, 127),
    y=range_map(500, 0, 65535, -127, 127),
    )
    print(" x", 500, "y", 500)
    led.value = True
    time.sleep(1)



    gp.release_buttons(1)
    gp.move_joysticks(
    x=range_map(10000, 0, 65535, -127, 127),
    y=range_map(10000, 0, 65535, -127, 127),
    )
    print(" x", 10000, "y", 10000)
    print(" release", 1, end="")
    led.value = False
    time.sleep(1)
