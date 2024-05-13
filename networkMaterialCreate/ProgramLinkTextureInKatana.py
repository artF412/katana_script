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
        self.iso_label.setGeometry(QtCore.QRect(70, 370, 61, 31))
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
        self.iso_toolButton.clicked.connect(self.open_fileDialog_select_iso)
        self.cancel_button.clicked.connect(self.cancel_button_close)
        self.apply_button.clicked.connect(self.apply_button_link)
        
        icon_path = '/home/faiz/Desktop/Gakuseisean-Aire-Search.24.png'
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
        file_dialog.setOption(QFileDialog.ReadOnly, False)
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
                elif base_name.endswith(".iso"):
                    self.iso_lineEdit.setText(path)
            self.col_lineEdit.setReadOnly(True)
            self.nrm_lineEdit.setReadOnly(True)
            self.rgh_lineEdit.setReadOnly(True)
            self.met_lineEdit.setReadOnly(True)
            self.ao_lineEdit.setReadOnly(True)
            self.bmp_lineEdit.setReadOnly(True)
            self.emi_lineEdit.setReadOnly(True)
            self.iso_lineEdit.setReadOnly(True)
            

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
            
            
    def open_fileDialog_select_iso(self):
        iso_options = QFileDialog.Options()
        iso_dialog = QFileDialog()
        iso_dialog.setWindowTitle("ISO")
        iso_dialog.setDirectory(home)
        iso_dialog.setNameFilter("Image files (*.jpg *.png *.exr *.tif *.tga *.tx)")
        iso_selected_file, _ = iso_dialog.getOpenFileName(None, "Open Images", "", "Image files (*.jpg *.png *.exr *.tif *.tga *.tx)", options=iso_options)
        
        if iso_selected_file:
            self.iso_lineEdit.setReadOnly(True)
            self.iso_lineEdit.setText(iso_selected_file)
        


    def apply_button_link(self):
        path_col = self.col_lineEdit.text()
        path_nrm = self.nrm_lineEdit.text()
        path_rgh = self.rgh_lineEdit.text()
        path_met = self.met_lineEdit.text()
        path_bmp = self.bmp_lineEdit.text()
        path_ao = self.ao_lineEdit.text()
        path_emi = self.emi_lineEdit.text()
        path_iso = self.iso_lineEdit.text()
        self.create_katana_nodes(path_col, path_nrm, path_rgh, path_met, path_bmp, path_ao, path_emi, path_iso)
        self.Form.close()


    def cancel_button_close(self):
        self.Form.close()


    def create_katana_nodes(self, path_col, path_nrm, path_rgh, path_met, path_bmp, path_ao, path_emi, path_iso):
        root_node = NodegraphAPI.GetRootNode()

        network_material_create = NodegraphAPI.CreateNode('NetworkMaterialCreate', root_node)
        network_material = network_material_create.getNetworkMaterials()[0]

        # Create node standard_surface
        standard_surface = NodegraphAPI.CreateNode('ArnoldShadingNode', network_material_create)
        standard_surface.getParameter('name').setValue('standard_surface',0)
        standard_surface.getParameter('nodeType').setValue('standard_surface', 0)
        standard_surface.checkDynamicParameters()    ## Build parameter UI

        # Link node standard_surface [out] -> [arnoldSurface] node NetworkMaterialCreate
        standard_surface_out = standard_surface.getOutputPort('out')
        network_material_in = network_material.getInputPort('arnoldSurface')
        standard_surface_out.connect(network_material_in)

        standard_surface_position = NodegraphAPI.GetNodePosition(standard_surface)


        if path_col:
            asset_name_col = os.path.basename(path_col).split('.')[0]
            
            # create node col_color_correct
            col_color_correct = NodegraphAPI.CreateNode('ArnoldShadingNode', network_material_create)
            col_color_correct.getParameter('name').setValue('colorCorrect_col_{}'.format(asset_name_col),0)
            col_color_correct.getParameter('nodeType').setValue('color_correct',0)
            col_color_correct.checkDynamicParameters()

            # Link node color_correct [out] -> [base_color] node standard_surface
            col_color_correct_out = col_color_correct.getOutputPort('out')
            standard_surface_in_base_color = standard_surface.getInputPort('base_color')
            col_color_correct_out.connect(standard_surface_in_base_color)
            
            # create node image_baseColor
            image_col = NodegraphAPI.CreateNode('ArnoldShadingNode', network_material_create)
            image_col.getParameter('name').setValue('image_col_{}'.format(asset_name_col),0)
            image_col.getParameter('nodeType').setValue('image', 0)
            image_col.checkDynamicParameters()

            # Link node col [out] -> [input] node color_correct
            image_col_out = image_col.getOutputPort('out')
            col_color_correct_input = col_color_correct.getInputPort('input')
            image_col_out.connect(col_color_correct_input)

            # Get parameter image_col filename
            image_col.getParameter('parameters.filename.value').setValue(path_col, 0)
            image_col.getParameter('parameters.filename.enable').setValue(1, 0)
            
            # Get parameter image_col ignore_missing_textures
            image_col.getParameter('parameters.ignore_missing_textures.enable').setValue(1, 0)
            image_col.getParameter('parameters.ignore_missing_textures.value').setValue(1, 0)
            
            # set position
            NodegraphAPI.SetNodePosition(col_color_correct,(standard_surface_position[0]-400,standard_surface_position[1]))
            NodegraphAPI.SetNodePosition(image_col,(standard_surface_position[0]-800,standard_surface_position[1]))
        
        
        if path_rgh:
            asset_name_rgh = os.path.basename(path_rgh).split('.')[0]
            
            # Create node rgh_ramp_float
            rgh_ramp_float = NodegraphAPI.CreateNode('ArnoldShadingNode', network_material_create)
            rgh_ramp_float.getParameter('name').setValue('rampFloat_rgh_{}'.format(asset_name_rgh),0)
            rgh_ramp_float.getParameter('nodeType').setValue('ramp_float',0)
            rgh_ramp_float.checkDynamicParameters()

            # Link node rgh_ramp_float [out] -> [specular_roughness] node standard_surface
            rgh_ramp_float_out = rgh_ramp_float.getOutputPort('out')
            standard_surface_in_specular_roughness = standard_surface.getInputPort('specular_roughness')
            rgh_ramp_float_out.connect(standard_surface_in_specular_roughness)
            
            # create node image_roughtness
            image_rgh = NodegraphAPI.CreateNode('ArnoldShadingNode', network_material_create)
            image_rgh.getParameter('name').setValue('image_rgh_{}'.format(asset_name_rgh),0)
            image_rgh.getParameter('nodeType').setValue('image', 0)
            image_rgh.checkDynamicParameters()

            # Link node rgh [out] -> [input] node rgh_ramp_float
            image_rgh_out = image_rgh.getOutputPort('out')
            rgh_ramp_float_input = rgh_ramp_float.getInputPort('input')
            image_rgh_out.connect(rgh_ramp_float_input)

            # Get parameters image_rgh filename
            image_rgh.getParameter('parameters.filename.value').setValue(path_rgh, 0)
            image_rgh.getParameter('parameters.filename.enable').setValue(1, 0)

            # Get parameter image_rgh ignore_missing_textures
            image_rgh.getParameter('parameters.ignore_missing_textures.enable').setValue(1, 0)
            image_rgh.getParameter('parameters.ignore_missing_textures.value').setValue(1, 0)
            
            # set position
            NodegraphAPI.SetNodePosition(rgh_ramp_float,(standard_surface_position[0]-400,standard_surface_position[1]-400))
            NodegraphAPI.SetNodePosition(image_rgh,(standard_surface_position[0]-800,standard_surface_position[1]-400))


        if path_met:  
            asset_name_met = os.path.basename(path_met).split('.')[0]
            
            # create node met_ramp_float
            met_ramp_float = NodegraphAPI.CreateNode('ArnoldShadingNode',network_material_create)
            met_ramp_float.getParameter('name').setValue('rampFloat_met_{}'.format(asset_name_met),0)
            met_ramp_float.getParameter('nodeType').setValue('ramp_float',0)
            met_ramp_float.checkDynamicParameters()

            # Link node met_ramp_float [out] -> [metalness] node standard_surface
            met_ramp_float_out = met_ramp_float.getOutputPort('out')
            standard_surface_in_metalness = standard_surface.getInputPort('metalness')
            met_ramp_float_out.connect(standard_surface_in_metalness)
            
            # create node image_matelness
            image_met = NodegraphAPI.CreateNode('ArnoldShadingNode', network_material_create)
            image_met.getParameter('name').setValue('image_met_{}'.format(asset_name_met),0)
            image_met.getParameter('nodeType').setValue('image',0)
            image_met.checkDynamicParameters()

            # Link node mat [out] -> [metalness] node met_ramp_float
            image_met_out = image_met.getOutputPort('out')
            met_ramp_float_input = met_ramp_float.getInputPort('input')
            image_met_out.connect(met_ramp_float_input)

            # Get parameters image_met filename
            image_met.getParameter('parameters.filename.value').setValue(path_met, 0)
            image_met.getParameter('parameters.filename.enable').setValue(1, 0)

            # Get parameter image_met ignore_missing_textures
            image_met.getParameter('parameters.ignore_missing_textures.enable').setValue(1, 0)
            image_met.getParameter('parameters.ignore_missing_textures.value').setValue(1, 0)
            
            # set position
            NodegraphAPI.SetNodePosition(met_ramp_float,(standard_surface_position[0]-400,standard_surface_position[1]-800))
            NodegraphAPI.SetNodePosition(image_met,(standard_surface_position[0]-800,standard_surface_position[1]-800))
            
            
        if path_nrm:
            asset_name_nrm = os.path.basename(path_nrm).split('.')[0]
            
            # create node normal_map
            normal_map = NodegraphAPI.CreateNode('ArnoldShadingNode',network_material_create)
            normal_map.getParameter('name').setValue('normalMap_{}'.format(asset_name_nrm),0)
            normal_map.getParameter('nodeType').setValue('normal_map',0)
            normal_map.checkDynamicParameters()

            # Link node normal_map [out] -> [normal] node standard_surface
            normal_map_out = normal_map.getOutputPort('out')
            standard_surface_in_normal = standard_surface.getInputPort('normal')
            normal_map_out.connect(standard_surface_in_normal)
            
            # create node image_nrm
            image_nrm = NodegraphAPI.CreateNode('ArnoldShadingNode', network_material_create)
            image_nrm.getParameter('name').setValue('image_nrm_{}'.format(asset_name_nrm),0)
            image_nrm.getParameter('nodeType').setValue('image',0)
            image_nrm.checkDynamicParameters()

            # Link node nrm [out] -> [normal] node normal_map
            image_nrm_out = image_nrm.getOutputPort('out')
            normal_map_input = normal_map.getInputPort('input')
            image_nrm_out.connect(normal_map_input)

            # Get parameters image_nrm filename
            image_nrm.getParameter('parameters.filename.value').setValue(path_nrm, 0)
            image_nrm.getParameter('parameters.filename.enable').setValue(1, 0)

            # Get parameter image_nrm ignore_missing_textures
            image_nrm.getParameter('parameters.ignore_missing_textures.enable').setValue(1, 0)
            image_nrm.getParameter('parameters.ignore_missing_textures.value').setValue(1, 0)
            
            # set position
            NodegraphAPI.SetNodePosition(normal_map,(standard_surface_position[0]-400,standard_surface_position[1]-1200))
            NodegraphAPI.SetNodePosition(image_nrm,(standard_surface_position[0]-800,standard_surface_position[1]-1200))
            
            
        if path_bmp:
            asset_name_bmp = os.path.basename(path_bmp).split('.')[0]
            
            # create node bump2d
            bump_2d = NodegraphAPI.CreateNode('ArnoldShadingNode',network_material_create)
            bump_2d.getParameter('name').setValue('bump2d_{}'.format(asset_name_bmp),0)
            bump_2d.getParameter('nodeType').setValue('bump2d',0)
            bump_2d.checkDynamicParameters()

            # create node image_bmp
            image_bmp = NodegraphAPI.CreateNode('ArnoldShadingNode', network_material_create)
            image_bmp.getParameter('name').setValue('image_bmp_{}'.format(asset_name_bmp),0)
            image_bmp.getParameter('nodeType').setValue('image',0)
            image_bmp.checkDynamicParameters()
            
            # Link node bmp [out] -> [bump_map] node bump2d
            image_bmp_out = image_bmp.getOutputPort('out')
            bump_2d_input = bump_2d.getInputPort('bump_map')
            image_bmp_out.connect(bump_2d_input)
            
            # Get parameters image_nrm filename
            image_bmp.getParameter('parameters.filename.value').setValue(path_bmp, 0)
            image_bmp.getParameter('parameters.filename.enable').setValue(1, 0)

            # Get parameter image_bmp ignore_missing_textures
            image_bmp.getParameter('parameters.ignore_missing_textures.enable').setValue(1, 0)
            image_bmp.getParameter('parameters.ignore_missing_textures.value').setValue(1, 0)
            
            # set position
            NodegraphAPI.SetNodePosition(bump_2d,(standard_surface_position[0]-400,standard_surface_position[1]-2000))
            NodegraphAPI.SetNodePosition(image_bmp,(standard_surface_position[0]-800,standard_surface_position[1]-2000))
            
        
        if path_emi:
            asset_name_emi = os.path.basename(path_emi).split('.')[0]
            
            # create node emi_color_correct
            emi_color_correct = NodegraphAPI.CreateNode('ArnoldShadingNode', network_material_create)
            emi_color_correct.getParameter('name').setValue('colorCorrect_emi_{}'.format(asset_name_emi),0)
            emi_color_correct.getParameter('nodeType').setValue('color_correct',0)
            emi_color_correct.checkDynamicParameters()

            # Link node color_correct [out] -> [base_color] node standard_surface
            emi_color_correct_out = emi_color_correct.getOutputPort('out')
            standard_surface_in_emission = standard_surface.getInputPort('emission_color')
            emi_color_correct_out.connect(standard_surface_in_emission)

            # create node image_emi
            image_emi = NodegraphAPI.CreateNode('ArnoldShadingNode', network_material_create)
            image_emi.getParameter('name').setValue('image_emi_{}'.format(asset_name_emi),0)
            image_emi.getParameter('nodeType').setValue('image',0)
            image_emi.checkDynamicParameters()
            
            # Link node emi [out] -> [input] node emi_color_correct
            image_emi_out = image_emi.getOutputPort('out')
            emi_color_correct_input = emi_color_correct.getInputPort('input')
            image_emi_out.connect(emi_color_correct_input)
            
            # Get parameters image_nrm filename
            image_emi.getParameter('parameters.filename.value').setValue(path_emi, 0)
            image_emi.getParameter('parameters.filename.enable').setValue(1, 0)

            # Get parameter image_emi ignore_missing_textures
            image_emi.getParameter('parameters.ignore_missing_textures.enable').setValue(1, 0)
            image_emi.getParameter('parameters.ignore_missing_textures.value').setValue(1, 0)
            
            # set position
            NodegraphAPI.SetNodePosition(emi_color_correct,(standard_surface_position[0]-400,standard_surface_position[1]-2400))
            NodegraphAPI.SetNodePosition(image_emi,(standard_surface_position[0]-800,standard_surface_position[1]-2400))
            
            
        if path_ao:
            asset_name_ao = os.path.basename(path_ao).split('.')[0]
            
            # create node image_ao
            image_ao = NodegraphAPI.CreateNode('ArnoldShadingNode', network_material_create)
            image_ao.getParameter('name').setValue('image_ao_{}'.format(asset_name_ao),0)
            image_ao.getParameter('nodeType').setValue('image',0)
            image_ao.checkDynamicParameters()
            
            # Get parameters image_nrm filename
            image_ao.getParameter('parameters.filename.value').setValue(path_ao, 0)
            image_ao.getParameter('parameters.filename.enable').setValue(1, 0)

            # Get parameter image_ao ignore_missing_textures
            image_ao.getParameter('parameters.ignore_missing_textures.enable').setValue(1, 0)
            image_ao.getParameter('parameters.ignore_missing_textures.value').setValue(1, 0)
            
            #set position
            NodegraphAPI.SetNodePosition(image_ao,(standard_surface_position[0]-800,standard_surface_position[1]-1600))
            
            
        if path_iso:
            asset_name_iso = os.path.basename(path_iso).split('.')[0]
            
            # create node met_ramp_float
            iso_ramp_float = NodegraphAPI.CreateNode('ArnoldShadingNode',network_material_create)
            iso_ramp_float.getParameter('name').setValue('rampFloat_iso_{}'.format(asset_name_iso),0)
            iso_ramp_float.getParameter('nodeType').setValue('ramp_float',0)
            iso_ramp_float.checkDynamicParameters() 
            
            # create node image_iso
            image_iso = NodegraphAPI.CreateNode('ArnoldShadingNode', network_material_create)
            image_iso.getParameter('name').setValue('image_iso_{}'.format(asset_name_iso),0)
            image_iso.getParameter('nodeType').setValue('image',0)
            image_iso.checkDynamicParameters()
            
            # Link node iso [out] -> [input] node iso_ramp_float
            image_iso_out = image_iso.getOutputPort('out')
            iso_ramp_float_input = iso_ramp_float.getInputPort('input')
            image_iso_out.connect(iso_ramp_float_input)
            
            # Get parameters image_nrm filename
            image_iso.getParameter('parameters.filename.value').setValue(path_iso, 0)
            image_iso.getParameter('parameters.filename.enable').setValue(1, 0)

            # Get parameter image_iso ignore_missing_textures
            image_iso.getParameter('parameters.ignore_missing_textures.enable').setValue(1, 0)
            image_iso.getParameter('parameters.ignore_missing_textures.value').setValue(1, 0)
            
            #set position
            NodegraphAPI.SetNodePosition(iso_ramp_float,(standard_surface_position[0]-400,standard_surface_position[1]-2800))
            NodegraphAPI.SetNodePosition(image_iso,(standard_surface_position[0]-800,standard_surface_position[1]-2800))


app = QtWidgets.QApplication.instance()
Form = QtWidgets.QWidget()
ui = MainUI()
ui.setupUi(Form)
Form.show()