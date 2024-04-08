import os

class FileManager:
    def __init__(self, root_dir):
        self.root_dir = root_dir

    def list_files(self):
        try:
            files = os.listdir(self.root_dir)
            print("Files in the directory:")
            for file in files:
                print(file)
        except OSError as e:
            print(f"Error: {e}")

    def delete_file(self, filename):
        try:
            filepath = os.path.join(self.root_dir, filename)
            if os.path.exists(filepath):  # Check if the file exists
                os.remove(filepath)
                print("File deleted successfully!")
            else:
                print("File not found.")
        except OSError as e:
            print(f"Error: {e}")

def main():
    root_dir = "/Users/mariamcnally/Downloads/privatefolder"
    file_manager = FileManager(root_dir)
    
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
