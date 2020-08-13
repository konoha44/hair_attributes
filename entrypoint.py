import os
from time import sleep

while len([i for i in os.listdir() if '.onnx' in i])==7:
    sleep(1)
    print('Еще не загрузилось')
    pass
print('\n\n загрузилось\n\n')
