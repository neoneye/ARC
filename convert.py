# Convert from a compacted json file, to the same json formatting as in the original ARC dataset.
# The input file is named "input.json"
# The output file is named "output.json"
import json

def custom_json_formatter(data):
    # Helper function to format lists with single spaces
    if isinstance(data, list):
        return '[' + ', '.join(custom_json_formatter(item) for item in data) + ']'
    elif isinstance(data, dict):
        items = (f'"{key}": {custom_json_formatter(value)}' for key, value in data.items())
        return '{' + ', '.join(items) + '}'
    elif isinstance(data, str):
        return f'"{data}"'
    else:
        return str(data)

def reformat_json(input_file, output_file):
    # Read the original JSON data
    with open(input_file, 'r') as file:
        json_data = json.load(file)

    # Apply the custom formatting
    formatted_json = custom_json_formatter(json_data)

    # Write the formatted JSON to the output file
    with open(output_file, 'w') as file:
        file.write(formatted_json)

# Example usage
reformat_json('input.json', 'output.json')
