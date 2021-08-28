import pyautogui, random, time
bober = './res/bober.png'
test = './res/test.png'
found = False
CORR = 10

class Bobber:
    img = './res/bobber.png'
    founded = False
    targeted = False


    def find(self):
        self.position = pyautogui.locateOnScreen(self.img, confidence=0.7)
        if self.position:
            self.founded = True
        else:
            self.position = False

    def target(self):
        corr = 10
        pos = pyautogui.center(self.position)
        x = random.uniform(pos.x - corr, pos.x + corr)
        y = random.uniform(pos.y - corr, pos.y + corr)
        t = random.uniform(0.1, 0.2)
        pyautogui.moveTo(x, y, t)
        self.targeted = True

    def wait(self):
        return pyautogui.locateOnScreen(self.img, confidence=0.7)

    def catch(self):
        pyautogui.keyDown('shift')
        pyautogui.click(button='left')
        pyautogui.keyUp('shift')
        time.sleep(random.uniform(1, 2))
        pyautogui.press('=')
        time.sleep(random.uniform(1, 2))
        self.founded = False
        self.targeted = False

bobber = Bobber()
while True:
    print("Szukam spławika")
    bobber.find()
    if bobber.founded:
        print("Spławik znaleziony")
        bobber.target()
        if bobber.targeted:
            print("Spławik namierzony")
            while bobber.wait():
                print("Czekam na branie")
            print("łapię!")
            bobber.catch()

