import os
import shutil
folder = input("Enter folder path: ")
if not os.path.exists(folder):
    print("Folder not found.")
else:
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Videos": [".mp4", ".avi", ".mkv"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
        "Music": [".mp3", ".wav"],
        "Archives": [".zip", ".rar"]
    }
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path):
            extension = os.path.splitext(file)[1].lower()
            for category, extensions in categories.items():
                if extension in extensions:
                    category_folder = os.path.join(folder, category)
                    if not os.path.exists(category_folder):
                        os.mkdir(category_folder)
                    shutil.move(
                        file_path,
                        os.path.join(category_folder, file)
                    )
                    print(file, "->", category)
                    break
    print("Files organized successfully!")