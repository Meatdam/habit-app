import requests
from base.settings import TELEGRAM_TOKEN, TELEGRAM_URL


def send_telegram_message(chat_id, message):
    """
    Отправка сообщения в телеграм чат
    """
    params = {
        'text': message,
        'chat_id': chat_id,
    }
    requests.get(f'{TELEGRAM_URL}{TELEGRAM_TOKEN}/sendMessage', params=params)
