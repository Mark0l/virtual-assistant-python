# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# ---------------.....MAIN.....---------------
def main():
    with open('aux_files/time.txt', 'r') as reader:
        date_mmdd = reader.read()
    today = strftime("%m%d%H")
    if (date_mmdd[0:4] != today[0:4] and int(today[4:6]) >= 6) or (
            date_mmdd[0:4] == today[0:4] and int(date_mmdd[4:6]) < 6 <= int(today[4:6])):
        init.reset_checklist()
        init.reset_cycle()
        print("\nresetted: cycle & morning routine\n")
        print(f"\nadded daily: {add_repeating_tasks()}")
        write_time()
    draw_checklist()
    while True:
        if butt_NFC.is_pressed:
            check_routine_via_NFC()
            draw_checklist()
        if butt_task.is_pressed:
            new_task()
        if butt_shopping.is_pressed:
            new_task("shop")
        if butt.is_pressed:
            with open('aux_files/cycle_state.txt', 'r') as reader:
                cycle_state = reader.read()
                print(f"----------\nhello world \n\n cycle number is {cycle_state}\n----------")
                cycle_state = int(cycle_state)

            try:
                with canvas(device_pomodoro) as draw:
                    draw.rectangle(device_pomodoro.bounding_box, outline="white", fill="black")
                    draw.text((30, 40), "Hello World", fill="white", font=font_norm)
            except:
                print("\n! npomo-display error ! \t\tpomo disp init\n")

            while True:
                write_time()
                pomo_red_blink(cycle_state)
                with open('aux_files/cycle_state.txt', 'r') as reader:
                    cycle_state = int(reader.read())
                    print(f"----------\n following pomo is {cycle_state + 1}\n----------")
                cycle_state = pomo_red_light(cycle_state)
                pomo_green_blink(cycle_state)
                pomo_green_light(cycle_state)
        if butt_up.is_pressed:
            print_tasks(20)
        if butt_down.is_pressed:
            print_tasks(20, "project")
        sleep(0.5)


# ---------------.....INIT.....---------------
# used when started by "start_yn.py" sequence with button press OR "python3 -m main" command
from init import *

# print_tasks(15)
print("\nFinished starting.\n\tEnjoy your day :)\n")
main()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
