import os
import asyncio
from modules.llm_model import generate_completion

# Read the OpenAI API key from a file
with open("openai_api_key", "r") as key_file:
    openai_api_key = key_file.read().strip()

# Set the OpenAI API key
os.environ["OPENAI_API_KEY"] = openai_api_key
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

# Path to the directory with prompt files
input_dir = './prompts/'

# Path to the directory where output will be saved
output_dir = './output-docs/'

# Create the output directory if it does not exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

async def process_files():
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

def main():
    # Run the asynchronous function to process all files
    asyncio.run(process_files())

# This is the standard boilerplate that calls the 'main' function
# when the script is run directly
if __name__ == '__main__':
    main()
