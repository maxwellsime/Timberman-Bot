import cv2 as cv
import numpy as np
import win32gui
import win32ui
import win32con
import pyautogui


class TimberBot:
    def __init__(self):
        self.s = 'x'

    def window_grab():
        w = 1920
        h = 1080

        hwnd = win32gui.FindWindow(
            None, 'example screenshot (1).jpg - IrfanView')
        wDC = win32gui.GetWindowDC(hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        bmp = win32ui.CreateBitmap()
        bmp.CreateCompatibleBitmap(dcObj, w, h)
        cDC.SelectObject(bmp)
        cDC.BitBlt((0, 0), (w, h), dcObj, (0, 0), win32con.SRCCOPY)

        # Change screenshot format
        signedIntsArray = bmp.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (h, w, 4)

        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(hwnd, wDC)
        win32gui.DeleteObject(bmp.GetHandle())

        return img

    def run():
        # Looping screengrabs
        while(True):
            screenshot = TimberBot.window_grab()
            cv.imshow('Computer Vision', screenshot)

            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                break

        print('Done.')


TimberBot.run()
