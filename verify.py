# check there are infact 21 images in each folder under FULL, if not, print the problemmed folder
import re
import bs4
import requests
import os
import glob

# get how many files are in each folder
folders_in_full = int(len(os.listdir('Full')))

for folder in glob.glob('Full/Folder*'):
    if len(os.listdir(folder)) != 21:
        if folder == f'Full\Folder{folders_in_full}':
            print(
                "Last folder doesn't have 21 images, but it's the last folder so it's ok.")
        else:
            print(folder)
            print("Re-run downloadimages.py")


request_database = requests.get(
    "https://shot.cafe/results.php?page=999999999999999999999999999999")
soup_database = bs4.BeautifulSoup(request_database.text, 'lxml')
returned = (soup_database.text)
returned = returned.replace("\n", "").replace(",", "")
returned_num = re.findall(r'\d+', returned)
dir_list = os.listdir("Full")


count = sum([len(files) for root, dirs, files in os.walk("Full")])

if count == int(returned_num[0]):
    print("Number of images in Full folder matches number of images on website")
else:
    print("Number of images in Full folder does not match number of images on website")
    print("Re-run downloadimages.py")
