# Create the 'prompts' directory if it does not exist
mkdir -p prompts

# Read each line (i.e., each file path) from files.txt
while IFS= read -r file_path
do
    # Generate a unique output file name based on the input file name
    # For example, if file_path is "$HOME/projects/filebot/Dockerfile",
    # the output file will be "Dockerfile_output.txt"
    output_file="$(basename "$file_path")_output.txt"

    # Run the sed command using the current file_path and save the result
    # in the uniquely named output file
    # It first replaces $file_path with the actual file path,
    # and then replaces $Document with the content of the file specified by file_path
    sed -e "s|\$file_path|$file_path|g" -e "s/\$Document/$(sed 's/[&/]/\\&/g' <"$file_path" | sed ':a;N;$!ba;s/\n/\\n/g')/g" ./prompt.txt > "prompts/$output_file"

done < files.txt
