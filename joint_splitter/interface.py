import sys

from PySide2 import QtCore
from PySide2.QtCore import Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QWidget, QPushButton, QSlider, QHBoxLayout, QVBoxLayout, QLabel
from pymel.core import ls

sys.path.append("C:\\Users\\tahmi\\PycharmProjects\\R-Tools\\joint_splitter")
from joint_splitter import JointSplitter


class BSlider(QWidget):
    def __init__(self, onValueChanged, minRange=0, maxRange=10, value=5):
        super(BSlider, self).__init__()
        # initializing values
        self.onValueChanged = onValueChanged
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
        if JointSplitterInterface.connected:
            self.value = value
            self.valueLabel.setText(str(value))
            self.onValueChanged()


class JointSplitterInterface(QWidget):
    connected = False

    def __init__(self):
        super(JointSplitterInterface, self).__init__()
        self.first_joint = None
        self.second_joint = None
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Joint Splitter')
        main_layout = QVBoxLayout()
        self.joint_split_count_slider = BSlider(self.split_joints)
        main_layout.addWidget(self.joint_split_count_slider)
        main_layout.addStretch(1)

        hbox = QHBoxLayout()
        connect_button = QPushButton("Connect", self)
        disconnect_button = QPushButton("Disconnect", self)

        disconnect_button.clicked.connect(self.close)
        connect_button.clicked.connect(self.connect)
        # connect_button.clicked.connect(lambda *args: JointSplitter.split_joints(joint_split_count_slider.value))

        hbox.addWidget(connect_button)
        hbox.addWidget(disconnect_button)

        main_layout.addLayout(hbox)

        self.setLayout(main_layout)
        self.show()

    def split_joints(self):
        JointSplitter.split_joints(self.first_joint, self.second_joint, self.joint_split_count_slider.value)

    def disconnect(self, *args, **kwargs):
        JointSplitterInterface.connected = False
        self.close()

    def connect(self, *args, **kwargs):
        selection = ls(selection=True)
        if JointSplitter.validate_for_split_joint(selection):
            self.first_joint = ls(selection=True)[0]
            self.second_joint = ls(selection=True)[1]
            JointSplitterInterface.connected = True


gui = JointSplitterInterface()
