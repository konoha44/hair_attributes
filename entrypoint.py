import os
from time import sleep

def take_amount():
    return len([i for i in os.listdir() if '.onnx' in i])
def waiting():
    while take_amount() < 7:
        sleep(15)
    sleep(5)

if take_amount!=7:
    waiting()
    
print('\n\n все модели загружены из яндекса, можем запускать фласк\n\n')
