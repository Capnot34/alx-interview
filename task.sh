#!/bin/bash

# Function to create README.md for each project
create_readme() {
    local project_name=$1
    local project_directory=$2

    cat > "$project_directory/README.md" <<EOF
# $project_name

## Description
This project focuses on implementing $project_name in Python.

## Requirements
* Python 3.x

## How to Use
1. Clone the repository.
2. Navigate to the $project_directory directory.
3. Run the main script to see the Pascal's Triangle output.

## Files
* \`$project_name.py\`: Python script containing the implementation of $project_name.
* \`main.py\`: Main script to test the functionality of $project_name.

## Example
\`\`\`bash
$ python3 main.py
\`\`\`

## Author
Written by [Your Name]

EOF
}

# Function to create project directories and files
create_project() {
    local project_name=$1

    # Create directory for the project
    mkdir "$project_name"

    # Create README.md for the project
    create_readme "$project_name" "$project_name"

    # Create Python script file
    touch "$project_name/$project_name.py"

    # Populate Python script file
    cat > "$project_name/$project_name.py" <<EOF
def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n.
    """
    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        triangle.append(row)

    return triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    triangle = pascal_triangle(5)
    print_triangle(triangle)
EOF

    # Create main script file
    touch "$project_name/main.py"

    # Populate main script file
    cat > "$project_name/main.py" <<EOF
#!/usr/bin/python3
"""
Main script to test the functionality of $project_name
"""
from $project_name import pascal_triangle, print_triangle

if __name__ == "__main__":
    triangle = pascal_triangle(5)
    print_triangle(triangle)
EOF

    # Create README.md for the project
    create_readme "$project_name" "$project_name"
}

# Create project directory and files
create_project "0-pascal_triangle"


