# Космический Телеграм

Скачивает картинки космоса от NASA и SpaceX через API, и создает бота который выкладывает картинки в телеграм с определенной частотой

### Как установить
- Установить Python3

- Выполнить команду ```pip install -r requirements.txt```

- Получить API токены NASA и Telegram:
 - Токен NASA можно получить по ссылке ```https://api.nasa.gov/```

 - Токен Telegram можно получить у телеграм бота ```@BotFather```

- Создать .env файл с следующим содержанием:

  NASA_API_TOKEN=<ВАШ NASA токен>

  TG_API_TOKEN=<ВАШ Tg токен>

  PUBLISHING_DELAY=<Задержка публикации в секундах(если этот пункт не указывать то задержка будет 86400 секунд = 1 день)>


- Запустить бота командой ```python bot.py```, подождать пока скрипт скачает картинки, после этого он начнет присылать их в тг.  



Код написан в качестве тренировки работы с API
