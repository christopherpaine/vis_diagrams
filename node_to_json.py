import sys
import json

def process_input(input_file, output_file):
    output_dict = {}
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            if ';' in line:
                values = line.split(';')
                output_dict[values[0]] = values[1]
            else:
                output_dict[line] = ""

    with open(output_file, 'w') as f:
        json.dump(output_dict, f, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input_file output_file")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    process_input(input_file, output_file)

