import os

class FileManager:
    def __init__(self):
        self.root_dir = "/Users/mariamcnally/Downloads/privatefolder"

        ## Non accessible directories
        # /Users/mariamcnally/Downloads/privatefolder

        #default directory
        # /Users/mariamcnally/Desktop/SW2Semester/UFO/Filepath

    def list_files(self):
        files = os.listdir(self.root_dir)
        print("Files in the directory:")
        for file in files:
            print(file)

    def delete_file(self, filename):
        filepath = os.path.join(self.root_dir, filename)
        os.system("rm " + filepath)
        print("File deleted successfully!")

def main():
    file_manager = FileManager()
    
    print("Welcome to File Manager!")
    while True:
        print("\nMenu:")
        print("1. List files")
        print("2. Delete file")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            file_manager.list_files()
        elif choice == "2":
            filename = input("Enter the file name you want to delete: ")
            file_manager.delete_file(filename)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
