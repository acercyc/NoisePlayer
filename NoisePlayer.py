import glob
import sys
from threading import Timer
import numpy as np
from PyQt5.QtWidgets import QMainWindow, QApplication
from pygame import mixer
import GUI

# ============================================================================ #
#                             Sound file processing                            #
# ============================================================================ #
fMp3 = []
fWave = glob.glob('./*.wav')
files = fMp3 + fWave


# ============================================================================ #
#                                      GUI                                     #
# ============================================================================ #
class MyWindow(QMainWindow, GUI.Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        # sound
        mixer.init()
        self.soundObj = None

        # timer
        # self.timer = sched.scheduler()
        self.volumeChangeTime = 5
        self.timer = Timer(self.volumeChangeTime, self.changeVolume)

        # ------------------------------------ GUI ----------------------------------- #
        self.setupUi(self)
        self.listWidget.addItems(files)

        # callback function
        self.Play.clicked.connect(self.cb_Play)
        self.Stop.clicked.connect(self.cb_Stop)
        self.randomVolume.clicked.connect(self.cb_randomVolume)
        self.show()
        self.activateWindow()

    def cb_Play(self):
        mixer.stop()
        selected = self.listWidget.currentItem().text()
        print(selected)
        self.soundObj = mixer.Sound(selected)
        self.soundObj.play(loops=100)

    def cb_Stop(self):
        mixer.stop()
        self.timer.cancel()

    def cb_randomVolume(self):
        self.changeVolume()
        # self.timer.enter(3, 1, self.changeVolume)
        # self.timer.run(False)
        # self.timer = Timer(5, self.changeVolume)
        # self.timer.start()

    def changeVolume(self):
        v = np.random.rand()
        self.soundObj.set_volume(v)
        self.timer = Timer(self.volumeChangeTime, self.changeVolume).start()
        # self.timer.enter(3, 1, self.changeVolume)
        # self.timer.run(False)
        # self.timer.start()
        print(v)


app = QApplication(sys.argv)
w = MyWindow()
app.exec_()
