import os
import threading
import pandas as pd
import requests
from tqdm import tqdm

# define function for downloading images in a separate thread


def download_images(images, output_dir):
    for url in tqdm(images, desc=output_dir):
        filename = os.path.join(output_dir, os.path.basename(url))
        if os.path.exists(filename):
            continue
        response = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(response.content)


# read in CSV file with image URLs
df = pd.read_csv('shot_cafe_images.csv')

# create output directory
output_dir = 'Full'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# loop through URLs and download images
num_images = len(df)
num_folders = (num_images // 21) + 1
threads = []
for folder_num in range(num_folders):
    folder_name = f'Folder{folder_num + 1}'
    folder_path = os.path.join(output_dir, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    start_idx = folder_num * 21
    end_idx = min((folder_num + 1) * 21, num_images)
    images = df.iloc[start_idx:end_idx]['url'].tolist()
    thread = threading.Thread(target=download_images,
                              args=(images, folder_path))
    thread.start()
    threads.append(thread)

# wait for all threads to finish
for thread in threads:
    thread.join()
