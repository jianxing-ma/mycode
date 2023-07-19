import keyboard


# Listen for a single key press
def read_key():
    key = keyboard.read_key()
    return key


# Listen for key events continuously
def listen_keys():
    keyboard.on_press(on_press_callback)
    keyboard.wait()


# Callback function for key press event
def on_press_callback(event):
    print(f"Key pressed: {event.name}")


# Example usage
key = read_key()
print(f"Key pressed: {key}")

# listen_keys()

