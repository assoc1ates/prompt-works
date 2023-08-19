import os
import re

def traverse(dir_path, output_dir):
    """
    Recursively traverse through directories from the given directory path,
    and write the full paths of known source code file types to a file named
    'files.txt' in a specified directory. Ignores directories named .git.

    :param dir_path: The root directory path to start traversing from.
    :type dir_path: str
    :param output_dir: The directory where 'files.txt' will be created.
    :type output_dir: str
    """
    # Regular expression pattern to match known source code file types
    source_code_pattern = re.compile(r".*\.(py|java|c|cpp|js|ts|go|rs|rb|php|swift|kt|scala|m|h|hpp|cs|sh|bash)$")

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Open the output file 'files.txt' in the specified directory
    with open(os.path.join(output_dir, 'files.txt'), 'w') as outfile:
        for root, dirs, files in os.walk(dir_path):
            # Remove .git directory from traversal, if it exists
            if '.git' in dirs:
                dirs.remove('.git')

            # Check each file in the current directory
            for file_name in files:
                if source_code_pattern.match(file_name):
                    # Full path of the source code file
                    full_path = os.path.join(root, file_name)
                    # Write the full path of the source code file to 'files.txt'
                    outfile.write(full_path + '\n')

if __name__ == "__main__":
    # Example usage
    # Start traversing from the current directory
    # Write the result to 'files.txt' in the directory named 'output'
    traverse(".", ".")
