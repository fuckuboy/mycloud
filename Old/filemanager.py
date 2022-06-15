from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
import os
import design


class MyFileBrowser(design.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self, maya=False):
        super(MyFileBrowser, self).__init__()
        self.setupUi(self)
        self.maya = maya
        self.tv_localStorage.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tv_localStorage.customContextMenuRequested.connect(self.context_menu)
        self.populate()

    def populate(self):
        path = r"E:\storage"
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath((QtCore.QDir.rootPath()))
        self.tv_localStorage.setModel(self.model)
        self.tv_localStorage.setRootIndex(self.model.index(path))
        self.tv_localStorage.setSortingEnabled(True)

    def context_menu(self):
        menu = QtWidgets.QMenu()
        open = menu.addAction("Open in new maya")
        open.triggered.connect(self.open_file)

        if self.maya:
            open_file = menu.addAction("Open file")
            open_file.triggered.connect(lambda: self.maya_file_operations(open_file=True))

            import_to_maya = menu.addAction("Import to Maya")
            import_to_maya.triggered.connect(self.maya_file_operations)

            reference_to_maya = menu.addAction("Add reference to Maya")
            reference_to_maya.triggered.connect(lambda: self.maya_file_operations(reference=True))

        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())

    def open_file(self):
        index = self.tv_localStorage.currentIndex()
        file_path = self.model.filePath(index)
        os.startfile(file_path)

    def maya_file_operations(self, reference=False, open_file=False):
        """
        open ,  reference,  Import
        :return:
        """
        index = self.tv_localStorage.currentIndex()
        file_path = self.model.filePath(index)
        import maya.cmds as cmds
        if reference:
            cmds.file(file_path, reference=True, type='mayaAscii', groupReference=True)
        elif open_file:
            file_location = cmds.file(query=True, location=True)
            if file_location == 'unknown':
                cmds.file(file_path, open=True, force=True)
            else:
                modify_file = cmds.file(query=True, modified=True)
                if modify_file:
                    result = cmds.confirmDialog(title='Opening new maya file',
                                                message='This file is modified. do you want to save this file.?',
                                                button=['yes', 'no'],
                                                defaultButton='yes',
                                                cancelButton='no',
                                                dismissString='no')
                    if result == 'yes':
                        cmds.file(save=True, type='mayaAscii')
                        cmds.file(file_path, open=True, force=True)
                    else:
                        cmds.file(file_path, open=True, force=True)
                else:
                    cmds.file(file_path, open=True, force=True)
        else:
            cmds.file(file_path, i=True, groupReference=True)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    fb = MyFileBrowser()
    fb.show()
    app.exec_()
