import pyautogui
from time import sleep


def keep_alive_windows_login():
    current_mouse_x, current_mouse_y = pyautogui.position()
    press_button = True
    while True:
        try:
            new_mouse_x, new_mouse_y = pyautogui.position()
            if new_mouse_x == current_mouse_x and new_mouse_y == current_mouse_y:
                if press_button:
                    pyautogui.press('volumedown')
                    press_button = False
                else:
                    pyautogui.press('volumeup')
                    press_button = True
        except:
            continue
        current_mouse_x, current_mouse_y = new_mouse_x, new_mouse_y
        sleep(300)

if __name__ == '__main__':
    keep_alive_windows_login()