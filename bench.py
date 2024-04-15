# Class requirement for Research Project of The Senior High School Department, School of Saint Anthony, Quezon City under the guidance of our research adviser Rey-Ann Rachelle S.P. Palasigue for A.Y. 2023-2024.

# Information about testing environment:
# OS: Windows 11 Pro 23H2 
# Processor: AMD Ryzen 5 7600 6-Core Processor 3.80 GHz 6 cores
# Memory: 32GiB DDR5 @ 6000MHz
# Python 3.12.3
# tesseract v5.3.3.20231005
#  leptonica-1.83.1
#   libgif 5.2.1 : libjpeg 8d (libjpeg-turbo 2.1.4) : libpng 1.6.40 : libtiff 4.6.0 : zlib 1.2.13 : libwebp 1.3.2 : libopenjp2 2.5.0
#  Found AVX512BW
#  Found AVX512F
#  Found AVX512VNNI
#  Found AVX2
#  Found AVX
#  Found FMA
#  Found SSE4.1
#  Found libarchive 3.7.2 zlib/1.3 liblzma/5.4.4 bz2lib/1.0.8 liblz4/1.9.4 libzstd/1.5.5
#  Found libcurl/8.3.0 Schannel zlib/1.3 brotli/1.1.0 zstd/1.5.5 libidn2/2.3.4 libpsl/0.21.2 (+libidn2/2.3.3) libssh2/1.11.0

import time
import timeit
import os
import pytesseract

start_time = time.time()
tess_exe = r"C:\Users\xmdb\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
image_folder = os.path.join(os.path.dirname(__file__), "benchmark")  # Folder containing the images
os.environ['TESSDATA_PREFIX'] = r"benchmark"

# List of image filenames
image_filenames = [
    "282210e5d753aeef.jpg",
    "c508532ae14086e6.jpg",
    "ddc348ba882ec11b.jpg",
    "e0f97cc7c2e71a1b.jpg",
    "e547672600381540.jpg",
    "p02-105.png",
    "p02-131.png",
    "p03-040.png",
    "p03-069.png",
    "r06-103.png"
]

code_to_test = """
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"{}"
pytesseract.pytesseract.image_to_string(r"{}", lang='eng')
"""

for idx, image_filename in enumerate(image_filenames, start=1):
    full_image_path = os.path.join(image_folder, image_filename)
    elapsed_time = timeit.timeit(code_to_test.format(tess_exe, full_image_path), number=1)
    ocr_result = code_to_test.format(tess_exe, full_image_path)
    print("Image {}: Elapsed Time: {:.4f} seconds".format(idx, elapsed_time))
    print("Image {}: Accuracy")