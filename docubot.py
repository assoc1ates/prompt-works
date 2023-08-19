import os
import asyncio
import sys
from modules.llm_model import generate_completion
from modules.source_code_finder import traverse
from modules.generate_prompts import generate_prompts

def read_api_key(file_path="openai_api_key"):
    """
    Read the OpenAI API key from a file.

    :param file_path: The path to the file containing the OpenAI API key.
    :type file_path: str
    :return: The OpenAI API key as a string.
    """
    with open(file_path, "r") as key_file:
        return key_file.read().strip()

# Set the OpenAI API key
openai_api_key = read_api_key()
os.environ["OPENAI_API_KEY"] = openai_api_key
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

async def process_files(input_dir, output_dir):
    """
    Asynchronously process files from the input directory
    and save the generated completions to the output directory.

    :param input_dir: The path to the directory with prompt files.
    :type input_dir: str
    :param output_dir: The path to the directory where output will be saved.
    :type output_dir: str
    """
    # Create the output directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through all the files in the input directory
    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)

        # Only process files (not directories)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                prompt = file.read()

            # Generate completion using the OpenAI API
            completion = await generate_completion(prompt)

            # Write the completion to a new file in the output directory
            output_file_path = os.path.join(output_dir, filename)
            with open(output_file_path, 'w') as output_file:
                output_file.write(completion)

def main(input_dir, output_dir):
    """
    Main function that gets invoked when the script is run directly.
    It takes the input and output directory paths from the command line arguments,
    calls the traverse function from the source_code_finder module,
    and then runs the asynchronous process_files function.
    """
    print("input_dir arg:", input_dir)
    print("output_dir arg:", output_dir)

    # Run the traverse function from the source_code_finder module
    traverse(input_dir, output_dir)
    # Run the generate_prompts function from generate_prompts module
    generate_prompts()

    # Run the asynchronous function to process all files
    asyncio.run(process_files('prompts', 'output-docs'))

# This is the standard boilerplate that calls the 'main' function
# when the script is run directly
if __name__ == "__main__":
    # Check if the command line arguments are provided
    if len(sys.argv) < 3:
        print("Usage: python docubot.py <input_dir_path> <output_dir_path>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])