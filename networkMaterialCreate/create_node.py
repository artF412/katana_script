def create_katana_nodes(self, path_col, path_nrm, path_rgh, path_met, path_bmp, path_ao, path_emi):
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
            # create node col_color_correct
            col_color_correct = NodegraphAPI.CreateNode('ArnoldShadingNode', network_material_create)
            col_color_correct.getParameter('name').setValue('col_color_correct',0)
            col_color_correct.getParameter('nodeType').setValue('color_correct',0)
            col_color_correct.checkDynamicParameters()

            # Link node color_correct [out] -> [base_color] node standard_surface
            col_color_correct_out = col_color_correct.getOutputPort('out')
            standard_surface_in_base_color = standard_surface.getInputPort('base_color')
            col_color_correct_out.connect(standard_surface_in_base_color)
            
            # create node image_baseColor
            image_col = NodegraphAPI.CreateNode('ArnoldShadingNode', network_material_create)
            image_col.getParameter('name').setValue('col',0)
            image_col.getParameter('nodeType').setValue('image', 0)
            image_col.checkDynamicParameters()

            # Link node col [out] -> [input] node color_correct
            image_col_out = image_col.getOutputPort('out')
            col_color_correct_input = col_color_correct.getInputPort('input')
            image_col_out.connect(col_color_correct_input)

            # Get parameter image_col filename
            image_col.getParameter('parameters.filename.value').setValue(path_col, 0)
            image_col.getParameter('parameters.filename.enable').setValue(1, 0)
            
            # set position
            NodegraphAPI.SetNodePosition(col_color_correct,(standard_surface_position[0]-400,standard_surface_position[1]))
            NodegraphAPI.SetNodePosition(image_col,(standard_surface_position[0]-800,standard_surface_position[1]))
        
        if path_rgh:
            # Create node rgh_ramp_float
            rgh_ramp_float = NodegraphAPI.CreateNode('ArnoldShadingNode', network_material_create)
            rgh_ramp_float.getParameter('name').setValue('rgh_ramp_float',0)
            rgh_ramp_float.getParameter('nodeType').setValue('ramp_float',0)
            rgh_ramp_float.checkDynamicParameters()

            # Link node rgh_ramp_float [out] -> [specular_roughness] node standard_surface
            rgh_ramp_float_out = rgh_ramp_float.getOutputPort('out')
            standard_surface_in_specular_roughness = standard_surface.getInputPort('specular_roughness')
            rgh_ramp_float_out.connect(standard_surface_in_specular_roughness)
            
            # create node image_roughtness
            image_rgh = NodegraphAPI.CreateNode('ArnoldShadingNode', network_material_create)
            image_rgh.getParameter('name').setValue('rgh',0)
            image_rgh.getParameter('nodeType').setValue('image', 0)
            image_rgh.checkDynamicParameters()

            # Link node rgh [out] -> [input] node rgh_ramp_float
            image_rgh_out = image_rgh.getOutputPort('out')
            rgh_ramp_float_input = rgh_ramp_float.getInputPort('input')
            image_rgh_out.connect(rgh_ramp_float_input)

            # Get parameters image_rgh filename
            image_rgh.getParameter('parameters.filename.value').setValue(path_rgh, 0)
            image_rgh.getParameter('parameters.filename.enable').setValue(1, 0)
            
            # set position
            NodegraphAPI.SetNodePosition(rgh_ramp_float,(standard_surface_position[0]-400,standard_surface_position[1]-400))
            NodegraphAPI.SetNodePosition(image_rgh,(standard_surface_position[0]-800,standard_surface_position[1]-400))

        if path_met:  
            # create node met_ramp_float
            met_ramp_float = NodegraphAPI.CreateNode('ArnoldShadingNode',network_material_create)
            met_ramp_float.getParameter('name').setValue('met_ramp_float',0)
            met_ramp_float.getParameter('nodeType').setValue('ramp_float',0)
            met_ramp_float.checkDynamicParameters()

            # Link node met_ramp_float [out] -> [metalness] node standard_surface
            met_ramp_float_out = met_ramp_float.getOutputPort('out')
            standard_surface_in_metalness = standard_surface.getInputPort('metalness')
            met_ramp_float_out.connect(standard_surface_in_metalness)
            
            # create node image_matelness
            image_met = NodegraphAPI.CreateNode('ArnoldShadingNode', network_material_create)
            image_met.getParameter('name').setValue('met',0)
            image_met.getParameter('nodeType').setValue('image',0)
            image_met.checkDynamicParameters()

            # Link node mat [out] -> [metalness] node met_ramp_float
            image_met_out = image_met.getOutputPort('out')
            met_ramp_float_input = met_ramp_float.getInputPort('input')
            image_met_out.connect(met_ramp_float_input)

            # Get parameters image_met filename
            image_met.getParameter('parameters.filename.value').setValue(path_met, 0)
            image_met.getParameter('parameters.filename.enable').setValue(1, 0)
            
            # set position
            NodegraphAPI.SetNodePosition(met_ramp_float,(standard_surface_position[0]-400,standard_surface_position[1]-800))
            NodegraphAPI.SetNodePosition(image_met,(standard_surface_position[0]-800,standard_surface_position[1]-800))
            
        if path_nrm:
            # create node normal_map
            normal_map = NodegraphAPI.CreateNode('ArnoldShadingNode',network_material_create)
            normal_map.getParameter('name').setValue('normal_map',0)
            normal_map.getParameter('nodeType').setValue('normal_map',0)
            normal_map.checkDynamicParameters()

            # Link node normal_map [out] -> [normal] node standard_surface
            normal_map_out = normal_map.getOutputPort('out')
            standard_surface_in_normal = standard_surface.getInputPort('normal')
            normal_map_out.connect(standard_surface_in_normal)
            
            # create node image_nrm
            image_nrm = NodegraphAPI.CreateNode('ArnoldShadingNode', network_material_create)
            image_nrm.getParameter('name').setValue('nrm',0)
            image_nrm.getParameter('nodeType').setValue('image',0)
            image_nrm.checkDynamicParameters()

            # Link node nrm [out] -> [normal] node normal_map
            image_nrm_out = image_nrm.getOutputPort('out')
            normal_map_input = normal_map.getInputPort('input')
            image_nrm_out.connect(normal_map_input)

            # Get parameters image_nrm filename
            image_nrm.getParameter('parameters.filename.value').setValue(path_nrm, 0)
            image_nrm.getParameter('parameters.filename.enable').setValue(1, 0)
            
            # set position
            NodegraphAPI.SetNodePosition(normal_map,(standard_surface_position[0]-400,standard_surface_position[1]-1200))
            NodegraphAPI.SetNodePosition(image_nrm,(standard_surface_position[0]-800,standard_surface_position[1]-1200))
            
        if path_bmp:
            # create node bump2d
            bump_2d = NodegraphAPI.CreateNode('ArnoldShadingNode',network_material_create)
            bump_2d.getParameter('name').setValue('bump2d',0)
            bump_2d.getParameter('nodeType').setValue('bump2d',0)
            bump_2d.checkDynamicParameters()

            # create node image_bmp
            image_bmp = NodegraphAPI.CreateNode('ArnoldShadingNode', network_material_create)
            image_bmp.getParameter('name').setValue('bmp',0)
            image_bmp.getParameter('nodeType').setValue('image',0)
            image_bmp.checkDynamicParameters()
            
            # Link node bmp [out] -> [bump_map] node bump2d
            image_bmp_out = image_bmp.getOutputPort('out')
            bump_2d_input = bump_2d.getInputPort('bump_map')
            image_bmp_out.connect(bump_2d_input)
            
            # Get parameters image_nrm filename
            image_bmp.getParameter('parameters.filename.value').setValue(path_bmp, 0)
            image_bmp.getParameter('parameters.filename.enable').setValue(1, 0)
            
            # set position
            NodegraphAPI.SetNodePosition(bump_2d,(standard_surface_position[0]-400,standard_surface_position[1]-2000))
            NodegraphAPI.SetNodePosition(image_bmp,(standard_surface_position[0]-800,standard_surface_position[1]-2000))
            
        
        if path_emi:
            # create node emi_color_correct
            emi_color_correct = NodegraphAPI.CreateNode('ArnoldShadingNode', network_material_create)
            emi_color_correct.getParameter('name').setValue('emi_color_correct',0)
            emi_color_correct.getParameter('nodeType').setValue('color_correct',0)
            emi_color_correct.checkDynamicParameters()

            # Link node color_correct [out] -> [base_color] node standard_surface
            emi_color_correct_out = emi_color_correct.getOutputPort('out')
            standard_surface_in_emission = standard_surface.getInputPort('emission_color')
            emi_color_correct_out.connect(standard_surface_in_emission)

            # create node image_emi
            image_emi = NodegraphAPI.CreateNode('ArnoldShadingNode', network_material_create)
            image_emi.getParameter('name').setValue('emi',0)
            image_emi.getParameter('nodeType').setValue('image',0)
            image_emi.checkDynamicParameters()
            
            # Link node emi [out] -> [input] node emi_color_correct
            image_emi_out = image_emi.getOutputPort('out')
            emi_color_correct_input = emi_color_correct.getInputPort('input')
            image_emi_out.connect(emi_color_correct_input)
            
            # Get parameters image_nrm filename
            image_emi.getParameter('parameters.filename.value').setValue(path_emi, 0)
            image_emi.getParameter('parameters.filename.enable').setValue(1, 0)
            
            # set position
            NodegraphAPI.SetNodePosition(emi_color_correct,(standard_surface_position[0]-400,standard_surface_position[1]-2400))
            NodegraphAPI.SetNodePosition(image_emi,(standard_surface_position[0]-800,standard_surface_position[1]-2400))
            
        if path_ao:
            # create node image_ao
            image_ao = NodegraphAPI.CreateNode('ArnoldShadingNode', network_material_create)
            image_ao.getParameter('name').setValue('ao',0)
            image_ao.getParameter('nodeType').setValue('image',0)
            image_ao.checkDynamicParameters()
            
            # Get parameters image_nrm filename
            image_ao.getParameter('parameters.filename.value').setValue(path_ao, 0)
            image_ao.getParameter('parameters.filename.enable').setValue(1, 0)
            
            #set position
            NodegraphAPI.SetNodePosition(image_ao,(standard_surface_position[0]-800,standard_surface_position[1]-1600))