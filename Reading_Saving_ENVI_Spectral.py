# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 15:05:19 2023

@author: Morteza
"""

import spectral
import numpy as np
import os

# Specify the folder path containing the ENVI files
input_folder = "C:/Users/Morteza/OneDrive/Desktop/PhD/dataN"

# Specify the base name of the ENVI header file (without extension)
base_name = "Seurat_BEFORE"

# Construct the full paths for the header and data files
header_file = f"{input_folder}/{base_name}.hdr"
data_file = f"{input_folder}/{base_name}.dat"  # Or use the correct extension based on your data format

# Read the hyperspectral image using spectral
spectral_image = spectral.open_image(header_file)

# Access the data as a NumPy array
hyperspectral_data = spectral_image.load()

# Print the shape of the data array
print("Shape of hyperspectral data:", hyperspectral_data.shape)

# Specify the folder path for saving the ENVI files
output_folder = "C:/Users/Morteza/OneDrive/Desktop/PhD/dataN/Output"

# Specify the base name for the ENVI header file (without extension)
base_name = "output"

# Create a SpectralImage object
header_file = os.path.join(output_folder, base_name + ".hdr")
spectral.envi.save_image(header_file, hyperspectral_data, interleave='bil', dtype=np.float32)