def process_files(base_path, fill_path, remove_path, output_path):
    # Read fill_file
    with open(fill_path, 'r') as fill_file:
        fill_line = fill_file.readline().rstrip()

    # Remove newline characters and trailing whitespace from fill_line
    fill_line = fill_line.replace('\r', '').replace('\n', '').strip()

    # Read remove_file
    with open(remove_path, 'r') as remove_file:
        remove_line = remove_file.readline().rstrip() if remove_file else ""

    # Remove newline characters and trailing whitespace from remove_line
    remove_line = remove_line.replace('\r', '').replace('\n', '').strip()

    # Process base_file
    with open(base_path, 'r') as base_file:
        base_lines = base_file.readlines()

    modified_lines = []
    empty_line_count = 0

    for orig_line in base_lines:
        line = orig_line.rstrip()

        if not line:
            empty_line_count += 1
            line = fill_line
        elif remove_line:
            line = line.replace(remove_line, '')

        modified_lines.append(line)

    # Write the modifications to output_file
    with open(output_path, 'w') as output_file:
        output_file.write(f"There are {len(modified_lines)} lines in base file.\n")
        output_file.write(f"There are {empty_line_count} empty lines in base file.\n")
        for modified_line in modified_lines:
            output_file.write(f"{modified_line}\n")

if __name__ == "__main__":
    base_path = "path_to_base_file.txt"
    fill_path = "path_to_fill_file.txt"
    remove_path = "path_to_remove_file.txt"
    output_path = "path_to_output_file.txt"

    process_files(base_path, fill_path, remove_path, output_path)