# virtual-assistant-python
## Introduction
Extracted parts of my pet project of virtual assistant, written in Python. Projects consists of main HW unit Raspberry Pi, peripheral components, SW is mainly in Pythnon with some Bash usage. Project runs as a continuous interactible script. Assistant is optimized for 1" always-on OLED display, but supports also 7" display (for debugging and more detailed informations).

## Functionalities
1. tasks list (auto sorting between project and life related, priority sorting, date sorting, auto suggesting),  
2. pomodoro timer (visual and push notifications), 
3. meal planning ("recipe book", shopping list creation), 
4. data upload to cloud service, 
5. NFC reader for easily expandable interactibility, 
6. shopping list (available on web, adding items on web or through keyboard), 
7. daily checklist of tasks.

## Project structure
1. When device is turned on, there is a constant loop waiting for user imput. Two scenarios can happen:
   - user wants to start virtual-assistant
   - user wants to access Raspberry Pi
2. When assistant is started, all functions are available except for meal planning and pomodoro timer.
   - Always-on display shows top priority tasks, which are sorted by priority and due date.
   - Functions are triggered by button press. Each functionality has a button assigned.
   - Meal planning is accessed from command line as a standalone script.
   - Pomodoro timer is additional function that can be run on top of normal function, but is off by default for power saving and is triggered by designated button.
