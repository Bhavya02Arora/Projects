# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class MyClass:
    def __init__(self):
        self.my_variable = 42

    def read_file(self):
        with open('file.txt', 'r') as file:
            lines = file.readlines()
        return lines

    def ccwc(self, content):
        """Count characters, words, and lines in the given content."""
        # number of bytes calculation
        num_bytes = len(content.encode('utf-8'))
        # number of characters calculation
        num_chars = len(content)
        # number of words
        num_words = len(content.split())
        # number of lines
        num_lines = len(content.splitlines())

        print(f"Bytes: {num_bytes}, Characters: {num_chars}, Words: {num_words}, Lines: {num_lines}")
        return num_bytes, num_chars, num_words, num_lines


if __name__ == "__main__":
    # argument parser for command line arguments

    my_instance = MyClass()
    lines = my_instance.read_file()
    num_bytes, num_chars, num_words, num_lines = my_instance.ccwc(''.join(lines))

    # import argparse
    # parser = argparse.ArgumentParser(description='Process some integers.')
    # parser.add_argument('--file', type=str, help='File to read')
    # args = parser.parse_args()
    # # If a file is provided, read it; otherwise, use the default 'file.txt'
    # if args.file:
    #     file_name = args.file
    # else:
    #     file_name = 'file.txt'
    # # Ensure the file exists
    import os
    # if not os.path.exists(file_name):
    #     print(f"File {file_name} does not exist.")
    #     exit(1)

    # take arguments from command line for wc like ccwc -w test.txt
    import sys
    if len(sys.argv) > 1:
        file_name = sys.argv[2]
    else:
        file_name = 'file.txt'
    # Check if the file exists
    if not os.path.isfile(file_name):
        print(f"File {file_name} does not exist.")
        exit(1)
    # Read the file and count characters, words, and lines
    import sys
    # Usage: ccwc -l [file_name]
    command = sys.argv[1] if len(sys.argv) > 1 else None
    print("Command: {}".format(command))
    if command and command.startswith('-'):
        if command == '-l':
            print("Counting lines in the file...")
            print(f"Number of lines: {num_lines}")
        elif command == '-w':
            print("Counting words in the file...")
            print(f"Number of words: {num_words}")
        elif command == '-c':
            print("Counting characters in the file...")
            print(f"Number of characters: {num_chars}")
        else:
            print(f"Unknown command: {command}")
            exit(1)
    else:
        print("No valid command provided. Defaulting to counting characters, words, and lines.")
    # Create an instance of MyClass and call its methods



