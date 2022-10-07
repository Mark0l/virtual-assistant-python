from gpiozero import Button
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106
from time import sleep

butt_shopping = Button(13)
butt_task = Button(6)

serial_routine = i2c(port=1, address=0x3C)
device_routine = sh1106(serial_routine, height=64, width=128)
device_routine.rotate = 2

with canvas(device_routine) as draw:
    draw.text((15, 25), f"Press SHOP to START.", fill="white")
#print(f"start wizard running")

while 1:
    if butt_shopping.is_pressed:
        butt_shopping.close()
        butt_task.close()
        with canvas(device_routine) as draw:
            draw.text((5, 25), f"starting HOME-ASS.", fill="white")
        print(f"\n--- STARTING HOME-ASSISTANT ---")
        import main
        break
        print("--------- broke from 'start_yn' loop ----------")

    if butt_task.is_pressed:
        with canvas(device_routine) as draw:
            draw.text((5, 25), f"ending script", fill="white")
        print(f"\n--- ending script ---")
        break
    sleep(0.5)
