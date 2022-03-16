# [where_to_go][docs]
# Обзор
Проект Яндекс.Афиша позволяет разместить локации (например, локации вашего города) на карте с их описанием и фотографиями. Локации оторажаются на карте, по клику на локации открывается описание и картинки этой локации.</br>
<b>Это учебный проект.</b>

# Требования
* Python (3.8, 3.9, 3.10)
* Django (3.2, 4.0)

### Зависимые модули
* Pillow==8.4
* python-slugify==6.1
* django-admin-sortable2==1.0
* django-tinymce==3.4

# Установка
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

***
Тестовые данные взяты с сайта [KudaGo](https://kudago.com).