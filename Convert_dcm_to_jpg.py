import os
import pydicom
from PIL import Image
import numpy as np
from tkinter import Tk
from tkinter import filedialog


def convert_dcm_to_jpeg(dcm_folder,
                        output_folder):
    """
    Function for converting files from .dcm to .jpeg format
    :param dcm_folder: takes the path to the folder with the dcm format files
    :param output_folder: accepts the folder path for output jpeg files
    :return:jpeg format file
    """
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all DICOM files in the input folder
    dcm_files = [f for f in os.listdir(dcm_folder) if f.endswith('.dcm')]

    # Convert each DICOM file to JPEG
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


def choose_folder(title):
    """
    :param title: the function opens a window and asks to select a folder
    :return:the path to the folder is selected through the window
    """
    # Open a folder selection dialog
    root = Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title=title)
    root.destroy()
    return folder_path


if __name__ == "__main__":
    # The first parameter is the path to the input files
    # And the second parameter is the path to the output files
    convert_dcm_to_jpeg(dcm_folder=choose_folder('Сhoose files folder'),
                        output_folder=choose_folder('Сhoose output folder'))

