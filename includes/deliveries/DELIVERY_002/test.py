import sys

def print_file_contents(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)

def main():
    print("main func")

if __name__ == "__main__":
    file_path = 'xxx/abc.sql'
    if len(sys.argv) > 1:
        if sys.argv[1] == "print_file_contents":
            print_file_contents(file_path)
        else:
            print("Invalid argument")
    else:
        main()
