import os
import shutil

def rename_images(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".png"):
                base_name, extension = os.path.splitext(file)
                
                # Extract number and count
                number, count = base_name.split("_")[:2]

                # Add leading zeros to count
                count_with_zeros = count.zfill(4)

                # Create the new filename
                new_filename = f"{number}_{count_with_zeros}{extension}"

                # Construct the full paths
                old_path = os.path.join(root, file)
                new_path = os.path.join(root, new_filename)

                # Rename the file
                shutil.move(old_path, new_path)
                print(f"Renamed: {old_path} -> {new_path}")

if __name__ == "__main__":
    folder_path = "/home/daniel/software/visualInspectionPopcorn/data/raw_data"
    rename_images(folder_path)
