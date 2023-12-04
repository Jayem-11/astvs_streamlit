import os
import glob

def get_files_with_blob(directory, blob):
    # Change the current directory to the specified directory
    os.chdir(directory)

    # Use glob to get all the files in the directory with the specified blob
    files = glob.glob(blob)

    return files


def delete_files(files):
    for file in files:
        # Check if it is a file (not a directory)
        if os.path.isfile(file):
            os.remove(file)  # Delete the file


