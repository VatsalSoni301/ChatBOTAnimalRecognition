import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os
import threading

class TimerMessageBox(QMessageBox):
    def __init__(self, timeout=3, parent=None):
        super(TimerMessageBox, self).__init__(parent)
        self.setWindowTitle("wait")
        self.time_to_wait = timeout
        self.setText("Wait for {0} seconds to get output".format(timeout))
        self.setStandardButtons(QMessageBox.NoButton)
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.changeContent)
        self.timer.start()

    def changeContent(self):
        self.setText("Wait for {0} seconds to get output".format(self.time_to_wait))
        self.time_to_wait -= 1
        if self.time_to_wait <= 0:
            self.close()

    def closeEvent(self, event):
        self.timer.stop()
        event.accept()

class Animal(QWidget):

    def __init__(self, parent=None):
        super(Animal, self).__init__(parent)
        self.fileName1=''
        self.fileName = ''
        self.layout = QVBoxLayout()
        self.srcb = QPushButton("Open File")
        self.srcb.clicked.connect(self.getfile)
        self.ok=QPushButton("Ok")
        self.ok.clicked.connect(self.okk)
        self.cnc = QPushButton("Cancel")
        self.cnc.clicked.connect(self.cncl)
        self.src = QLabel("Select File")
        self.setMinimumSize(850, 50)
        self.destb = QPushButton("Save Path")
        self.destb.clicked.connect(self.getfile1)
        self.dest = QLabel("Destination Path")

        self.layout.addWidget(self.srcb)
        self.layout.addWidget(self.src)
        self.layout.addWidget(self.destb)
        self.layout.addWidget(self.dest)
        self.layout.addWidget(self.ok)
        self.layout.addWidget(self.cnc)

        self.setLayout(self.layout)
        self.setWindowTitle("File")

    def getfile(self):

        self.fileName = QFileDialog.getOpenFileName(self, 'OpenFile')
        self.src.setText(self.fileName)

    def getfile1(self):

        self.fileName1 = QFileDialog.getSaveFileName(self, "Save file", "", ".txt")
        #self.fileName1 = QFileDialog.getOpenFileName(self, 'OpenFile')
        self.dest.setText(self.fileName1)

    def okk(self):

        print(self.fileName)
        print(self.fileName1)
        ans='./darknet detect cfg/yolo.cfg yolo.weights'+' '+self.fileName+' '+'>'+self.fileName1
        
        #ans='python --version'
        t=threading.Thread(target=self.cmd,args=(str(ans),))
        t.start()
        messagebox = TimerMessageBox(40, self)
        messagebox.exec_()
        ans='emacs'+' '+self.fileName1
        os.system(str(ans))

    def cncl(self):
        self.close()

    def cmd(self,command):
        os.system(command)


def main():

    app = QApplication(sys.argv)
    ex = Animal()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
