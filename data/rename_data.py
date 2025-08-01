import os
import shutil

def process_labels(folder_path, folders, save_path, add="/obj_train_data/", extension=".txt"):
    for folder in folders:
        full_path = os.path.join(folder_path, folder + add)
        print(full_path)
        for label in os.listdir(full_path):
            label_path = os.path.join(full_path, label)
            if label_path.endswith(extension):
                base_name, extension = os.path.splitext(label)
                new_filename = os.path.join(save_path, f"{folder}_{os.path.basename(base_name)}{extension}")
                shutil.copy(label_path, new_filename)

def rename_data(folder):
    # folder contains imgs/ and labels/ with the same filenames.
    # Rename labels starting at 0 and rename imgs to match the labels.
    # Move renamed data into a new folder.

    new_folder = "data/renamed_data"
    os.makedirs(new_folder, exist_ok=True)

    label_counter = 0  # Counter to rename labels

    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".txt"):
                base_name, extension = os.path.splitext(file)
                new_label_filename = f"labels/{label_counter}.txt"
                new_img_filename = f"imgs/{label_counter}.png"  # Change the extension based on your image format
                
                old_label_path = os.path.join(root, file)
                new_label_path = os.path.join(new_folder, new_label_filename)
                
                # Update the img path based on your image folder structure
                old_img_path = os.path.join(root.replace("labels", "imgs"), f"{base_name}.png")
                new_img_path = os.path.join(new_folder, new_img_filename)
                
                # Copy and rename label file
                shutil.copy(old_label_path, new_label_path)
                print(f"Renamed Label: {old_label_path} -> {new_label_path}")

                # Copy and rename image file
                shutil.copy(old_img_path, new_img_path)
                print(f"Renamed Image: {old_img_path} -> {new_img_path}")

                label_counter += 1

if __name__ == "__main__":
    # FOR IMAGES
    folder_path = "/home/daniel/software/visualInspectionPopcorn/data/raw_data/webcam/images"
    folders = ["good", "bad", "acceptable"]
    save_path = "/home/daniel/software/visualInspectionPopcorn/data/annotated_data/webcam/images"

    process_labels(folder_path, folders, save_path, add="", extension=".png")


    # FOR LABELS
    folder_path = "/home/daniel/software/visualInspectionPopcorn/data/raw_data/webcam/labels"
    folders = ["good", "bad", "acceptable"]
    save_path = "/home/daniel/software/visualInspectionPopcorn/data/annotated_data/webcam/labels"

    process_labels(folder_path, folders, save_path)



    # THE FOLLOWING WAS USED TO RENAME ORIGINAL IMAGES
#     import os
# import shutil

# def rename_images(folder_path):
#     for root, dirs, files in os.walk(folder_path):
#         for file in files:
#             if file.endswith(".png"):
#                 base_name, extension = os.path.splitext(file)
                
#                 # Extract number and count
#                 number, count = base_name.split("_")[:2]

#                 # Add leading zeros to count
#                 count_with_zeros = count.zfill(4)

#                 # Create the new filename
#                 new_filename = f"{number}_{count_with_zeros}{extension}"

#                 # Construct the full paths
#                 old_path = os.path.join(root, file)
#                 new_path = os.path.join(root, new_filename)

#                 # Rename the file
#                 shutil.copy(old_path, new_path)
#                 print(f"Renamed: {old_path} -> {new_path}")

# if __name__ == "__main__":
#     folder_path = "/home/daniel/software/visualInspectionPopcorn/data/raw_data"
#     rename_images(folder_path)
