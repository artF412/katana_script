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


# create node color_correct
color_correct = NodegraphAPI.CreateNode('ArnoldShadingNode', network_material_create)
color_correct.getParameter('name').setValue('color_correct',0)
color_correct.getParameter('nodeType').setValue('color_correct',0)
color_correct.checkDynamicParameters()

# Link node color_correct [out] -> [base_color] node standard_surface
color_correct_out = color_correct.getOutputPort('out')
standard_surface_in_base_color = standard_surface.getInputPort('base_color')
color_correct_out.connect(standard_surface_in_base_color)


# Create node ramp_float
rgh_ramp_float = NodegraphAPI.CreateNode('ArnoldShadingNode', network_material_create)
rgh_ramp_float.getParameter('name').setValue('rgh_ramp_float',0)
rgh_ramp_float.getParameter('nodeType').setValue('ramp_float',0)
rgh_ramp_float.checkDynamicParameters()

# Link node rgh_ramp_float [out] -> [specular_roughness] node standard_surface
rgh_ramp_float_out = rgh_ramp_float.getOutputPort('out')
standard_surface_in_specular_roughness = standard_surface.getInputPort('specular_roughness')
rgh_ramp_float_out.connect(standard_surface_in_specular_roughness)


# create node met_ramp_float
met_ramp_float = NodegraphAPI.CreateNode('ArnoldShadingNode',network_material_create)
met_ramp_float.getParameter('name').setValue('met_ramp_float',0)
met_ramp_float.getParameter('nodeType').setValue('ramp_float',0)
met_ramp_float.checkDynamicParameters()

# Link node met_ramp_float [out] -> [metalness] node standard_surface
met_ramp_float_out = met_ramp_float.getOutputPort('out')
standard_surface_in_metalness = standard_surface.getInputPort('metalness')
met_ramp_float_out.connect(standard_surface_in_metalness)


# create node normal_map
normal_map = NodegraphAPI.CreateNode('ArnoldShadingNode',network_material_create)
normal_map.getParameter('name').setValue('normal_map',0)
normal_map.getParameter('nodeType').setValue('normal_map',0)
normal_map.checkDynamicParameters()

# Link node normal_map [out] -> [normal] node standard_surface
normal_map_out = normal_map.getOutputPort('out')
standard_surface_in_normal = standard_surface.getInputPort('normal')
normal_map_out.connect(standard_surface_in_normal)


# create node image_baseColor
image_col = NodegraphAPI.CreateNode('ArnoldShadingNode', network_material_create)
image_col.getParameter('name').setValue('col',0)
image_col.getParameter('nodeType').setValue('image', 0)
image_col.checkDynamicParameters()

# Link node col [out] -> [input] node color_correct
image_col_out = image_col.getOutputPort('out')
color_correct_input = color_correct.getInputPort('input')
image_col_out.connect(color_correct_input)


# create node image_roughtness
image_rgh = NodegraphAPI.CreateNode('ArnoldShadingNode', network_material_create)
image_rgh.getParameter('name').setValue('rgh',0)
image_rgh.getParameter('nodeType').setValue('image', 0)
image_rgh.checkDynamicParameters()

# Link node rgh [out] -> [input] node rgh_ramp_float
image_rgh_out = image_rgh.getOutputPort('out')
rgh_ramp_float_input = rgh_ramp_float.getInputPort('input')
image_rgh_out.connect(rgh_ramp_float_input)


# create node image_matelness
image_met = NodegraphAPI.CreateNode('ArnoldShadingNode', network_material_create)
image_met.getParameter('name').setValue('met',0)
image_met.getParameter('nodeType').setValue('image',0)
image_met.checkDynamicParameters()

# Link node mat [out] -> [metalness] node met_ramp_float
image_met_out = image_met.getOutputPort('out')
met_ramp_float_input = met_ramp_float.getInputPort('input')
image_met_out.connect(met_ramp_float_input)


# create node image_normal_map
image_normal_map = NodegraphAPI.CreateNode('ArnoldShadingNode', network_material_create)
image_normal_map.getParameter('name').setValue('nrm',0)
image_normal_map.getParameter('nodeType').setValue('image',0)
image_met.checkDynamicParameters()

# Link node nrm [out] -> [normal] node normal_map
image_normal_map_out = image_normal_map.getOutputPort('out')
normal_map_input = normal_map.getInputPort('input')
image_normal_map_out.connect(normal_map_input)


# Position Node
standard_surface_position = NodegraphAPI.GetNodePosition(standard_surface)

NodegraphAPI.SetNodePosition(color_correct,(standard_surface_position[0]-400,standard_surface_position[1]))
NodegraphAPI.SetNodePosition(rgh_ramp_float,(standard_surface_position[0]-400,standard_surface_position[1]-400))
NodegraphAPI.SetNodePosition(met_ramp_float,(standard_surface_position[0]-400,standard_surface_position[1]-800))
NodegraphAPI.SetNodePosition(normal_map,(standard_surface_position[0]-400,standard_surface_position[1]-1200))

NodegraphAPI.SetNodePosition(image_col,(standard_surface_position[0]-800,standard_surface_position[1]))
NodegraphAPI.SetNodePosition(image_rgh,(standard_surface_position[0]-800,standard_surface_position[1]-400))
NodegraphAPI.SetNodePosition(image_met,(standard_surface_position[0]-800,standard_surface_position[1]-800))
NodegraphAPI.SetNodePosition(image_normal_map,(standard_surface_position[0]-800,standard_surface_position[1]-1200))