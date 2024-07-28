import os
import re

def get_files():
    return [f for f in os.listdir() if os.path.isfile(f)]

def sort_files(files):
    return sorted(files, key=lambda x: re.sub(r'^\d+_', '', x))

def rename_files(files):
    for index, file in enumerate(files, start=1):
        new_name = f"{index}_{re.sub(r'^\d+_', '', file)}"
        if file != new_name:
            os.rename(file, new_name)
            print(f"Renamed '{file}' to '{new_name}'")

def main():
    files = get_files()
    sorted_files = sort_files(files)
    rename_files(sorted_files)

if __name__ == "__main__":
    main()
