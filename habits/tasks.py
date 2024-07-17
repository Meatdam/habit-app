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
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    current_date_1 = datetime.datetime.now()

    for habit in habits:
        result_time = habit.time + datetime.timedelta(hours=UTC_HOUR)
        if (current_date == result_time.strftime("%Y-%m-%d %H:%M") and habit.is_daily is True
                and habit.mailing_sign is True and habit.time.day <= current_date_1.day + 7):

            tg_chat = habit.owner.tg_chat_id
            if habit.prize is None:
                message = (f"Не забудь {habit.action} в {habit.time}' место: '{habit.place}'. И получи приз: "
                           f"'Твое хорошее настроение'")
            else:
                message = (f"Не забудь {habit.action} в {habit.time}' место: '{habit.place}'. И получи приз: "
                           f"'{habit.prize}'")
            send_telegram_message(tg_chat, message)
        elif (current_date == result_time.strftime("%Y-%m-%d %H:%M")
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
        elif habit.mailing_sign is False and habit.time.day + 7 == current_date_1.day:
            habit.mailing_sign = True
            habit.save()
            tg_chat = habit.owner.tg_chat_id
            if habit.prize is None:
                message = (f"Не забудь {habit.action} в {habit.time}' место: '{habit.place}'. И получи приз: "
                           f"'Твое хорошее настроение'")
            else:
                message = (f"Не забудь {habit.action} в {habit.time}' место: '{habit.place}'. И получи приз: "
                           f"'{habit.prize}'")
            send_telegram_message(tg_chat, message)
            habit.mailing_sign = False
