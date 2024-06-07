import os
import shutil


def move_files_to_new_folders(source_folder, destination_folder):
    for i in range(1, 4):
        for j in range(1, 4):
            current_file = os.path.join(source_folder, str(j), f"{i}.jpg")
            current_file_alternative = os.path.join(source_folder, str(j), f"{i}_.jpg")

            if os.path.exists(current_file):
                new_folder = os.path.join(destination_folder, str(i))
                os.makedirs(new_folder, exist_ok=True)
                new_file = os.path.join(new_folder, f"{j}.jpg")
                shutil.copy(current_file, new_file)
            elif os.path.exists(current_file_alternative):
                new_folder = os.path.join(destination_folder, str(i))
                os.makedirs(new_folder, exist_ok=True)
                new_file = os.path.join(new_folder, f"{j}.jpg")
                shutil.copy(current_file_alternative, new_file)
                os.rename(new_file, new_file.replace("_.jpg", ".jpg"))

def process_folder(folder):
    new_folder = f"{folder}_new"

    os.makedirs(new_folder, exist_ok=True)

    move_files_to_new_folders(folder, new_folder)

    for i in range(1, 4):
        shutil.rmtree(os.path.join(folder, str(i)))

    for root, dirs, _files in os.walk(new_folder):
        for d in dirs:
            shutil.move(os.path.join(root, d), folder)

    shutil.rmtree(new_folder)
