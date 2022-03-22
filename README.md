# Куда пойти — Москва глазами Артёма
## Обзор
Проект Яндекс.Афиша позволяет разместить локации (например, локации вашего города) на карте с их описанием и фотографиями. Локации оторажаются на карте, по клику на локации открывается описание и картинки этой локации.</br>
[Демо сайта](https://rs0x069.pythonanywhere.com/) </br>
[Панель упарвления сайтом](https://rs0x069.pythonanywhere.com/admin/) (имя пользователя `admin`, пароль `admin`) </br>

## Требования
* Python (3.8, 3.9, 3.10)
* Django (3.2, 4.0)

### Зависимые модули
* Pillow==8.4
* python-slugify==6.1
* django-admin-sortable2==1.0
* django-tinymce==3.4

## Установка
* Установить Python</br>
* Склонировать проект
```commandline
git clone https://github.com/rs0x069/where_to_go.git
```
* Перейти в папку `where_to_go`
* (Опционально) Создать виртуальное окружение</br>
```commandline
# Linux
sudo apt-get install python3-venv
python3 -m venv .venv
source .venv/bin/activate

# macOS
python3 -m venv .venv
source .venv/bin/activate

# Windows
py -3 -m venv .venv
.venv\scripts\activate
```
* Обновить pip
```commandline
python -m pip install --upgrade pip
```
* Установить пакеты
```commandline
pip install -r requirements.txt
```
* Подготовить базу данных
```commandline
python manage.py migrate
```
* Создать пользователя для панели управления
```commandline
python manage.py createsuperuser
```
* Запустить проект
```commandline
python manage.py runserver
```
* Сайт доступен по адресу <http://127.0.0.1:8000/>
* Панель управления доступна по адресу <http://127.0.0.1:8000/admin/>
* Сайт необходимо заполнить тестовыми данными по адресу <http://127.0.0.1:8000/admin/places/place/>

## Настройка проекта
### Переменные окружения
* DJANGO_SECRET_KEY - переменная SECRET_KEY в settings.py
* DJANGO_DEBUG - переменная DEBUG в settings.py
* DJANGO_ALLOWED_HOSTS - переменная ALLOWED_HOSTS в settings.py, несколько хостов указываются через запятую
### Загрузка данными
```commandline
python manage.py load_place http://адрес/файла.json
```

## Образец json-файла
```json
{
    "title": "Горбовская ГЭС",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/151dc8d2833276130c3dff6dd1e43aac.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1ba047f0e1e885f4aff5ee18d54e87bc.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/4af219237df1691ffe0d4ba41a2f5b41.jpg"
    ],
    "description_short": "В 80 километрах от Москвы стоит Горбовская ГЭС — заброшенная ...",
    "description_long": "<p>Горбовская ГЭС была сооружена в 1953 году. Она была достаточно мощной, на её борту установили два 250-киловатных генератора, а также ...</p>",
    "coordinates": {
        "lng": "36.26108899999998",
        "lat": "55.65323799999996"
    }
}
```

***
Тестовые данные взяты с сайта [KudaGo](https://kudago.com). </br>
Фронтенд взят у [devman](https://github.com/devmanorg/where-to-go-frontend)

***
Учебный проект для курсов web-разработчиков [dvmn](https://dvmn.org).  
