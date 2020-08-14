import requests
import argparse
from pprint import pprint

parser = argparse.ArgumentParser(description='Predict image with hair attributes')
parser.add_argument('host', type=str, help='public ip')
parser.add_argument(
    '--image_name',
    type=str,
    default='picture.jpg',
    help='name of image (default: picture.jpg)'
)
params = parser.parse_args()

with open(params.image_name,'rb') as file:
    img = file.read()

files = {'image': img}
r = requests.post(f"http://{params.host.strip()}:8000/predict_atrs", files=files).json()

pprint(r)