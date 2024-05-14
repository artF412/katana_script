# katana --script new.py /home/faiz/Documents/katana/farm_settings/scan_test.katana /home/faiz/Documents/katana/farm_settings/ver_edit/scan_test_up.katana

import time
from Katana import NodegraphAPI
from Katana import KatanaFile
import sys

print("Start")
start_time = time.time()

old = sys.argv[1]
change = sys.argv[2]

# open file .katana
open_file = KatanaFile.Load(old)

# Function to find nodes connected to a given node
def find_connected_nodes(node):
    connected_nodes = []
    for port in node.getInputPorts():

        # Check if the port is connected
        connected_port = port.getConnectedPort(0)
        if connected_port:

            # If connected, get the connected node and append it to the list
            connected_node = connected_port.getNode()
            connected_nodes.append(connected_node)

        return connected_nodes

# Main function
def main():
    # Get the root node of the scene
    root_node = NodegraphAPI.GetRootNode()

    # Find all nodes of type Render
    render_nodes = NodegraphAPI.GetAllNodesByType("Render")

    for render_node in render_nodes:
        connected_nodes = find_connected_nodes(render_node)
        if connected_nodes:
            for connected_node in connected_nodes:
                if not connected_node.getName().startswith("FARM_SETTINGS"):

                    # Create node "FARM_SETTINGS" and Connect FARM_SETTINGS node to node render and connected_node
                    connected_node_out = connected_node.getOutputPort('out')
                    create_node_farmSettings = NodegraphAPI.CreateNode('FARM_SETTINGS')
                    farmSettings_correct_input = create_node_farmSettings.getInputPort('i0')
                    connected_node_out.connect(farmSettings_correct_input)
                    farmSettings_correct_out = create_node_farmSettings.getOutputPort('o0')
                    render_node_input = render_node.getInputPort('input')
                    farmSettings_correct_out.connect(render_node_input)

                    # Get the position of the Render node and Set position
                    render_position = NodegraphAPI.GetNodePosition(render_node)
                    NodegraphAPI.SetNodePosition(create_node_farmSettings,(render_position[0],render_position[1]+100))
        else:
            # Create node "FARM_SETTINGS" and Connect render node to FARM_SETTINGS node
            create_node_farmSettings = NodegraphAPI.CreateNode('FARM_SETTINGS')
            farmSettings_correct_out = create_node_farmSettings.getOutputPort('o0')
            render_node_input = render_node.getInputPort('input')
            farmSettings_correct_out.connect(render_node_input)

            # Get the position of the Render node and Set position
            render_position = NodegraphAPI.GetNodePosition(render_node)
            NodegraphAPI.SetNodePosition(create_node_farmSettings,(render_position[0],render_position[1]+200))

# Call the main function
main()

# save new file .katana
save_file = KatanaFile.Save(change)

# calculate time this programe
end_time = time.time()
duration_in_seconds = end_time - start_time
duration_in_milliseconds = duration_in_seconds
print("Time : {} sec".format(duration_in_milliseconds))