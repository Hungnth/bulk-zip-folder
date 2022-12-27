import os
import shutil

dir_path = input("Enter the path of the directory you want to zip: ")

# Get a list of all subdirectories in the input directory
subdirs = [subdir for subdir in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, subdir))]

# Iterate over the subdirectories
for subdir in subdirs:
    # Create a zip archive of the subdirectory
    print(f"Zipping {subdir}...")
    shutil.make_archive(os.path.join(dir_path, subdir), 'zip', dir_path, subdir)
