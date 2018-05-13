import sys

from PySide2.QtGui import QFont

sys.path.append("C:\\Users\\tahmi\\PycharmProjects\\R-Tools\\plugin")

from PySide2 import QtCore
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QPushButton, QSlider, QHBoxLayout, QVBoxLayout, QLabel
from plugin import JointSplitter


class BSlider(QWidget):
    def __init__(self, minRange=0, maxRange=10, value=5):
        super(BSlider, self).__init__()
        # initializing values
        self.minRange = minRange
        self.maxRange = maxRange
        self.value = value

        font_for_value_label = QFont("SansSerif", 13)

        self.minLabel = QLabel(str(minRange), self)
        self.maxLabel = QLabel(str(maxRange), self)
        self.valueLabel = QLabel(str(value), self)
        self.valueLabel.setFont(font_for_value_label)
        self.minLabel.setFont(font_for_value_label)
        self.maxLabel.setFont(font_for_value_label)

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setRange(self.minRange, self.maxRange)
        self.slider.setValue(self.value)

        # setting up signals and slots aka events
        self.slider.valueChanged[int].connect(self.onSliderValueChanged)

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.minLabel)
        self.hbox.addWidget(self.slider)
        self.hbox.addWidget(self.maxLabel)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(self.valueLabel)

        self.valueLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.setLayout(self.vbox)
        self.setFixedHeight(80)

    def onSliderValueChanged(self, value):
        self.value = value
        self.valueLabel.setText(str(value))


class BasicGUI(QWidget):
    def __init__(self):
        super(BasicGUI, self).__init__()
        self.split_count = 5
        self.min_split_count = 2
        self.max_split_count = 10
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Joint Splitter')

        main_layout = QVBoxLayout()
        joint_split_count_slider = BSlider()
        main_layout.addWidget(joint_split_count_slider)
        main_layout.addStretch(1)

        hbox = QHBoxLayout()
        ok_button = QPushButton("Apply", self)
        cancel_button = QPushButton("Cancel", self)

        cancel_button.clicked.connect(self.close)
        print(joint_split_count_slider.value)
        ok_button.clicked.connect(lambda *args: JointSplitter.split_joints(joint_split_count_slider.value))

        hbox.addWidget(ok_button)
        hbox.addWidget(cancel_button)

        main_layout.addLayout(hbox)

        self.setLayout(main_layout)
        self.show()
        # setting up label for the button
        # QToolTip.setFont(QFont('SansSerif', 12))
        # self.setToolTip('This is a <b>QWidget</b> widget')

        # setting up layout
        # horizontalBox = QHBoxLayout()

        #
        # button = QPushButton('Quit', self)
        # button.setToolTip('This is a <b>QPushButton</b> widget')
        # button.resize(100, 50)
        # button.move(100, 85)
        #
        # button.clicked.connect(self.close)
        #
        # self.split_count_label = QLabel("Split Count: " + str(self.split_count), self)
        #
        # slider = QSlider(Qt.Horizontal, self)
        # slider.setRange(self.min_split_count, self.max_split_count)
        # slider.setValue(self.split_count)
        # slider.setFocusPolicy(Qt.NoFocus)
        #
        # # horizontalBox.addWidget(self.split_count_label)
        # horizontalBox.addWidget(slider)
        #
        #
        # vbox = QVBoxLayout()
        # vbox.addLayout(horizontalBox)
        # vbox.addWidget(self.split_count_label)
        # vbox.addWidget(button)
        #
        # self.setLayout(vbox)


gui = BasicGUI()
