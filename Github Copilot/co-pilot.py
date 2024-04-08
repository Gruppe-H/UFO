import os
import sys

class FileManager:
    def __init__(self, root_dir):
        self.root_dir = root_dir

    def list_files(self):
        # securely list files and handle exceptions
        try:
            files = os.listdir(self.root_dir)
            # print files in the directory
            print("Files in the directory: ")
            for file in files:
                print(file)
        # handle exceptions
        except FileNotFoundError:
            print("Directory not found")
        except PermissionError:
            print("Permission denied")
        except Exception as e:
            print("An error occurred: ", e)
        
    def create_file(self, file_name):
        # securely create file and handle exceptions
        try:
            with open(os.path.join(self.root_dir, file_name), 'w') as file:
                print(f"File {file_name} created successfully")
        except FileNotFoundError:
            print("Directory not found")
        except PermissionError:
            print("Permission denied")
        except Exception as e:
            print("An error occurred: ", e)

    def delete_file(self, file_name):
        # securely delete file and handle exceptions
        try:
            os.remove(os.path.join(self.root_dir, file_name))
            print(f"File {file_name} deleted successfully")
        except FileNotFoundError:
            print("Directory not found")
        except PermissionError:
            print("Permission denied")
        except Exception as e:
            print("An error occurred: ", e)

# create an instance of FileManager
def main():
    root_dir = "/Users/mariamcnally/Desktop/SW2Semester/UFO/Filepath"

    file_manager = FileManager(root_dir)

    # print a menu for selecting an option
    print("Select an option: ")
    print("1. List files")
    print("2. Create file")
    print("3. Delete file")
    print("4. Exit")
    option = input("Enter option: ")

    # handle user input
    if option == "1":
        file_manager.list_files()
    elif option == "2":
        file_name = input("Enter file name: ")
        file_manager.create_file(file_name)
    elif option == "3":
        file_name = input("Enter file name: ")
        file_manager.delete_file(file_name)
    elif option == "4":
        print("Exiting...")
        sys.exit()
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()

      
    