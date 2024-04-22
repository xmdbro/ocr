# Image 1: Average Elapsed Time: 0.2499 seconds
# Image 2: Average Elapsed Time: 0.1185 seconds
# Image 3: Average Elapsed Time: 0.1079 seconds
# Image 4: Average Elapsed Time: 0.1139 seconds
# Image 5: Average Elapsed Time: 0.1093 seconds
# Image 6: Average Elapsed Time: 1.0486 seconds
# Image 7: Average Elapsed Time: 0.9303 seconds
# Image 8: Average Elapsed Time: 0.8551 seconds
# Image 9: Average Elapsed Time: 0.9014 seconds
# Image 10: Average Elapsed Time: 0.9835 seconds

import re
from collections import defaultdict
import statistics

# Path to your text file
file_path = r'X:\gaming gamer\repos\ocr\benchmark\100runs.txt'

# Dictionary to store times for each image
image_times = defaultdict(list)

# Regex to extract image number and elapsed time
pattern = r"Image (\d+): Elapsed Time: (\d+\.\d+) seconds"

# Open the text file and read line-by-line
with open(file_path, 'r') as file:
    for line in file:
        match = re.match(pattern, line)
        if match:
            image_number = int(match.group(1))
            elapsed_time = float(match.group(2))
            image_times[image_number].append(elapsed_time)

# Calculate the average for each image
image_averages = {img_num: statistics.mean(times) for img_num, times in image_times.items()}

# Output the average elapsed time for each image
for img_num, avg_time in image_averages.items():
    print(f"Image {img_num}: Average Elapsed Time: {avg_time:.4f} seconds")