from celery import shared_task
from habits.models import Habits

import datetime
from habits.services import send_telegram_message


@shared_task
def send_habit():
    """
    Задача для отправки напоминаний о выполнении полезных привычек в телеграм чатах
    """
    habits = Habits.objects.all()
    current_date = datetime.datetime.now()
    count = 0
    if Habits.objects.filter(is_daily=True) and count <= 7:
        for habit in habits:
            if f"{current_date.time().hour}:{current_date.time().minute}" == f"{habit.time.hour}:{habit.time.minute}":
                count += 1
                tg_chat = habit.owner.tg_chat_id
                if habit.prize is None:
                    message = (f"Не забудь {habit.action} в {habit.time}' место: '{habit.place}'. И получи приз: "
                               f"'Твое хорошее настроение'")
                else:
                    message = (f"Не забудь {habit.action} в {habit.time}' место: '{habit.place}'. И получи приз: "
                               f"'{habit.prize}'")
                send_telegram_message(tg_chat, message)
    else:
        for habit in habits:
            if f"{current_date.time().hour}:{current_date.time().minute}" == f"{habit.time.hour}:{habit.time.minute}":
                count += 7
                tg_chat = habit.owner.tg_chat_id
                if habit.prize is None:
                    message = (f"Не забудь {habit.action} в {habit.time}' место: '{habit.place}'. И получи приз: "
                               f"'Твое хорошее настроение'")
                else:
                    message = (f"Не забудь {habit.action} в {habit.time}' место: '{habit.place}'. И получи приз: "
                               f"'{habit.prize}'")
                send_telegram_message(tg_chat, message)
