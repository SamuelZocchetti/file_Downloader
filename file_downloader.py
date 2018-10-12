from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(494, 275)
        self.lineEditPath = QtWidgets.QLineEdit(Dialog)
        self.lineEditPath.setGeometry(QtCore.QRect(26, 74, 441, 21))
        self.lineEditPath.setObjectName("lineEditPath")
        self.pushButtonPath = QtWidgets.QPushButton(Dialog)
        self.pushButtonPath.setGeometry(QtCore.QRect(20, 30, 133, 32))
        self.pushButtonPath.setObjectName("pushButtonPath")
        self.pushButtonPath.clicked.connect(self.pathButton_clicked)
        self.lineEditName = QtWidgets.QLineEdit(Dialog)
        self.lineEditName.setGeometry(QtCore.QRect(26, 129, 125, 21))
        self.lineEditName.setObjectName("lineEditName")
        self.labelName = QtWidgets.QLabel(Dialog)
        self.labelName.setGeometry(QtCore.QRect(26, 105, 84, 16))
        self.labelName.setObjectName("labelName")
        self.pushButtonDownload = QtWidgets.QPushButton(Dialog)
        self.pushButtonDownload.setGeometry(QtCore.QRect(20, 209, 128, 32))
        self.pushButtonDownload.setObjectName("pushButtonDownload")
        self.pushButtonDownload.clicked.connect(self.downloadButton)
        self.lineEditUrl = QtWidgets.QLineEdit(Dialog)
        self.lineEditUrl.setGeometry(QtCore.QRect(26, 184, 441, 21))
        self.lineEditUrl.setObjectName("lineEditUrl")
        self.labelUrl = QtWidgets.QLabel(Dialog)
        self.labelUrl.setGeometry(QtCore.QRect(26, 160, 57, 16))
        self.labelUrl.setObjectName("labelUrl")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def pathButton_clicked(self):
        #options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        #fileName, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        fileName = str(QFileDialog.getExistingDirectory(None, "Select Directory"))
        self.lineEditPath.setText(fileName)
        if fileName:
            print(fileName)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "File Downloader"))
        self.pushButtonPath.setText(_translate("Dialog", "Seleziona Path"))
        self.labelName.setText(_translate("Dialog", "Nome del File"))
        self.pushButtonDownload.setText(_translate("Dialog", "Download File"))
        self.labelUrl.setText(_translate("Dialog", "Copia Url"))

    def downloadButton(self):
        import urllib.request
        import ssl
        ssl._create_default_https_context = ssl._create_unverified_context
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        shost = self.lineEditUrl.text()
        phost = str(shost)
        name = phost.rsplit('/', 1)[-1]
        self.lineEditName.setText(name)
        spath = self.lineEditPath.text()
        ppath = str(spath)
        destinazione = ppath + "/" + name
        #print(destinazione)
        urllib.request.urlretrieve(phost, destinazione)

if __name__ == "__main__":
    import sys
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
