import boto3
from tqdm import tqdm


def download_model(bucket):
    session = boto3.session.Session()
    s3 = session.client(
        service_name='s3',
        endpoint_url='https://storage.yandexcloud.net'
    )
    model_names = []
    for item in s3.list_objects(Bucket=bucket)['Contents']:
        model_names.append(item['Key'])
    for model in tqdm(model_names[:2], desc='Download Models'):
        get_object_response = s3.get_object(Bucket=bucket,Key=model)
        with open(model, 'wb') as model_file:
            model_file.write(get_object_response['Body'].read())

start = time.time()
download_model('hair-atrs-models')
end = time.time()-start
print('модели скачались ',end)