#!/bin/bash

# Function to traverse directories
traverse() {
    for file in "$1"/*; do
        if [ -d "$file" ]; then
            # If directory, then traverse it, unless it's certain directories.
            if [[ "$file" != *"osan3-files"* ]] && [[ "$file" != *"docs"* ]] && [[ "$file" != *"filebot-store-000"* ]] && [[ "$file" != *".git"* ]] && [[ "$file" != *"__pycache__"* ]]; then
                echo "$file"
                traverse "$file"
            fi
        elif [ -f "$file" ]; then
            # If file, print its full path
            echo "$file"
        fi
    done
}

# Start traversing from the current directory
traverse .
