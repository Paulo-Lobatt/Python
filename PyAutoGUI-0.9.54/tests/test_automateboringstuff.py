"""
Unit tests to ensure that we don't change PyAutoGUI in such a way
that makes the text in "Automate the Boring Stuff with Python" wrong.
"""

import unittest, time, threading, os, sys
import pyautogui


class TestGeneral(unittest.TestCase):
    def test_p415e1(self):
        """From page 415 of the 1st edition:
        >>> import pyautogui
        >>> pyautogui.PAUSE = 1
        >>> pyautogui.FAILSAFE = True
        """
        oldValue = pyautogui.PAUSE  # PAUSE should exist.
        pyautogui.PAUSE = 1  # This should not fail.
        pyautogui.PAUSE = oldValue

        oldValue = pyautogui.FAILSAFE  # FAILSAFE should exist.
        pyautogui.FAILSAFE = False  # This should not fail.
        pyautogui.FAILSAFE = oldValue



    def test_p416e1(self):
        """From page 416 of 1st edition:
        >>> import pyautogui
        >>> pyautogui.size()
        (1920, 1080)
        >>> width, height = pyautogui.size()

        >>> import pyautogui
        >>> for i in range(10):
            pyautogui.moveTo(100, 100, duration=0.25)
            pyautogui.moveTo(200, 100, duration=0.25)
            pyautogui.moveTo(200, 200, duration=0.25)
            pyautogui.moveTo(100, 200, duration=0.25)

        >>> import pyautogui
        >>> for i in range(10):
            pyautogui.moveRel(100, 0, duration=0.25)
            pyautogui.moveRel(0, 100, duration=0.25)
            pyautogui.moveRel(-100, 0, duration=0.25)
            pyautogui.moveRel(0, -100, duration=0.25)
        """
        wh = pyautogui.size()
        self.assertTrue(type(wh[0]) == int)
        self.assertTrue(type(wh[1]) == int)

        self.assertTrue(type(wh.width) == int)
        self.assertTrue(type(wh.height) == int)

        startTime = time.time()
        pyautogui.moveTo(100, 100, duration=0.25)
        self.assertTrue(pyautogui.position() == (100, 100))
        self.assertTrue(time.time() > startTime + 0.25)

        startTime = time.time()
        pyautogui.moveRel(100, 0, duration=0.25)
        self.assertTrue(pyautogui.position() == (200, 100))
        self.assertTrue(time.time() > startTime + 0.25)

        pyautogui.moveRel(0, 100, duration=0.25)
        self.assertTrue(pyautogui.position() == (200, 200))

        pyautogui.moveRel(-100, 0, duration=0.25)
        self.assertTrue(pyautogui.position() == (100, 200))

        pyautogui.moveRel(0, -100, duration=0.25)
        self.assertTrue(pyautogui.position() == (100, 100))

    def test_p417e1(self):
        """From page 417, first edition:
        >>> pyautogui.position()
        (311, 622)
        >>> pyautogui.position()
        (377, 481)
        >>> pyautogui.position()
        (1536, 637)
        """
        xy = pyautogui.position()  # This should not cause an error
        self.assertTrue(type(xy[0]) == int)
        self.assertTrue(type(xy[1]) == int)

    def test_p421e1(self):
        threading.Thread(target=os.system, args=('mspaint',)).start()
        time.sleep(2)
        win = pyautogui.getWindowsWithTitle('Untitled - Paint')[0]
        win.activate() # Bring to foreground
        win.maximize()
        time.sleep(2)
        pyautogui.moveTo(100, 300)

        distance = 30  # Make this 30 instead of 200 just so the test goes quicker.
        while distance > 0:
            pyautogui.dragRel(distance, 0, duration=0.2) # move right
            distance = distance - 5
            pyautogui.dragRel(0, distance, duration=0.2) # move down
            pyautogui.dragRel(-distance, 0, duration=0.2) # move left
            distance = distance - 5
            pyautogui.dragRel(0, -distance, duration=0.2) # move up

        win.close()
        #time.sleep(0.3)  # Wait for dialog to appear
        pyautogui.press('n')  # Tell mspaint to not save.

    def test_p422e1(self):
        """
        >>> pyautogui.scroll(200)
        """

        pyautogui.scroll(200)  # Just make sure this doesn't fail.


    def test_p423e1(self):
        """
        >>> import pyautogui
        >>> im = pyautogui.screenshot()

        >>> im.getpixel((0, 0))
        (176, 176, 175)
        >>> im.getpixel((50, 200))
        (130, 135, 144)
        """
        im = pyautogui.screenshot()
        rgb = im.getpixel((0, 0))
        self.assertTrue(type(rgb) == tuple)
        self.assertTrue(len(rgb) == 3)
        self.assertTrue(type(rgb[0]) == int)
        self.assertTrue(type(rgb[1]) == int)
        self.assertTrue(type(rgb[2]) == int)

        rgb = im.getpixel((50, 200))
        self.assertTrue(type(rgb) == tuple)
        self.assertTrue(len(rgb) == 3)
        self.assertTrue(type(rgb[0]) == int)
        self.assertTrue(type(rgb[1]) == int)
        self.assertTrue(type(rgb[2]) == int)

        """
        From page 424, 1st ed:
        >>> import pyautogui
        >>> im = pyautogui.screenshot()
        >>> im.getpixel((50, 200))
        (130, 135, 144)
        >>> pyautogui.pixelMatchesColor(50, 200, (130, 135, 144))
        True
        >>> pyautogui.pixelMatchesColor(50, 200, (255, 135, 144))
        False
        """

        pyautogui.pixelMatchesColor(50, 200, (130, 135, 144))
        pyautogui.pixelMatchesColor(50, 200, (255, 135, 144))


    def test_p425e1(self):
        """
        >>> import pyautogui
        >>> pyautogui.locateOnScreen('submit.png')
        (643, 745, 70, 29)

        >>> list(pyautogui.locateAllOnScreen('submit.png'))
        [(643, 745, 70, 29), (1007, 801, 70, 29)]
        """
        FOLDER_OF_THIS_FILE = os.path.dirname(os.path.abspath(__file__))
        testFile = os.path.join(FOLDER_OF_THIS_FILE, 'testimage.png')

        # Make sure these don't fail. They don't have to match anything on the screen.
        pyautogui.locateOnScreen(testFile)
        list(pyautogui.locateAllOnScreen(testFile))

    def test_p426e1(self):
        """
        >>> pyautogui.locateOnScreen('submit.png')
        (643, 745, 70, 29)
        >>> pyautogui.center((643, 745, 70, 29))
        (678, 759)
        >>> pyautogui.click((678, 759))

        >>> pyautogui.click(100, 100); pyautogui.typewrite('Hello world!')
        """

        xy = pyautogui.center((643, 745, 70, 29))
        self.assertTrue(xy == (678, 759))
        pyautogui.click((10, 10))

        threading.Thread(target=pyautogui.prompt).start()
        time.sleep(3)  # Wait for dialog box to open.
        pyautogui.typewrite('Hello world!\n')
        time.sleep(1)  # Wait for dialog box to close.




if __name__ == "__main__":
    #webbrowser.open('file://' + os.getcwd().replace('\\', '/') + '/blank.html')
    #time.sleep(4)
    if sys.platform != 'win32':
        print('This unit test is Windows only.')
        sys.exit()

    unittest.main()
