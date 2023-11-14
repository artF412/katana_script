from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtGui import QIcon
import os
from os.path import expanduser, splitext
home = expanduser("~")

class MainUI(object):
    def setupUi(self, Form):
        self.Form = Form
        Form.setObjectName("Form")
        Form.resize(615, 500)
        self.select_multiple_image = QtWidgets.QPushButton(Form)
        self.select_multiple_image.setGeometry(QtCore.QRect(230, 30, 250, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_multiple_image.sizePolicy().hasHeightForWidth())
        self.select_multiple_image.setSizePolicy(sizePolicy)
        self.select_multiple_image.setMinimumSize(QtCore.QSize(0, 0))
        self.select_multiple_image.setIconSize(QtCore.QSize(16, 16))
        self.select_multiple_image.setObjectName("select_multiple_image")
        self.col_label = QtWidgets.QLabel(Form)
        self.col_label.setGeometry(QtCore.QRect(60, 90, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setBold(True)
        font.setWeight(75)
        self.col_label.setFont(font)
        self.col_label.setObjectName("col_label")
        self.nrm_label = QtWidgets.QLabel(Form)
        self.nrm_label.setGeometry(QtCore.QRect(60, 130, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setBold(True)
        font.setWeight(75)
        self.nrm_label.setFont(font)
        self.nrm_label.setObjectName("nrm_label")
        self.rgh_label = QtWidgets.QLabel(Form)
        self.rgh_label.setGeometry(QtCore.QRect(50, 170, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setBold(True)
        font.setWeight(75)
        self.rgh_label.setFont(font)
        self.rgh_label.setObjectName("rgh_label")
        self.met_label = QtWidgets.QLabel(Form)
        self.met_label.setGeometry(QtCore.QRect(50, 210, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setBold(True)
        font.setWeight(75)
        self.met_label.setFont(font)
        self.met_label.setObjectName("met_label")
        self.ao_label = QtWidgets.QLabel(Form)
        self.ao_label.setGeometry(QtCore.QRect(20, 250, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setBold(True)
        font.setWeight(75)
        self.ao_label.setFont(font)
        self.ao_label.setObjectName("ao_label")
        self.emi_label = QtWidgets.QLabel(Form)
        self.emi_label.setGeometry(QtCore.QRect(50, 330, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setBold(True)
        font.setWeight(75)
        self.emi_label.setFont(font)
        self.emi_label.setObjectName("emi_label")
        self.bmp_label = QtWidgets.QLabel(Form)
        self.bmp_label.setGeometry(QtCore.QRect(60, 290, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setBold(True)
        font.setWeight(75)
        self.bmp_label.setFont(font)
        self.bmp_label.setObjectName("bmp_label")
        
        self.iso_label = QtWidgets.QLabel(Form)
        self.iso_label.setGeometry(QtCore.QRect(60, 370, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setBold(True)
        font.setWeight(75)
        self.iso_label.setFont(font)
        self.iso_label.setObjectName("iso_label")
        
        self.iso_lineEdit = QtWidgets.QLineEdit(Form)
        self.iso_lineEdit.setGeometry(QtCore.QRect(180, 370, 351, 31))
        self.iso_lineEdit.setObjectName("iso_lineEdit")
        
        self.ao_lineEdit = QtWidgets.QLineEdit(Form)
        self.ao_lineEdit.setGeometry(QtCore.QRect(180, 250, 351, 31))
        self.ao_lineEdit.setObjectName("ao_lineEdit")
        self.col_lineEdit = QtWidgets.QLineEdit(Form)
        self.col_lineEdit.setGeometry(QtCore.QRect(180, 90, 351, 31))
        self.col_lineEdit.setObjectName("col_lineEdit")
        self.nrm_lineEdit = QtWidgets.QLineEdit(Form)
        self.nrm_lineEdit.setGeometry(QtCore.QRect(180, 130, 351, 31))
        self.nrm_lineEdit.setObjectName("nrm_lineEdit")
        self.rgh_lineEdit = QtWidgets.QLineEdit(Form)
        self.rgh_lineEdit.setGeometry(QtCore.QRect(180, 170, 351, 31))
        self.rgh_lineEdit.setObjectName("rgh_lineEdit")
        self.met_lineEdit = QtWidgets.QLineEdit(Form)
        self.met_lineEdit.setGeometry(QtCore.QRect(180, 210, 351, 31))
        self.met_lineEdit.setObjectName("met_lineEdit")
        self.bmp_lineEdit = QtWidgets.QLineEdit(Form)
        self.bmp_lineEdit.setGeometry(QtCore.QRect(180, 290, 351, 31))
        self.bmp_lineEdit.setObjectName("bmp_lineEdit")
        self.emi_lineEdit = QtWidgets.QLineEdit(Form)
        self.emi_lineEdit.setGeometry(QtCore.QRect(180, 330, 351, 31))
        self.emi_lineEdit.setObjectName("emi_lineEdit")

        self.iso_toolButton = QtWidgets.QToolButton(Form)
        self.iso_toolButton.setGeometry(QtCore.QRect(550, 370, 31, 31))
        self.iso_toolButton.setObjectName("iso_toolButton")
        
        self.col_toolButton = QtWidgets.QToolButton(Form)
        self.col_toolButton.setGeometry(QtCore.QRect(550, 90, 31, 31))
        self.col_toolButton.setObjectName("col_toolButton")
        self.nrm_toolButton = QtWidgets.QToolButton(Form)
        self.nrm_toolButton.setGeometry(QtCore.QRect(550, 130, 31, 31))
        self.nrm_toolButton.setObjectName("nrm_toolButton")
        self.rgh_toolButton = QtWidgets.QToolButton(Form)
        self.rgh_toolButton.setGeometry(QtCore.QRect(550, 170, 31, 31))
        self.rgh_toolButton.setObjectName("rgh_toolButton")
        self.met_toolButton = QtWidgets.QToolButton(Form)
        self.met_toolButton.setGeometry(QtCore.QRect(550, 210, 31, 31))
        self.met_toolButton.setObjectName("met_toolButton")
        self.ao_toolButton = QtWidgets.QToolButton(Form)
        self.ao_toolButton.setGeometry(QtCore.QRect(550, 250, 31, 31))
        self.ao_toolButton.setObjectName("ao_toolButton")
        self.bmp_toolButton = QtWidgets.QToolButton(Form)
        self.bmp_toolButton.setGeometry(QtCore.QRect(550, 290, 31, 31))
        self.bmp_toolButton.setObjectName("bmp_toolButton")
        self.emi_toolButton = QtWidgets.QToolButton(Form)
        self.emi_toolButton.setGeometry(QtCore.QRect(550, 330, 31, 31))
        self.emi_toolButton.setObjectName("emi_toolButton")
        self.apply_button = QtWidgets.QPushButton(Form)
        self.apply_button.setGeometry(QtCore.QRect(390, 420, 88, 31))
        self.apply_button.setObjectName("apply_button")
        self.cancel_button = QtWidgets.QPushButton(Form)
        self.cancel_button.setGeometry(QtCore.QRect(490, 420, 88, 31))
        self.cancel_button.setObjectName("cancel_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.select_multiple_image.clicked.connect(self.open_fileDialog_select_multiple_image)
        self.col_toolButton.clicked.connect(self.open_fileDialog_select_col)
        self.nrm_toolButton.clicked.connect(self.open_fileDialog_select_nrm)
        self.rgh_toolButton.clicked.connect(self.open_fileDialog_select_rgh)
        self.met_toolButton.clicked.connect(self.open_fileDialog_select_met)
        self.ao_toolButton.clicked.connect(self.open_fileDialog_select_ao)
        self.bmp_toolButton.clicked.connect(self.open_fileDialog_select_bmp)
        self.emi_toolButton.clicked.connect(self.open_fileDialog_select_emi)

        self.cancel_button.clicked.connect(self.cancel_button_close)
        self.apply_button.clicked.connect(self.apply_button_link)
        
        icon_path = '/opt/path/icon'
        icon_button = QIcon(icon_path)
        self.col_toolButton.setIcon(icon_button)
        self.nrm_toolButton.setIcon(icon_button)
        self.rgh_toolButton.setIcon(icon_button)
        self.met_toolButton.setIcon(icon_button)
        self.ao_toolButton.setIcon(icon_button)
        self.emi_toolButton.setIcon(icon_button)
        self.bmp_toolButton.setIcon(icon_button)
        self.iso_toolButton.setIcon(icon_button)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Katana Workflow to Image Maps"))
        self.select_multiple_image.setText(_translate("Form", "Select Multiple Image"))
        self.col_label.setText(_translate("Form", "Color"))
        self.nrm_label.setText(_translate("Form", "Normal"))
        self.rgh_label.setText(_translate("Form", "Roughness"))
        self.met_label.setText(_translate("Form", "Metalness"))
        self.ao_label.setText(_translate("Form", "Ambient Occlusion"))
        self.emi_label.setText(_translate("Form", "Emission"))
        self.bmp_label.setText(_translate("Form", "Height"))
        
        self.iso_label.setText(_translate("Form", "ISO"))
        self.iso_toolButton.setText(_translate("Form", "..."))
        
        self.col_toolButton.setText(_translate("Form", "..."))
        self.nrm_toolButton.setText(_translate("Form", "..."))
        self.rgh_toolButton.setText(_translate("Form", "..."))
        self.met_toolButton.setText(_translate("Form", "..."))
        self.ao_toolButton.setText(_translate("Form", "..."))
        self.bmp_toolButton.setText(_translate("Form", "..."))
        self.emi_toolButton.setText(_translate("Form", "..."))
        self.apply_button.setText(_translate("Form", "Apply"))
        self.cancel_button.setText(_translate("Form", "Cancel"))


    def open_fileDialog_select_multiple_image(self):
        options = QFileDialog.Options()
        file_dialog = QFileDialog()
        file_dialog.setWindowTitle("Katana Workflow to Image Maps")
        file_dialog.setDirectory(home)
        file_dialog.setNameFilter("Image files (*.jpg *.png *.exr *.tif *.tga *.tx)")
        file_paths, _ = file_dialog.getOpenFileNames(None, "Open Images", "", "Image files (*.jpg *.png *.exr *.tif *.tga *.tx)", options=options)

        if file_paths:
            for path in file_paths:
                file_name = path.split("/")[-1]  # Extract the file name from the path
                base_name, extension = os.path.splitext(file_name)
                # Check file name patterns and set the appropriate line edits
                if base_name.endswith(".col"):
                    self.col_lineEdit.setText(path)
                elif base_name.endswith(".nrm"):
                    self.nrm_lineEdit.setText(path)
                elif base_name.endswith(".rgh"):
                    self.rgh_lineEdit.setText(path)
                elif base_name.endswith(".met"):
                    self.met_lineEdit.setText(path)
                elif base_name.endswith(".ao"):
                    self.ao_lineEdit.setText(path)
                elif base_name.endswith(".bmp"):
                    self.bmp_lineEdit.setText(path)
                elif base_name.endswith(".emi"):
                    self.emi_lineEdit.setText(path)
            self.col_lineEdit.setReadOnly(True)
            self.nrm_lineEdit.setReadOnly(True)
            self.rgh_lineEdit.setReadOnly(True)
            self.met_lineEdit.setReadOnly(True)
            self.ao_lineEdit.setReadOnly(True)
            self.bmp_lineEdit.setReadOnly(True)
            self.emi_lineEdit.setReadOnly(True)
            

    def open_fileDialog_select_col(self):
        col_options = QFileDialog.Options()
        col_dialog = QFileDialog()
        col_dialog.setWindowTitle("Base Color")
        col_dialog.setDirectory(home)
        col_dialog.setNameFilter("Image files (*.jpg *.png *.exr *.tif *.tga *.tx)")
        col_selected_file, _ = col_dialog.getOpenFileName(None, "Open Image", "", "Image files (*.jpg *.png *.exr *.tif *.tga *.tx)", options=col_options)

        if col_selected_file:
            self.col_lineEdit.setReadOnly(True)
            self.col_lineEdit.setText(col_selected_file)


    def open_fileDialog_select_nrm(self):
        nrm_options = QFileDialog.Options()
        nrm_dialog = QFileDialog()
        nrm_dialog.setWindowTitle("Normal")
        nrm_dialog.setDirectory(home)
        nrm_dialog.setNameFilter("Image files (*.jpg *.png *.exr *.tif *.tga *.tx)")
        nrm_selected_file, _ = nrm_dialog.getOpenFileName(None, "Open Images", "", "Image files (*.jpg *.png *.exr *.tif *.tga *.tx)", options=nrm_options)

        if nrm_selected_file:
            self.nrm_lineEdit.setReadOnly(True)
            self.nrm_lineEdit.setText(nrm_selected_file)

    def open_fileDialog_select_rgh(self):
        rgh_options = QFileDialog.Options()
        rgh_dialog = QFileDialog()
        rgh_dialog.setWindowTitle("Roughness")
        rgh_dialog.setDirectory(home)
        rgh_dialog.setNameFilter("Image files (*.jpg *.png *.exr *.tif *.tga *.tx)")
        rgh_selected_file, _ = rgh_dialog.getOpenFileName(None, "Open Image", "", "Image files (*.jpg *.png *.exr *.tif *.tga *.tx)", options=rgh_options)

        if rgh_selected_file:
            self.rgh_lineEdit.setReadOnly(True)
            self.rgh_lineEdit.setText(rgh_selected_file)

    def open_fileDialog_select_met(self):
        met_options = QFileDialog.Options()
        met_dialog = QFileDialog()
        met_dialog.setWindowTitle("Metalness")
        met_dialog.setDirectory(home)
        met_dialog.setNameFilter("Image files (*.jpg *.png *.exr *.tif *.tga *.tx)")
        met_selected_file, _ = met_dialog.getOpenFileName(None, "Open Images", "", "Image files (*.jpg *.png *.exr *.tif *.tga *.tx)", options=met_options)

        if met_selected_file:
            self.met_lineEdit.setReadOnly(True)
            self.met_lineEdit.setText(met_selected_file)

    def open_fileDialog_select_ao(self):
        ao_options = QFileDialog.Options()
        ao_dialog = QFileDialog()
        ao_dialog.setWindowTitle("Ambient occlusion")
        ao_dialog.setDirectory(home)
        ao_dialog.setNameFilter("Image files (*.jpg *.png *.exr *.tif *.tga *.tx)")
        ao_selected_file, _ = ao_dialog.getOpenFileName(None, "Open Images", "", "Image files (*.jpg *.png *.exr *.tif *.tga *.tx)", options=ao_options)

        if ao_selected_file:
            self.ao_lineEdit.setReadOnly(True)
            self.ao_lineEdit.setText(ao_selected_file)

    def open_fileDialog_select_bmp(self):
        bmp_options = QFileDialog.Options()
        bmp_dialog = QFileDialog()
        bmp_dialog.setWindowTitle("Height")
        bmp_dialog.setDirectory(home)
        bmp_dialog.setNameFilter("Image files (*.jpg *.png *.exr *.tif *.tga *.tx)")
        bmp_selected_file, _ = bmp_dialog.getOpenFileName(None, "Open Images", "", "Image files (*.jpg *.png *.exr *.tif *.tga *.tx)", options=bmp_options)

        if bmp_selected_file:
            self.bmp_lineEdit.setReadOnly(True)
            self.bmp_lineEdit.setText(bmp_selected_file)


    def open_fileDialog_select_emi(self):
        emi_options = QFileDialog.Options()
        emi_dialog = QFileDialog()
        emi_dialog.setWindowTitle("Emission")
        emi_dialog.setDirectory(home)
        emi_dialog.setNameFilter("Image files (*.jpg *.png *.exr *.tif *.tga *.tx)")
        emi_selected_file, _ = emi_dialog.getOpenFileName(None, "Open Images", "", "Image files (*.jpg *.png *.exr *.tif *.tga *.tx)", options=emi_options)

        if emi_selected_file:
            self.emi_lineEdit.setReadOnly(True)
            self.emi_lineEdit.setText(emi_selected_file)

    def apply_button_link(self):
        path_col = self.col_lineEdit.text()
        path_nrm = self.nrm_lineEdit.text()
        path_rgh = self.rgh_lineEdit.text()
        path_met = self.met_lineEdit.text()
        path_bmp = self.bmp_lineEdit.text()
        path_ao = self.ao_lineEdit.text()
        path_emi = self.emi_lineEdit.text()
        self.create_katana_nodes(path_col, path_nrm, path_rgh, path_met, path_bmp, path_ao, path_emi)
        self.Form.close()

    def cancel_button_close(self):
        self.Form.close()
        
app = QtWidgets.QApplication.instance()
Form = QtWidgets.QWidget()
ui = MainUI()
ui.setupUi(Form)
Form.show()