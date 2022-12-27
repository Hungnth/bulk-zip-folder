# Bulk zip folder
This script allows the user to zip all the subdirectories inside a given directory. The user is prompted to enter the path of the directory, and the script iterates over all the subdirectories in the input directory and creates a zip archive for each one of them. The resulting zip archives are stored in the input directory.

## Prerequisites
- Python 3
- The `shutil` module, which is part of the Python Standard Library and does not need to be installed separately.

## Usage
1. Clone the repository or download the script.
2. Open a terminal and navigate to the directory where the script is located.
3. Run the script using the following command:

```python
python zip-all-folders.py
```
4. When prompted, enter the path of the directory whose subdirectories you want to zip.

## Notes
- The script does not handle errors that may occur while creating the zip archives, such as if the input directory does not exist or if the user does not have permission to create files in the input directory. It is recommended to add error handling to the code to handle these cases.
- The zip archives will be created using the name of the subdirectories as the base name for the archive file. Make sure that the names of the subdirectories are unique within the input directory to avoid overwriting the zip archives.
