Сервис на Flask для предсказания атрибутов по входной фотографии
Создаем виртуальную машину на яндекс облаке (с предустановленным докер контейнером)

```
git clone https://github.com/konoha44/hair_attributes
cd hair_attributes
sudo apt install screen
screen -S hair_service
docker-compose up --build
```
*Дожидаемся пока не выведется запись "модели загружены в память "*

удерживая кнопку ctrl последовательно нажимаем на A затем на D

# Для запросов из консоли
```usage: client.py [-h] [--image_name IMAGE_NAME] host

Predict image with hair attributes

positional arguments:
  host                  public ip

optional arguments:
  -h, --help            show this help message and exit
  --image_name IMAGE_NAME
                        name of image (default: picture.jpg)
```
```
python client.py <public_host>
or
python client.py <public_host> --image_name=picture.jpg
```

# Через форму в браузере (вебсайт)
http://<public_host>:8000/upload