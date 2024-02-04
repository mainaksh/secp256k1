import os

def search_in_files(directory, search_string):
    result = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        for line_number, line in enumerate(f, start=1):
                            if search_string in line:
                                print(f"Found in {file_path}, Line {line_number}: {line.strip()}")
                                result.append((file_path, line_number, line.strip()))
                except UnicodeDecodeError:
                    print(f"Skipping {file_path} due to UnicodeDecodeError")

    return result

def main():
    # Get user input for directory path
    directory_path = input("Enter the directory path to search into: ").strip()

    # Validate the directory path
    if not os.path.isdir(directory_path):
        print("Invalid directory path. Please provide a valid directory path.")
        return

    # Get user input for the 66-character string
    user_input = input("Enter a 66-character string starting with '03' or '02': ")

    # Validate user input
    if len(user_input) == 66 and (user_input.startswith('03') or user_input.startswith('02')):
        # Search for the input string in all text files under the specified directory
        search_result = search_in_files(directory_path, user_input)

        # Display the result
        if search_result:
            print("\nSearch completed. Found in the following locations:")
            for file_path, line_number, line_content in search_result:
                print(f"{file_path}, Line {line_number}: {line_content}")
        else:
            print("\nString not found in any text files in the specified directory.")

    else:
        print("Invalid input. Please enter a 66-character string starting with '03' or '02'.")

if __name__ == "__main__":
    main()
