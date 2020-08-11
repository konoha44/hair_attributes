import requests

with open('picture.jpg','rb') as file:
    img = file.read()

files = {'image': img}
r = requests.post("http://84.201.174.145:5001/predict_atrs", files=files)
print(r.text)