import os
from time import sleep

while len([i for i in os.listdir() if '.onnx' in i])<7:
    sleep(15)
    pass
print('\n\n все модели загружены из яндекса, можем запускать фласк\n\n')
