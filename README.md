### Парсер Scrapy

## Программа позволяющая парсить python.org и получать информацию ввиде статистики правил PEP.

# Список технологий:
> [Scrapy](https://scrapy.org)

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Получить статитистику правил PEP:
```
* Находясь в директории scrapy_parser_pep/

scrapy crawl pep
```