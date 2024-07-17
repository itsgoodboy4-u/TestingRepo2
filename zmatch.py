def compare_files(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        file1_lines = file1.readlines()
        file2_lines = file2.readlines()

    max_lines = max(len(file1_lines), len(file2_lines))
    differences = []
    count = 0 
    for i in range(max_lines):
        line1 = file1_lines[i].strip() if i < len(file1_lines) else None
        line2 = file2_lines[i].strip() if i < len(file2_lines) else None

        if line1 != line2:
            count += 1
            differences.append((i + 1, line1, line2))

            if count == 1:
                # return differences
                print(f"Line {i+1}:\nMyFile: {line1}\nCurruptedFile: {line2}\n")

def print_differences(differences):
    for line_number, line1, line2 in differences:
        print(f"Line {line_number}:\nMyFile: {line1}\nCurruptedFile: {line2}\n")

# Example usage
file1_path = 'myInflux'
file2_path = 'influc.conf.txt'
differences = compare_files(file1_path, file2_path)
# print_differences(differences)
