# Отправка фото в телеграмм 

Этот проект создан для отправки фото в телеграмме через бота. Так же есть возможность скачиавть фото космоса через API SpaceX и NASA

### Как установить

Для работы проекта нужно получить токен telegram(@BotFather).
Так же вы можете скачивать фото с сайта NASA, в этом случае вам так же нужен [токен](https://api.nasa.gov/).
Токены можно хранить в файле .env.

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Рекомендуется использовать [виртуальную среду](https://timeweb.cloud/tutorials/python/kak-sozdat-virtualnoe-okruzhenie) для изоляции проекта

в проекте есть несколько файлов

space_bot.py - загружает фото, если не может загрузить, то ничего не делает. Может загрузить конкретное фото (python space_bot.py 'полное имя изображения')

uploading_photos_tg.py - перемешивает случайным образом фотографии в директории(нужно создать заранее или же запустить файлы для скачаивания изображений) и передает для загрузки, после того как все фотографии были загружены цикл повторяется. Так же имеется параметр таймера загрузки, по умолчанию стоит 4 часа, можно указать свой (python uploading_photos_tg.py 'время между публикацией в секундах')

apod_images.py - загружает фотографию звездного неба от NASA, есть параметр даты. По умолчанию будет загружать сегодняшнее фото, ели оно есть. Можно указать от конкретного числа в формате(python apod_images.py 'YYYY-MM-DD')

epic_photo.py - загружает последнии фотографии земли от NASA.

fetch_spacex_images.py - загружает фото запуска ракет SpaceX(где они были сделаны), есть параметр id. Можно выбрать конкретный запуск(python fetch_spacex_images.py 'id')

main.py - содержит функции для загрузки и определения разрешения фото.

### Цель проекта

Автоматизировать загрузку фото в телеграм канал и упрастить скачивание изображений космоса.

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).