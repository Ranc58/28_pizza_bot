# Telegram Bot for Pizzeria

Bot for telegram with pizza catalog. 

# How to install
1. Recomended use venv or virtualenv for better isolation.\
   Venv setup example: \
   `python3 -m venv myenv`\
   `source myenv/bin/activate`
2. Install requirements: \
   `pip3 install -r requirements.txt` (alternatively try add `sudo` before command)
3. Go to [@botfather](https://telegram.me/botfather) and create Your bot.\
   More info about this: [Instruction for create bot](https://core.telegram.org/bots#3-how-do-i-create-a-bot).\
   Then you need copy bot-token to `PIZZA_BOT_TOKEN` in `env_conf` file.\
   If you want, you can change some params like admin login/password, database pathfile, etc in this file too.
4. Add new environment parameters to Your system: `source env_conf`.

# How to Use
1. Create database: `python3 db_operations -c`.
2. Update database from json: `python3 db_operations -u PATH_TO_JSON_FILE`.\
    JSON file must have structere like this:
    ```
    [
    {
        "title": "Маргарита",
        "description": "соус,сыр Моцарелла",
        "choices": [
            {
                "title": "30 см (450гр)",
                "price": "360"
            },
            {
                "title": "40 см (750гр)",
                "price": "460"
            }
        ]
    }
    ]
    ```
 3. Run `python3 bot.py`.
 4. Open chat with Your telegram bot and type `/start`. Bot should respond with a greetings.
 5. Type `/menu` for getting pizza catalog.
 6. To edit menu run `python3 admin_page.py`
 7. Go to `127.0.0.1:5000/admin/` and login.
 8. You can add/del/edit pizzas and some info like size and price on this web-interface.


# How to install and use with Docker
1. Open `Dockerfile` and change `ENV` for your needs(don't forget to specify the bot-token!).
2. If you want make first pizza catalog load from JSON - put json file in app folder.
3. `docker-compose build`
4. `docker-compose run web python3 /src/db_operations.py -c` for create SQlite database.
5. `docker-compose run web python3 /src/db_operations.py -u JSON_FILE` if you want fist load from JSON.
6. `docker-compose up`
7. Open chat with Your telegram bot and type `/start`. Bot should respond with a greetings.
8. Type `/menu` for getting pizza catalog.
9. Go to `<host_from_ENV>:5000/admin/` and login.
10. You can add/del/edit pizzas and some info like size and price on this web-interface.


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
