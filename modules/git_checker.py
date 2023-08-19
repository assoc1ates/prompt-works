import subprocess

def get_changed_files_in_commit(repo_path):
    """
    Get a list of changed or new files in the latest commit of a Git repository.

    Parameters:
    repo_path (str): The path to the Git repository.

    Returns:
    List[str]: A list of file paths that were changed or added in the latest commit.
    """
    try:
        # Run the git command to get a list of files changed in the last commit
        # --name-only: Show only names of changed files
        # --diff-filter=A: Select only added files
        # --diff-filter=M: Select only modified files
        result = subprocess.check_output(["git", "show", "--name-only", "--diff-filter=AM"],
                                          stderr=subprocess.STDOUT, cwd=repo_path)

        # Decode the result from bytes to string and split it into a list of file paths
        files = result.decode('utf-8').strip().split('\n')

        # Filter out the commit hash and any empty strings
        files = [f for f in files if f and not f.startswith('commit ')]

        return files

    except subprocess.CalledProcessError as e:
        print("Error occurred while checking git commit: ", e.output.decode('utf-8'))
        return []
    except Exception as e:
        print("An error occurred: ", e)
        return []

# Example usage:
repo_path = "/path/to/git/project"
changed_files = get_changed_files_in_commit(repo_path)
print("Changed or new files in the latest commit:", changed_files)