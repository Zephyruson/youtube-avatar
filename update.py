import requests
import re

CHANNEL_URL = "https://www.youtube.com/@JamieTX"

headers = {
    "User-Agent": "Mozilla/5.0"
}

html = requests.get(CHANNEL_URL, headers=headers).text

match = re.search(r'"avatar":\{"thumbnails":\[\{"url":"(https:[^"]+)"', html)

if not match:
    raise Exception("Avatar URL not found")

avatar_url = match.group(1)

img = requests.get(avatar_url, headers=headers).content

with open("avatar.png", "wb") as f:
    f.write(img)
