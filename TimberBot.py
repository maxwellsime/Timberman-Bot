import cv2 as cv
import numpy as np
import pyautogui
from PIL import ImageGrab
from time import sleep


class timberBot:
    '''
    Dynamic window sizing + Branch locating based on percentages
    Currently: Requires window to be top-left of your main monitor,
            16:9 resolution
        ImageGrab based on windowrect, 
            make sure the bottom of the bbox is where to search from
    '''
    w = 0
    h = 0

    # Calculates screengrab size
    def __init__(self, w, h):
        self.w = np.ceil(w * 0.44)
        self.h = np.ceil(h * 0.64)

    # Simple Imagegrab of left-side branch
    def grabber(self):
        img = ImageGrab.grab(bbox=(0, 0, self.w, self.h))
        return img

    # Loops searching for black pixels in the img
    # Finding a black pixel means a branch is found
    def branchSearch(self, img):
        # Search first 20 pixels, from bottom up
        n = self.h

        while n > self.h - 30:
            # -1 used to stop index out of bounds
            px = img.getpixel((self.w - 1, n - 1))
            if px == (0, 0, 0):
                # Branch is found in img
                return True
            else:
                n -= 2
        else:
            # Branch not found in img
            return False

    # Applies BranchSearch and responds with outputs
    def run(self):
        sleep(5)
        print('Get Ready!')

        for x in range(10):
            branch = self.branchSearch(self.grabber())

            if branch:
                pyautogui.press('right')
                print('Left Branch')
            else:
                pyautogui.press('left')
                print('Right Branch')
            x += 1
            sleep(0.5)
        print('Done.')

    def test(self):
        img = self.grabber()
        img = cv.cvtColor(np.array(img), cv.COLOR_RGB2BGR)
        cv.imshow('Computer Vision', img)

        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()


tim = timberBot(1600, 900)
tim.run()
