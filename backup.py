import os
import sys
import shutil
from datetime import datetime

def backup_files(source_dir, dest_dir):
    if not os.path.isdir(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return
    if not os.path.isdir(dest_dir):
        print(f"Error: Destination directory '{dest_dir}' does not exist.")
        return

    for filename in os.listdir(source_dir):
        # Only back up files, not directories
        src_file = os.path.join(source_dir, filename)
        #check if it's a file
        if os.path.isfile(src_file):
            # Prepare destination file path
            dest_file = os.path.join(dest_dir, filename)
            # If file exists in destination, append timestamp to filename
            if os.path.exists(dest_file):
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                name, ext = os.path.splitext(filename)
                new_filename = f"{name}_{timestamp}{ext}"
                dest_file = os.path.join(dest_dir, new_filename)
            try:
                shutil.copy2(src_file, dest_file)
                print(f"Copied: {src_file} -> {dest_file}")
            except Exception as e:
                print(f"Error copying {src_file}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py /path/to/source /path/to/destination")
    else:
        backup_files(sys.argv[1], sys.argv[2])