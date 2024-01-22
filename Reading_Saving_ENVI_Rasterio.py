# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 15:43:19 2023

@author: Morteza
"""

import rasterio
import numpy as np
import spectral
import os

# Specify the path to the ENVI data file and the file with .hdr
file = 'C:/Users/Morteza/OneDrive/Desktop/PhD/dataN/Seurat_BEFORE'
header_file = 'C:/Users/Morteza/OneDrive/Desktop/PhD/dataN/Seurat_BEFORE.hdr'

# Open the ENVI image using rasterio
with rasterio.open(file) as src:
    # Read the hyperspectral data into a NumPy array
    hyperspectral_data = src.read()

    # Display information about the hyperspectral data
    print('Shape of hyperspectral data:', hyperspectral_data.shape)
    print('Number of bands:', src.count)
    
#Here we can see the wavelengths of the data
img = spectral.open_image(header_file)


output_folder = "C:/Users/Morteza/OneDrive/Desktop/PhD/dataN/OutputR"

# Ensure the output folder exists; create it if it doesn't
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Specify the file path for the output raster
output_path = os.path.join(output_folder, "output.tif")

# Specify the dimensions of the raster
bands, rows, cols = hyperspectral_data.shape

# Specify the metadata for the output raster
metadata = {
    'driver': 'GTiff',
    'count': bands,
    'dtype': 'float32',  # Change the data type if needed
    'width': cols,
    'height': rows,
    # 'crs': 'EPSG:4326',  # Uncomment if you have CRS information
}

# Create the output raster file
with rasterio.open(output_path, 'w', **metadata) as dst:
    # Write hyperspectral data to the raster bands
    for i in range(bands):
        dst.write(hyperspectral_data[i, :, :], i + 1)