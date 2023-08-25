import os
import re

def create_mirror_directory(root_dir, dir_path, output_dir):
    """
    Creates a mirror directory location in the output directory for the given directory path.
    """
    relative_path = os.path.relpath(root_dir, dir_path)
    mirror_dir = os.path.join(output_dir, relative_path)
    os.makedirs(mirror_dir, exist_ok=True)

def document_source_files(dir_path, output_dir):
    """
    Traverse through directories from the given directory path and create mirrored documentation
    directories in the output directory. The directory where the script is run will have a 'files.txt'
    containing the paths of all source code files.
    """
    source_code_pattern = re.compile(r".*\.(py|java|c|cpp|js|ts|go|rs|rb|php|swift|kt|scala|m|h|hpp|cs|sh|bash)$")

    source_files = []

    for root, dirs, files in os.walk(dir_path):
        if '.git' in dirs:
            dirs.remove('.git')

        # Create mirrored directories without files
        create_mirror_directory(root, dir_path, output_dir)

        for file_name in files:
            if source_code_pattern.match(file_name):
                full_path = os.path.join(root, file_name)
                source_files.append(full_path)

    # Write the full paths of the source code files to 'files.txt' in the directory where the script is executed
    with open('files.txt', 'w') as docfile:
        for file_path in source_files:
            docfile.write(file_path + '\n')

if __name__ == "__main__":
    document_source_files("docubot", "documentation")
