import os

def rename_files(folder):
    files = os.listdir(folder)

    for i, file in enumerate(files):
        old_path = os.path.join(folder, file)
        new_path = os.path.join(folder, f"file_{i}.txt")

        os.rename(old_path, new_path)

    print("Files renamed successfully")