import subprocess

def get_changed_files_in_commit(repo_path):
    """
    Get a list of changed or new files in the latest commit of a Git repository.

    Parameters:
    repo_path (str): The path to the Git repository.

    Returns:
    List[Dict[str, str]]: A list of dictionaries, where each dictionary contains
    the 'oid' (Object ID) of the latest commit and the 'file_path' of a changed or added file in that commit.
    """
    try:
        # Run the git command to get the Object ID and list of files changed in the last commit
        # --name-only: Show only names of changed files
        # --diff-filter=AM: Select only added or modified files
        result = subprocess.check_output(["git", "show", "--name-only", "--diff-filter=AM"],
                                          stderr=subprocess.STDOUT, cwd=repo_path)

        # Decode the result from bytes to string and split it into a list of lines
        lines = result.decode('utf-8').strip().split('\n')

        # The first line should be the commit hash, starting with 'commit '
        oid = lines[0].split(' ')[1] if lines and lines[0].startswith('commit ') else None

        # The remaining lines are file paths; we filter to ignore lines that are not file paths
        file_paths = [f for f in lines[1:] if f and not f.startswith(('Author:', 'Date:', '    '))]

        # Combine the Object ID and file paths into a list of dictionaries
        changed_files = [{'oid': oid, 'file_path': file_path} for file_path in file_paths]

        return changed_files

    except subprocess.CalledProcessError as e:
        print("Error occurred while checking git commit: ", e.output.decode('utf-8'))
        return []
    except Exception as e:
        print("An error occurred: ", e)
        return []

# Example usage:
repo_path = "/path/to/your/repo"
changed_files = get_changed_files_in_commit(repo_path)
print("Changed or new files in the latest commit:", changed_files)
