#Created by Shamanthi => To learn how to multithread in python.
#Program simply runs through 1 - 100 continously and repeatedly, if user enters space, program asks if they want to continue looping or not.

import threading
import time
import keyboard

# Event to signal when to pause the number looping
pause_event = threading.Event()

# Variable to track if the looping should continue
continue_looping = True

# Function for the thread that loops through numbers
def loop_numbers():
    global continue_looping
    i = 1
    while continue_looping:
        print(i)
        time.sleep(1)  # Pause for 1 second between each number
        i += 1
        if i > 100:
            i = 1
        while pause_event.is_set():
            time.sleep(0.1)  # Sleep to avoid busy waiting

# Function to capture spacebar events and handle pausing and continuation
def on_space(event):
    global pause_event
    global continue_looping
    if event.name == 'space':
        pause_event.set()  # Pause the loop
        response = input("Looping paused. Do you want to continue (y/n)? ").lower()
        
        while response not in ['y', 'n']:
            response = input("Invalid input. Please enter 'y' or 'n': ").lower()
        if response == 'y':
            pause_event.clear()  # Resume the loop
        else:
            continue_looping = False  # End the program
            pause_event.clear()  # Ensure the loop is paused before exiting

# Register the spacebar event listener
keyboard.on_press(on_space)

# Create the thread for looping through numbers
thread1 = threading.Thread(target=loop_numbers)

# Start the thread
thread1.start()

# Wait for the thread to finish
thread1.join()

# Unregister the event listener
keyboard.unhook_all()

print("All tasks completed")
