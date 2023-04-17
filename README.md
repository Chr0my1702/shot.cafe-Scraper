
<h1 align="center">
  shot.cafe Scraper
  <br>
  
</h1>

<img src="https://user-images.githubusercontent.com/49107678/232515035-5a8d3ddd-ca83-454a-96da-42ec1a4a4f7a.png" width="400" height="100" />

# Scripts:
### Metadata_scraper.py
The Metadata Scraper is a script that scrapes metadata from a website and stores the extracted data in a CSV file and a Parquet file.
### Image_Downloader.py
Downloads images from a CSV file containing image URLs. The script creates a set of folders in a specified output directory, with each folder containing up to 21 images. The script uses threading to download images in parallel, allowing for faster downloads.
It also checks whether there are already pictures, if so, it won't request it again.
### Verify.py
The verify.py script checks that there are exactly 21 images in each folder under the directory Full. If there are any folders that do not have 21 images, the script prints the name of the folder and suggests to re-run the downloadimages.py script.
The script also verifies that the total number of images in the Full directory matches the number of images on the website. If there is a mismatch, the script prints a message suggesting to re-run the downloadimages.py script.

# How to run:

1) To run the metadata scraper, you can simply execute the Metadata_scraper.py script, which will scrape the metadata from the specified website and store it in both CSV and Parquet file formats.

2) To run the image downloader, you will need to create a CSV file containing image URLs and provide an output directory where the downloaded images will be saved. You can then execute the Image_Downloader.py script, which will create folders in the specified output directory and download up to 21 images per folder using threading for faster downloads. The script will also check whether the images have already been downloaded and skip them if they have.

3) To verify that the images were downloaded correctly, you can execute the Verify.py script, which will check that each folder under the Full directory contains exactly 21 images and that the total number of images in the Full directory matches the number of images on the website. If there are any issues, the script will suggest to re-run the downloadimages.py script.
