import requests

CHANNEL_URL = "https://www.youtube.com/@JamieTX"

html = requests.get(CHANNEL_URL).text

start = html.find('"avatar":{"thumbnails":[{"url":"') + 35
end = html.find('"', start)
avatar_url = html[start:end]

img = requests.get(avatar_url).content
with open("avatar.png", "wb") as f:
    f.write(img)
