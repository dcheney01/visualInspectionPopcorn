import os
from pathlib import Path
import shutil

def process_images_in_folder(input_folder, output_folder):
    # Iterate through each folder in the input folder
    for folder_name in os.listdir(input_folder):
        folder_path = os.path.join(input_folder, folder_name)

        # Check if the item in the folder is a directory
        if os.path.isdir(folder_path):
            print(f"Processing images in folder: {folder_name}")

            # Create the output folder for the current subfolder
            output_subfolder = os.path.join(output_folder, folder_name)
            os.makedirs(output_subfolder, exist_ok=True)

            # Flag to alternate between keeping and skipping images
            keep_image = True

            # Iterate through each image in the folder
            for image_name in os.listdir(folder_path):
                image_path = os.path.join(folder_path, image_name)

                # Check if the item is a file and has a common image extension
                if os.path.isfile(image_path) and image_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                    # Save every other image
                    if keep_image:
                        output_path = os.path.join(output_subfolder, image_name)
                        shutil.copyfile(image_path, output_path)
                        print(f"Image saved: {output_path}")

                    # Toggle the flag for the next iteration
                    keep_image = not keep_image

if __name__ == "__main__":
    # Set your input and output folders
    input_folder_path = '/home/daniel/catkin_ws/src/josh_vision/data/raw_data'
    output_folder_path = '/home/daniel/catkin_ws/src/josh_vision/data/filtered_data'

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder_path, exist_ok=True)

    # Process images in the input folder
    process_images_in_folder(input_folder_path, output_folder_path)