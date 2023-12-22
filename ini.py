import json
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from telebot import TeleBot
from sqlalchemy_utils import database_exists, create_database


def get_config():
    with open(Path(Path.cwd(), 'config.json'), 'r') as file:
        config = json.load(file)
    return config


def get_engine_string():
    config = get_config()
    return f"postgresql+psycopg2://{config['mysql']['user']}:{config['mysql']['password']}@{config['mysql']['host']}:{config['mysql']['port']}/" \
           f"{config['mysql']['database']}"


def generate_engine():
    connection = create_engine(get_engine_string())
    return connection


def send_log(log_text):
    config = get_config()
    bot = TeleBot(config['telegram_bot_logs'])
    for admin_id in config['admins_ids']:
        try:
            bot.send_message(admin_id, str(log_text))
        except Exception as ex:
            write_log_to_file(f"CANNOT SEND LOG TO ADMIN {admin_id} {ex}")


def write_log_to_file(log_text):
    with open("logs.txt", 'a') as file:
        file.write(str(log_text) + "\n")


base = declarative_base()

if __name__ == "__main__":
    engine = generate_engine()
    print(engine)
    if not database_exists(engine.url):
        create_database(engine.url)
    from database.models import *
    base.metadata.create_all(engine)
