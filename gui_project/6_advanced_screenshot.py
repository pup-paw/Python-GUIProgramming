import time
import keyboard
from PIL import ImageGrab


def screenshot():
    # 2021년 8월 31일 10시 50분 50초 -> _20210831_105050
    curr_time = time.strftime("_%y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))  # image_20210831_105050.png


keyboard.add_hotkey("F9", screenshot)  # 사용자가 F9키를 누르면 스크린샷 저장

keyboard.wait("esc")  # 사용자가 esc를 누를때까지 프로그램 수행
