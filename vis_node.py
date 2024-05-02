import json
import sys

# Check if the command line arguments are provided
if len(sys.argv) != 4:
    print("Usage: python script.py <input_file1> <input_file2> <output_file>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[3]
input_file2 = sys.argv[2]

# Read the JSON data from the specified input file
try:
    with open(input_file, 'r') as file:
        data = json.load(file)
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
    sys.exit(1)


try:
    with open(input_file2, 'r') as file:
        data2 = json.load(file)
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
    sys.exit(1)


# Open the specified output file to write the HTML content
try:
    with open(output_file, 'w') as outfile:
        # Write the HTML header and opening script tags
        outfile.write("""<!DOCTYPE html>
<html lang="en" style="height: 100%;">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Mind Map</title>
<link href="https://unpkg.com/vis-network/styles/vis-network.min.css" rel="stylesheet" type="text/css" />
<script type="text/javascript" src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
<style>
html, body {
    height: 100%;
    margin: 0;
}

body {
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>
</head>
<body>
<div id="mymindmap" style="width: 100%; height: 100%; border: 1px solid lightgray;"></div>


<script>
var nodes = new vis.DataSet([
""")

        # Iterate through each item in the dictionary
        for idx, (key, value) in enumerate(data.items(), start=1):
            # Format the node entry
            node_entry = f"    {{id: {idx}, label: '{key}', title: '{value}'}},\n"
            # Write each node entry to the file
            outfile.write(node_entry)

        outfile.write("""
// Add more nodes as needed
]);

var edges = new vis.DataSet([
               """)


        for key, value in data2.items():
            # value is a list, so value[0] is the first item and value[1] is the second item
            node_entry2 = f"    {{from: {value[0]}, to: {value[1]}}},\n"
            # Write each node entry to the file
            outfile.write(node_entry2)

        outfile.write("""
               
    // Define more edges as needed
]);

var container = document.getElementById('mymindmap');
var data = {
    nodes: nodes,
    edges: edges
};
var options = {
    nodes: {
        shape: 'dot',
        size: 20,
        font: {
            size: 15,
            color: '#000000'
        },
        borderWidth: 2
    },
    edges: {
        width: 2
    },
    physics: {
        forceAtlas2Based: {
            gravitationalConstant: -50,
            centralGravity: 0.005,
            springLength: 100,
            springConstant: 0.18
        },
        maxVelocity: 146,
        solver: 'forceAtlas2Based',
        timestep: 0.35,
        stabilization: {iterations: 150}
    }
};
var network = new vis.Network(container, data, options);




</script>

</body>
</html>

               """)







except Exception as e:
    print(f"An error occurred while writing to the file: {e}")
    sys.exit(1)

print(f"Data has been written to {output_file}")

