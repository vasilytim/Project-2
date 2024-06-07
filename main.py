# Не забываем добавить файлы А, Б, В, Г

from functions import process_folder

folders = ["А", "Б", "В", "Г"]

for folder in folders:
    print(f"Processing folder {folder}")
    process_folder(folder)

print("Program execution completed.")
