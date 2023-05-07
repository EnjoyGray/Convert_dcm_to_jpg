import os
import pydicom
from PIL import Image
import numpy as np

def convert_dcm_to_jpeg(dcm_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    dcm_files = [f for f in os.listdir(dcm_folder) if f.endswith('.dcm')]

    for dcm_file in dcm_files:
        dcm_path = os.path.join(dcm_folder, dcm_file)
        dcm = pydicom.dcmread(dcm_path)
        image = dcm.pixel_array

        # Normalize pixel values to an 8-bit range
        image = (image / np.max(image) * 255).astype(np.uint8)

        output_path = os.path.join(output_folder, f"{os.path.splitext(dcm_file)[0]}.jpeg")

        # Save the image as JPEG
        image = Image.fromarray(image)
        image.save(output_path, "JPEG")

        print(f"File successfully converted to JPEG: {output_path}")


# Example usage of the conversion function
dcm_folder_path = "path_to_dcm_folder"
output_folder_path = "/jpeg_files"

convert_dcm_to_jpeg(dcm_folder_path, output_folder_path)
