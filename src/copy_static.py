import os
import shutil

def clear_dir(directory):
    """Clears the entire directory of all files and sub directories"""
    shutil.rmtree(directory)
    os.mkdir(directory)

def copy_dir(directory, destination):
    """Copies all files and subdirectories to specified destination"""
    if os.path.exists(directory):
        dir_contents = os.listdir(directory)
        for item in dir_contents:
            source_path = os.path.join(directory, item)
            destination_path = os.path.join(destination, item)
            if os.path.isfile(source_path):
                print(f"Copying from : {source_path} to {destination_path}")
                print("-----------------------------------------------")
                shutil.copy(source_path, destination_path)
            else:
                print(f"Creating directory: {destination_path}")
                print("-----------------------------------------------")
                os.mkdir(destination_path)
                copy_dir(source_path, destination_path)
    else:
        raise ValueError(f"Directory: {directory} does not exist")