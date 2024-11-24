python3 vis_diagrams/node_to_json.py node node.json 
python3 vis_diagrams/rel_to_json.py rels rels.json
python3 vis_diagrams/vis_node.py node.json rels.json output.html
firefox output.html
