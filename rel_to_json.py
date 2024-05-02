import sys
import json

def process_input(input_file):
    data_dict = {}
    with open(input_file, 'r') as f:
        for i, line in enumerate(f, start=1):
            line = line.strip()
            if ',' in line:
                values = line.split(',')
                data_dict[str(i)] = [int(val) for val in values]
            else:
                print(f"Invalid data format in line {i}: {line}")
    return data_dict

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py input_file output_file")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    data_dict = process_input(input_file)

    with open(output_file, 'w') as f:
        json.dump(data_dict, f, indent=2)

if __name__ == "__main__":
    main()

