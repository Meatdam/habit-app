from celery import shared_task
from habits.models import Habits

import datetime
from habits.services import send_telegram_message


@shared_task
def send_habit():
    """
    Задача для отправки напоминаний о выполнении полезных привычек в телеграм чатах
    """
    UTC_HOUR = 5
    habits = Habits.objects.all()
    current_date = datetime.datetime.now()
    for habit in habits:
        if (f"{current_date.year}-{current_date.month}-{current_date.day} {current_date.hour}:{current_date.minute}" ==
                f"{habit.time.year}-{habit.time.month}-{habit.time.day} {habit.time.hour + UTC_HOUR}:"
                f"{habit.time.minute}"
                and habit.is_daily is True and habit.mailing_sign is True and habit.time.day <= current_date.day + 7):

            tg_chat = habit.owner.tg_chat_id
            if habit.prize is None:
                message = (f"Не забудь {habit.action} в {habit.time}' место: '{habit.place}'. И получи приз: "
                           f"'Твое хорошее настроение'")
            else:
                message = (f"Не забудь {habit.action} в {habit.time}' место: '{habit.place}'. И получи приз: "
                           f"'{habit.prize}'")
            send_telegram_message(tg_chat, message)
        elif (f"{current_date.year}-{current_date.month}-{current_date.day} {current_date.hour}:"
              f"{current_date.minute}" == f"{habit.time.year}-{habit.time.month}-{habit.time.day} "
                                          f"{habit.time.hour + UTC_HOUR}:"
                f"{habit.time.minute}"
                and habit.is_daily is False and habit.mailing_sign is True):
            habit.mailing_sign = False
            habit.save()
            tg_chat = habit.owner.tg_chat_id
            if habit.prize is None:
                message = (f"Не забудь {habit.action} в {habit.time}' место: '{habit.place}'. И получи приз: "
                           f"'Твое хорошее настроение'")
            else:
                message = (f"Не забудь {habit.action} в {habit.time}' место: '{habit.place}'. И получи приз: "
                           f"'{habit.prize}'")
            send_telegram_message(tg_chat, message)
