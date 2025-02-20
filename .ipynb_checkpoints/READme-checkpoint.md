# File Processor Script

This script processes files with specific extensions (.py, .cpp, .yaml) in a given directory and concatenates their contents into a single output file.

## Features

- Processes files with extensions .py, .cpp, and .yaml.
- Concatenates the contents of these files into a single output file.
- Supports command-line arguments for directory and output file specification.

## Requirements

- Python 3.x

## Usage

1. Clone the repository or download the script:
   Ensure you have the script saved locally on your machine.

2. Open a terminal or command prompt:
   Navigate to the directory where the script is located.

3. Run the script:
   Use the following command to execute the script:

   `python script_name.py --dir <input_directory> --out <output_file>`

   Replace <input_directory> with the path to the directory containing the files you want to process, and <output_file> with the desired name of the output file (without extension).

### Example

`python script_name.py --dir /path/to/input_directory --out output_filename`

This command will process all .py, .cpp, and .yaml files in /path/to/input_directory and write their contents to output_filename.txt.

## License

This script is provided under the MIT License. See the LICENSE file for more details.
