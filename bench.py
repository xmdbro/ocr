# Class requirement for Research Project of The Senior High School Department, School of Saint Anthony, Quezon City under the guidance of our research adviser Rey-Ann Rachelle S.P. Palasigue for A.Y. 2023-2024.

# Information about testing environment:
# OS: Windows 11 Pro 23H2 
# Processor: AMD Ryzen 5 7600 6-Core Processor 3.80 GHz 6 cores
# Memory: 32GiB DDR5 @ 6000MHz
# Python 3.12.3

import time
import timeit
import os
import pytesseract

start_time = time.time()
tess_exe = r"msvc.v5.openmp\tesseract.exe"
image_folder = r"images"  # Folder containing the images
os.environ['TESSDATA_PREFIX'] = r"tessdata_best\tessdata"

# List of image filenames
image_filenames = [
    "image1.jpg",
    "image2.jpg",
    # Add more image filenames as needed
]

code_to_test = """
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"{}"
pytesseract.pytesseract.image_to_string(r"{}", lang='eng')
"""

for idx, image_filename in enumerate(image_filenames, start=1):
    full_image_path = os.path.join(image_folder, image_filename)
    elapsed_time = timeit.timeit(code_to_test.format(tess_exe, full_image_path), number=1)
    print("Image {}: Elapsed Time: {:.4f} seconds".format(idx, elapsed_time))