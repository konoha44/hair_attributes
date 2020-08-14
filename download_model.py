import boto3
import time
import os

def download_model(bucket):
    session = boto3.session.Session()
    s3 = session.client(
        service_name='s3',
        endpoint_url='https://storage.yandexcloud.net'
    )
    model_names = []
    for item in s3.list_objects(Bucket=bucket)['Contents']:
        model_names.append(item['Key'])

    for model in model_names:
        get_object_response = s3.get_object(Bucket=bucket,Key=model)
        with open(model, 'wb') as model_file:
            model_file.write(get_object_response['Body'].read())

if len([i for i in os.listdir() if '.onnx' in i])<7:
    print('Началась загрузка моделей')
    start = time.time()
    download_model('hair-atrs-models')
    end = time.time()-start
    print('Загрузилось за  ', end)