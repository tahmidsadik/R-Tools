import maya.cmds as cmds
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QWidget, QCheckBox, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton

small_font = QFont("SansSerif", 12)
medium_text_font = QFont("SansSerif", 12)


class CheckBoxWithLineEdit(QWidget, ):
    def __init__(self, checkBoxLabel="Prefix", lineEditText="JNT", contentMargin=[0, 0, 0, 0]):
        super(CheckBoxWithLineEdit, self).__init__()
        self.checkBox = QCheckBox(checkBoxLabel)
        self.lineEdit = QLineEdit(lineEditText, self)

        # setting up fonts
        self.checkBox.setFont(small_font)
        self.lineEdit.setFont(small_font)

        self.lineEdit.setTextMargins(5, 5, 5, 5)
        self.lineEdit.setContentsMargins(contentMargin[0], contentMargin[1], \
                                         contentMargin[2], contentMargin[3])
        # margin = self.lineEdit.getContentsMargins()
        # margin = QLabel(str(margin), self)

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.checkBox)
        self.hbox.addWidget(self.lineEdit)
        # self.hbox.addWidget(margin)

        self.setLayout(self.hbox)
        self.setFixedHeight(60)


class Renamer(QWidget):
    def __init__(self):
        super(Renamer, self).__init__()
        self.baseName = ""
        self.separatorString = "_"
        self.prefix = ""
        self.suffix = ""
        self.isUsingPrefix = False
        self.isUsingPrefix = False
        self.renameList = []
        self.prefixGui = None
        self.suffixGui = None
        self.baseNameGui = None

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 450)
        self.setWindowTitle("Rename some stuff")

        contentMargin = [38, 0, 0, 0]
        self.baseNameGui = CheckBoxWithLineEdit("Base Name:", "Spine")
        self.prefixGui = CheckBoxWithLineEdit("Prefix:", "JNT", contentMargin=contentMargin)
        self.suffixGui = CheckBoxWithLineEdit("Suffix:", "GEO", contentMargin=contentMargin)
        button = QPushButton("Rename", self)
        button.setFont(medium_text_font)
        button.setFixedHeight(50)

        # button action
        button.clicked.connect(self.renameStuff)

        # layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.baseNameGui)
        mainLayout.addWidget(self.prefixGui)
        mainLayout.addWidget(self.suffixGui)
        mainLayout.addStretch(1)
        mainLayout.addWidget(button)

        self.setLayout(mainLayout)
        self.show()

    def renameStuff(self):
        selectedNodes = cmds.ls(selection=True)
        prefix = self.prefixGui.lineEdit.text()
        suffix = self.suffixGui.lineEdit.text()
        baseName = self.baseNameGui.lineEdit.text()
        name_without_idx = prefix + self.separatorString + baseName

        for idx, value in enumerate(selectedNodes):
            name = name_without_idx + str(idx) + self.separatorString + suffix
            cmds.rename(value, name)


x = Renamer()
