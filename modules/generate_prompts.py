import os

def create_prompts_directory(directory_path="prompts"):
    """
    Create the 'prompts' directory if it does not exist.
    Ensures that there is a directory to save the output files into.

    :param directory_path: The path of the directory to be created.
    :type directory_path: str
    """
    os.makedirs(directory_path, exist_ok=True)

def read_file_paths(file_path="files.txt"):
    """
    Read each line (i.e., each file path) from files.txt.

    :param file_path: The path of the file containing the file paths.
    :type file_path: str
    :return: A list of file paths.
    """
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def generate_output_file_name(input_file_path):
    """
    Generate a unique output file name based on the input file name.
    Constructs a new file name based on the name of the input file,
    appending '_docs.md' to create a unique name for the output file.

    :param input_file_path: The path of the input file.
    :type input_file_path: str
    :return: A string representing the output file name.
    """
    return os.path.basename(input_file_path) + '_docs.md'

def replace_placeholder_in_template(template_path, file_path, output_path):
    """
    Replace '$filepath' placeholder with the actual file path.
    Reads the template from 'prompt.txt', replaces the placeholder '$filepath'
    with the actual path of the current file, and writes the result to the specified output file.

    :param template_path: The path of the template file.
    :type template_path: str
    :param file_path: The actual file path to replace the placeholder in the template.
    :type file_path: str
    :param output_path: The path where the output file will be saved.
    :type output_path: str
    """
    with open(template_path, 'r') as template_file:
        content = template_file.read()
    content = content.replace('$filepath', file_path)

    with open(output_path, 'w') as output_file:
        output_file.write(content)

def generate_prompts():
    """
    Main function to process files based on the script logic.
    """
    create_prompts_directory()

    # Read file paths
    file_paths = read_file_paths()

    # Process each file path
    for file_path in file_paths:
        # Generate unique output file name
        output_file_name = generate_output_file_name(file_path)
        output_file_path = os.path.join("prompts", output_file_name)

        # Replace placeholder in the template and write to the output file
        replace_placeholder_in_template('./prompt.txt', file_path, output_file_path)
