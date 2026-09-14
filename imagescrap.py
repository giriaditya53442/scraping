import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import quote

savedir = "images"

if not os.path.exists(savedir):
    os.makedirs(savedir)

query = "cars"

url = f"https://www.bing.com/images/search?q={quote(query)}"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

image_tags = soup.find_all("img")

print("Images found:", len(image_tags))

count = 0

for i, image_tag in enumerate(image_tags):

    image_url = image_tag.get("src")

    if not image_url:
        image_url = image_tag.get("data-src")

    if image_url and image_url.startswith("http"):

        try:
            image_data = requests.get(
                image_url,
                headers=headers,
                timeout=10
            ).content

            filename = os.path.join(
                savedir,
                f"{query}_{count}.jpg"
            )

            with open(filename, "wb") as f:
                f.write(image_data)

            print(f"Downloaded: {filename}")

            count += 1

        except Exception as e:
            print("Error:", e)

print(f"\n{count} images downloaded.")