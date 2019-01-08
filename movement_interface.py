"""
#
# S0mHmxxGh0ulz
# 
# Author: l33tH@x0rxxGh0u1
#
"""

### Movement Interface

def player_input():
    global p_input
    p_input = input(": ")

def movement_prompt():
    options_1 = ["Forward", "Back", "Touch", "Items"]
    options_2 = ["Left", "Right"]
    hallFlag = False
    if hallFlag == True:
        for i  in range(0, len(options_2)):
             print(str(i +1)+ ")", options_2[i])
    else:
        for i  in range(0, len(options_1)):
             print(str(i + 1)+ ")", options_1[i])

def movement_selection(b_input):
    global selection
    selection = b_input
    if selection == 1:
        move
    elif selection == 2:
        days_selection()
    elif selection == 3:
        days_selection()
    elif selection == 4:
        opt_4()
    else:
        bad_input()
        duration_select()



