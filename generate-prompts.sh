#!/bin/bash

# Create the 'prompts' directory if it does not exist
# Ensures that there is a directory to save the output files into.
mkdir -p prompts

# Read each line (i.e., each file path) from files.txt
# Iterates over each line in the 'files.txt' file,
# where each line is expected to be a path to a file.
while IFS= read -r file_path
do
    # Generate a unique output file name based on the input file name
    # Constructs a new file name based on the name of the input file,
    # appending '_output.txt' to create a unique name for the output file.
    output_file="$(basename "$file_path")_docs.md"

    # Escape special characters in the file path
    # Prepares the file path string so that it can be safely used in a sed command.
    escaped_file_path=$(printf '%s\n' "$file_path" | sed 's:[\/&]:\\&:g;$!s/$/\\/')

    # Replace '$filepath' placeholder with the actual file path
    # The sed command reads the template from 'prompt.txt',
    # replaces the placeholder '$filepath' with the actual path of the current file.
    sed -e "s|\$filepath|$escaped_file_path|g" \
        ./prompt.txt > "prompts/$output_file"

done < files.txt

# Script Description:
# This script reads a list of file paths from 'files.txt',
# processes each of these files to replace placeholders in a template text ('prompt.txt'),
# and then writes the processed text to a new file in the 'prompts' directory.
