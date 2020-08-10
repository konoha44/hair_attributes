import requests

with open('picture.jpg','rb') as file:
    img = file.read()

files = {'image': img}
r = requests.post("http://0.0.0.0:5001/predict_atr", files=files)
print(r.text)