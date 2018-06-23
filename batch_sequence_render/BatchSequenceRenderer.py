import maya.cmds as cmds
from PySide2.QtWidgets import QWidget, QFileDialog, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout


class TextBoxWithLabel(QWidget):
    def __init__(self, label, inputVal):
        super(TextBoxWithLabel, self).__init__()
        self.labelStr = label
        self.inputStr = inputVal
        self.label = QLabel(self)
        self.lineEdit = QLineEdit(self)

        self.label.setText(self.labelStr)
        self.lineEdit.setText(self.inputStr)

        hbox = QHBoxLayout()
        hbox.addWidget(self.label)
        hbox.addWidget(self.lineEdit)

        self.setLayout(hbox)
        self.setFixedHeight(60)

        self.setContentsMargins(0, 0, 0, 0)


class SequenceRendererInterface(QWidget):
    def __init__(self):
        super(SequenceRendererInterface, self).__init__()
        self.availableRenderers = self.getListofAvailableRenderers()
        self.imageExtentionOptions = {
            "OPENEXR": "exr",
            "PNG": "png",
            "TIFF": "tif",
            "JPEG": "jpg",
            "TARGA": "targa"
        }
        self.renderers = {
            "mayaSoftware": "sw",
            "mayaHardware2": "hw2",
            "mentalRay": "mr",
            "redshift": "redshift",
            "arnold": "arnold"
        }
        self.initUI()

    def getListofAvailableRenderers(self):
        return cmds.renderer(query=True, namesOfAvailableRenderers=True)

    def getProjectPath(self):
        cmds.workspace(q=True, rootDirectory=True)

    def scenePath(self):
        cmds.file(query=True, sceneName=True)

    def initUI(self):
        self.setGeometry(100, 100, 400, 450)
        self.setWindowTitle("Batch Sequence Renderer")
        outputFolderpath = QFileDialog.getExistingDirectory(self, "Open Directory", "",
                                                            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)

        # finalImageNameLabel = QLabel(self)
        # finalImageNameLabel.setText(outputFolderpath + "/" + imageNameLabel.text() + "###.exr")

        self.imageName = TextBoxWithLabel("Image Name:", "Image")
        self.outputPath = TextBoxWithLabel("Output Path:", outputFolderpath)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.imageName)
        mainLayout.addWidget(self.outputPath)
        self.setLayout(mainLayout)
        self.show()


gui = SequenceRendererInterface()
