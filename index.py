import os
import zipfile

def create_attachment_index():
    with open('index.txt', 'w') as index_file:
        for filename in os.listdir('.'):
            if filename.endswith('.zip'):
                index_file.write(f"Attachments in {filename}:\n")
                try:
                    with zipfile.ZipFile(filename, 'r') as zip_ref:
                        for file_info in zip_ref.infolist():
                            index_file.write(f"- {file_info.filename}\n")
                except zipfile.BadZipFile:
                    index_file.write("  Error: Unable to read zip file\n")
                index_file.write("\n")

if __name__ == "__main__":
    create_attachment_index()
    print("Index file 'index.txt' has been created.")