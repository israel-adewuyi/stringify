import os
import argparse

files_of_interest = ["py", "cpp", "yaml"]

out_file_name = None

def process_files(dir):
    """
    If the file path is not a directory, then check if it's a file of interest. If it is, write its content to file. 
    If the file path is a directory, check which of it's files are files of interest or directories in themselves.
    """
    if not os.path.isdir(dir):
        partition = dir.split(".")
        if partition[-1] in files_of_interest:
            file_object = open(f"{dir}/{file_name}", "r", encoding="utf-8")

            with open(out_file_name, "a") as file:
                file.write(file_name)
                file.write(file_object.read())
    else:
        for file_name in os.listdir(dir):
            partition = file_name.split(".")
            if len(partition) == 1:
                process_files(f"{dir}/{file_name}")
            if partition[-1] in files_of_interest:
                file_object = open(f"{dir}/{file_name}", "r", encoding="utf-8")
    
                with open(out_file_name, "a") as file:
                    file.write(file_name)
                    file.write(file_object.read())
                

def main():
    global out_file_name
    parser = argparse.ArgumentParser(description="Process files in dir and write to output")

    parser.add_argument("--dir", required=True, help="The directory whose files are processed")
    parser.add_argument("--out", required=True, help="The directory to write to")

    args = parser.parse_args()

    directory = args.dir
    output = args.out

    out_file_name = f"{output}.txt"
    process_files(directory)


if __name__ == "__main__":
    main()