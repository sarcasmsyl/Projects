from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, \
    QStyle, QSlider, QFileDialog
from PyQt5.QtGui import QIcon, QPalette, QColor
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon('SarcasmMP.ico'))
        self.setWindowTitle('SMPlayer')
        self.setGeometry(400, 200, 900, 700)

        p = self.palette()
        p.setColor(QPalette.Window, QColor(0, 0, 0))
        self.setPalette(p)

        self.create_player()



    def create_player(self):

        self.mediaPlayer =  QMediaPlayer(None, QMediaPlayer.VideoSurface)

        videowidget = QVideoWidget()


        self.openButton = QPushButton('Open File')
        self.openButton.clicked.connect(self.open_file)

        self.playButton = QPushButton('Play')
        self.playButton.setEnabled(False)
        self.playButton.clicked.connect(self.play_video)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 0)
        self.slider.sliderMoved.connect(self.set_position)




        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)

        hbox.addWidget(self.openButton)
        hbox.addWidget(self.playButton)
        hbox.addWidget(self.slider)


        vbox = QVBoxLayout()
        vbox.addWidget(videowidget)

        vbox.addLayout(hbox)

        self.mediaPlayer.setVideoOutput(videowidget)
        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)


        self.setLayout(vbox)


    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")

        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playButton.setEnabled(True)

    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediastate_changed(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))

        else:
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def position_changed(self, position):
        self.slider.setValue(position)

    def duration_changed(self, duration):
        self.slider.setRange(0, duration)

    def set_position(self, position):
        self.mediaPlayer.setPosition(position)






app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
