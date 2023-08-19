import os
import re

def traverse(dir_path):
    """
    Recursively traverse through directories from the given directory path,
    and yield the full paths of known source code file types.
    Ignores directories named .git.

    :param dir_path: The root directory path to start traversing from.
    :type dir_path: str
    :yield: Full paths of known source code file types.
    :rtype: str
    """
    # Regular expression pattern to match known source code file types
    source_code_pattern = re.compile(r".*\.(py|java|c|cpp|js|ts|go|rs|rb|php|swift|kt|scala|m|h|hpp|cs|sh|bash)$")

    for root, dirs, files in os.walk(dir_path):
        # Remove .git directory from traversal, if it exists
        if '.git' in dirs:
            dirs.remove('.git')

        # Check each file in the current directory
        for file_name in files:
            if source_code_pattern.match(file_name):
                # Full path of the source code file
                full_path = os.path.join(root, file_name)
                yield full_path

if __name__ == "__main__":
    # Start traversing from the current directory, by default
    for source_file in traverse("."):
        print(source_file)
