import cv2
import pyautogui
import numpy
import time
import pydirectinput

# read target image
template = cv2.imread('resource/target.png', cv2.IMREAD_UNCHANGED)
hh, ww = template.shape[:2]
base = template[:,:,0:3]
alpha = template[:,:,3]
alpha = cv2.merge([alpha,alpha,alpha])

t = time.time()

while True:
    screenShot = image = cv2.cvtColor(numpy.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR)
    correlation = cv2.matchTemplate(screenShot, base, cv2.TM_CCORR_NORMED, mask=alpha)

    # set threshold and get all matches
    threshhold = 0.95
    location = numpy.where(correlation >= threshhold)
    print(location)

    # stop when find the target
    if len(location[0]):
        # send s and esc
        pydirectinput.press(['s', 'esc'], interval=0.2)
        break

    print(time.time() - t)

    # charge the engine
    if time.time() - t > 10:
        # send charge hotkey and f
        t = time.time()
        pydirectinput.press(['5', 'f'], interval=0.2)

    time.sleep(4)
