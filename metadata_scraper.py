import pandas as pd  # pandas makes very annoying messages
import tqdm
import requests
from bs4 import BeautifulSoup
import warnings, lxml
warnings.simplefilter(action='ignore', category=FutureWarning)

# create empty dataframe
df = pd.DataFrame(columns=['url', 'alt_text'])

# loop through pages and extract image data

for page_num in tqdm.tqdm(range(1, 779)):
    url = f'https://shot.cafe/results.php?page={page_num}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    images = soup.find_all('img')
    for img in images:
        img_url = img['src']
        full_url = f'https://shot.cafe/{img_url}'
        alt_text = img.get('alt', '')
        df = df.append({'url': full_url, 'alt_text': alt_text},
                       ignore_index=True)

# export dataframe to parquet file
df.to_csv('shot_cafe_images.csv')
df.to_parquet('shot_cafe_images.parquet')

# print number of urls extracted
print(f'{len(df)} urls were extracted.')
