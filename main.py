from PIL import ImageGrab
import pyautogui
import time


def iscollide(data):
    for i in range(830, 850):
        for j in range(320, 370):
            if data[i, j] < 171:
                hit("down")
                print('down')
                return
    for i in range(700,760):
        for j in range(350,370):
            if data[i,j] < 100:
                hit('space')
                print('jump')
                return



def hit(key):
    pyautogui.keyDown(key)
    return


if __name__=='__main__':

    time.sleep(5)
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        iscollide(data)


