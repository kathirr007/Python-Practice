"""Organizes files in the given directory into subfolders based on file type."""

import os
import shutil


def organize_files(source_dir):
    """
    Organizes files in the given directory into subfolders based on file type.

    Args:
        source_dir: The path to the source directory.

    Returns:
        None
    """

    file_types = {
        "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
        "documents": [
            ".pdf",
            ".doc",
            ".docx",
            ".txt",
            ".rtf",
            ".xls",
            ".xlsx",
            ".ppt",
            ".pptx",
        ],
        "archives": [".zip", ".rar", ".7z", ".gz", ".tar"],
        "videos": [".mp4", ".avi", ".mov", ".mkv"],
        "audio": [".mp3", ".wav", ".flac"],
        "others": [],  # For files that don't match any other category
    }

    for filename in os.listdir(source_dir):
        src_path = os.path.join(source_dir, filename)

        if os.path.isfile(src_path):
            file_ext = os.path.splitext(filename)[1].lower()

            for category, extensions in file_types.items():
                if file_ext in extensions:
                    dest_dir = os.path.join(source_dir, category)
                    os.makedirs(
                        dest_dir, exist_ok=True
                    )  # Create the destination directory if it doesn't exist
                    dest_path = os.path.join(dest_dir, filename)
                    shutil.move(src_path, dest_path)
                    break
            else:
                # If no match found, move to "Others" folder
                dest_dir = os.path.join(source_dir, "Others")
                os.makedirs(dest_dir, exist_ok=True)
                dest_path = os.path.join(dest_dir, filename)
                shutil.move(src_path, dest_path)


if __name__ == "__main__":
    source_directory = input("Enter the source directory path: ")
    organize_files(source_directory)
